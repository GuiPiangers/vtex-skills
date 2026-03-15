import os
import sys
import re
import requests
from bs4 import BeautifulSoup
import html2text

# ---------------------------------------------------------------------------
# Marcadores de seção gerenciada pelo scraping
# ---------------------------------------------------------------------------
SCRAPE_START = "<!-- SCRAPED:START -->"
SCRAPE_END   = "<!-- SCRAPED:END -->"


def fetch_page(url):
    """Realiza a requisição para a página e retorna o HTML parsed."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return None


def extract_links(soup, base_url="https://developers.vtex.com"):
    """Extrai os links dos elementos `a` dentro da classe especificada."""
    links = []
    containers = soup.select('.styles_flexWrap.css-4cffwv')

    if not containers:
        print("Aviso: Nenhum container com a classe 'styles_flexWrap css-4cffwv' encontrado.")
        return links

    for container in containers:
        anchors = container.find_all('a')
        for a in anchors:
            href = a.get('href')
            if href:
                if href.startswith('/'):
                    href = base_url + href
                links.append(href)

    return list(dict.fromkeys(links))


def format_filename(title):
    """Formata o título para ser usado como nome de arquivo (slugify)."""
    filename = re.sub(r'[^\w\s-]', '', title).strip().lower()
    filename = re.sub(r'[-\s]+', '-', filename)
    return f"{filename}.md"


def extract_code_lines(code_scroll_parent):
    """
    Extrai as linhas de código do bloco VTEX corretamente.

    Estrutura real do HTML da VTEX:
      .ch-code-scroll-parent  (contém data-ch-lang)
        └── .ch-code-scroll-content
              └── div  (container absoluto com todas as linhas)
                    ├── span.ch-code-line-number  "1"
                    ├── div  →  conteúdo da linha 1
                    ├── span.ch-code-line-number  "2"
                    ├── div  →  conteúdo da linha 2
                    ...

    Cada div de conteúdo possui um div interno inline-block com spans coloridos.
    As linhas reais são os divs que NÃO são .ch-code-line-number.
    """
    scroll_content = code_scroll_parent.select_one('.ch-code-scroll-content')
    if not scroll_content:
        # Fallback: tenta extração simples removendo números de linha
        for ln in code_scroll_parent.select('.ch-code-line-number'):
            ln.extract()
        return code_scroll_parent.get_text(separator='\n')

    # O container absoluto com todas as linhas intercaladas
    container = scroll_content.find('div')
    if not container:
        return ''

    lines = []
    for child in container.children:
        if not hasattr(child, 'name'):
            continue
        # Pula os números de linha
        if 'ch-code-line-number' in (child.get('class') or []):
            continue
        # Cada div restante é uma linha de código
        line_text = child.get_text()
        # Trata \n escapado literalmente (comum na VTEX docs)
        line_text = line_text.replace('\\n', '\n')
        lines.append(line_text)

    return '\n'.join(lines)


def fix_code_blocks(soup, full_soup):
    """
    Encontra os blocos de código com a classe `ch-codeblock`,
    extrai o texto linha a linha e substitui por um placeholder único.

    Retorna um dicionário { placeholder: fenced_code_block } para
    ser restaurado após a conversão para Markdown, garantindo que
    os blocos fiquem com cercas (```) e linguagem correta.
    """
    placeholders = {}

    for i, codeblock in enumerate(soup.select('.ch-codeblock')):
        code_scroll_parent = codeblock.select_one('.ch-code-scroll-parent')
        if not code_scroll_parent:
            continue

        # lang fica em data-ch-lang no .ch-code-scroll-parent
        lang = code_scroll_parent.get('data-ch-lang', '')

        # Extrai linhas corretamente
        raw_code = extract_code_lines(code_scroll_parent).strip()

        # Monta o bloco cercado com backticks e linguagem
        fence = f"```{lang}\n{raw_code}\n```"

        # Placeholder único que sobrevive à conversão HTML→MD
        placeholder = f"CODEBLOCK_PLACEHOLDER_{i}"
        placeholders[placeholder] = fence

        # Substitui o bloco inteiro pelo placeholder no HTML
        placeholder_tag = full_soup.new_tag("p")
        placeholder_tag.string = placeholder
        codeblock.insert_after(placeholder_tag)
        codeblock.extract()

    return placeholders


def restore_code_blocks(markdown, placeholders):
    """
    Substitui os placeholders no Markdown final pelos blocos
    de código cercados com backticks.
    """
    for placeholder, fence in placeholders.items():
        markdown = markdown.replace(placeholder, f"\n{fence}\n")
    return markdown


# ---------------------------------------------------------------------------
# Merge logic
# ---------------------------------------------------------------------------

def read_manual_content(filepath):
    """
    Lê o conteúdo manual de um arquivo existente — tudo que está
    FORA dos marcadores SCRAPED:START / SCRAPED:END.

    Retorna uma tupla (before, after) onde:
      - before: texto antes de SCRAPED:START (ex: título manual no topo)
      - after:  texto após SCRAPED:END (ex: seções de boas práticas, exemplos)

    Se o arquivo não existir ou não tiver marcadores, retorna ("", "").
    """
    if not os.path.exists(filepath):
        return ("", "")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if SCRAPE_START not in content:
        # Arquivo existe mas foi criado antes do sistema de marcadores.
        # Trata o conteúdo inteiro como seção "after" para preservar tudo.
        print(f"  [Aviso] Arquivo sem marcadores encontrado. Conteúdo preservado como seção manual.")
        return ("", content)

    start_idx = content.index(SCRAPE_START)
    end_idx   = content.index(SCRAPE_END) + len(SCRAPE_END)

    before = content[:start_idx].rstrip('\n')
    after  = content[end_idx:].lstrip('\n')

    return (before, after)


def build_merged_content(title, scraped_markdown, before, after):
    """
    Monta o arquivo final mesclando o conteúdo scraped com o conteúdo manual.

    Estrutura resultante:
      {before}                  ← conteúdo manual acima (se houver)
      <!-- SCRAPED:START -->
      # Título
      {scraped_markdown}        ← atualizado a cada scraping
      <!-- SCRAPED:END -->
      {after}                   ← suas adições manuais (nunca sobrescritas)
    """
    scraped_block = (
        f"{SCRAPE_START}\n"
        f"# {title}\n\n"
        f"{scraped_markdown.strip()}\n"
        f"{SCRAPE_END}"
    )

    parts = []
    if before:
        parts.append(before)
    parts.append(scraped_block)
    if after:
        parts.append(after)

    return '\n\n'.join(parts) + '\n'


# ---------------------------------------------------------------------------
# Scrape principal
# ---------------------------------------------------------------------------

def scrape_component(url, output_dir):
    """Navega para a URL de um componente, extrai o conteúdo e salva em markdown."""
    print(f"Scrape: {url}")
    soup = fetch_page(url)
    if not soup:
        return

    # Título
    title_element = soup.select_one('.title.css-1s43qfw')
    if title_element:
        title_text = title_element.get_text(strip=True)
    else:
        print(f"  [Aviso] Título não encontrado para {url}. Usando 'Componente Desconhecido'.")
        title_text = "Componente Desconhecido"

    # Conteúdo
    content_element = soup.select_one('.css-iourwr')
    if not content_element:
        print(f"  [Aviso] Conteúdo (css-iourwr) não encontrado para {url}.")
        return

    # Substitui blocos de código por placeholders antes da conversão
    placeholders = fix_code_blocks(content_element, soup)

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.body_width = 0
    converter.protect_links = True
    converter.use_automatic_links = False

    scraped_markdown = converter.handle(str(content_element))

    # Restaura os blocos de código com cercas (```) no lugar dos placeholders
    scraped_markdown = restore_code_blocks(scraped_markdown, placeholders)

    # Caminho do arquivo
    filename = format_filename(title_text)
    filepath = os.path.join(output_dir, filename)

    # Lê conteúdo manual existente (preserva seções fora dos marcadores)
    before, after = read_manual_content(filepath)

    # Monta conteúdo final mesclado
    final_content = build_merged_content(title_text, scraped_markdown, before, after)

    # Salva
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        action = "Atualizado" if os.path.exists(filepath) else "Criado"
        print(f"  -> {action}: {filepath}")
    except IOError as e:
        print(f"  [Erro] Falha ao salvar arquivo {filepath}: {e}")


# ---------------------------------------------------------------------------
# Links
# ---------------------------------------------------------------------------

BASIC_COMPONENTS_LINKS = [
    "https://developers.vtex.com/docs/apps/vtex.add-to-cart-button",
    "https://developers.vtex.com/docs/apps/vtex.breadcrumb",
    "https://developers.vtex.com/docs/apps/vtex.store-footer",
    "https://developers.vtex.com/docs/guides/google-one-tap-login",
    "https://developers.vtex.com/docs/apps/vtex.store-header",
    "https://developers.vtex.com/docs/apps/vtex.locale-switcher",
    "https://developers.vtex.com/docs/apps/vtex.login",
    "https://developers.vtex.com/docs/apps/vtex.menu",
    "https://developers.vtex.com/docs/apps/vtex.minicart",
    "https://developers.vtex.com/docs/apps/vtex.order-placed",
    "https://developers.vtex.com/docs/apps/vtex.product-customizer",
    "https://developers.vtex.com/docs/apps/vtex.product-identifier",
    "https://developers.vtex.com/docs/apps/vtex.product-list",
    "https://developers.vtex.com/docs/apps/vtex.product-price",
    "https://developers.vtex.com/docs/apps/vtex.product-quantity",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryspecificationbadges",
    "https://developers.vtex.com/docs/apps/vtex.product-summary",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryattachmentlist",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummarybrand",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummarybuybutton",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummarydescription",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryimage",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummarylist",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryname",
    "https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryskuselector",
    "https://developers.vtex.com/docs/apps/vtex.rich-text",
    "https://developers.vtex.com/docs/apps/vtex.search",
    "https://developers.vtex.com/docs/apps/vtex.search-result",
    "https://developers.vtex.com/docs/apps/vtex.shelf",
    "https://developers.vtex.com/docs/apps/vtex.store-image"
]

LAYOUT_LINKS = [
    "https://developers.vtex.com/docs/apps/vtex.condition-layout",
    "https://developers.vtex.com/docs/apps/vtex.flex-layout",
    "https://developers.vtex.com/docs/apps/vtex.disclosure-layout",
    "https://developers.vtex.com/docs/apps/vtex.modal-layout",
    "https://developers.vtex.com/docs/apps/vtex.overlay-layout",
    "https://developers.vtex.com/docs/apps/vtex.responsive-layout",
    "https://developers.vtex.com/docs/apps/vtex.slider-layout",
    "https://developers.vtex.com/docs/apps/vtex.stack-layout",
    "https://developers.vtex.com/docs/apps/vtex.sticky-layout",
    "https://developers.vtex.com/docs/apps/vtex.tab-layout"
]

ADVANCED_COMPONENTS_LINKS = [
    "https://developers.vtex.com/docs/apps/vtex.category-menu",
    "https://developers.vtex.com/docs/apps/vtex.iframe",
    "https://developers.vtex.com/docs/apps/vtex.product-availability",
    "https://developers.vtex.com/docs/apps/vtex.product-comparison",
    "https://developers.vtex.com/docs/apps/vtex.product-gifts",
    "https://developers.vtex.com/docs/apps/vtex.product-kit",
    "https://developers.vtex.com/docs/apps/vtex.recommendation-shelf",
    "https://developers.vtex.com/docs/apps/vtex.product-specification-badges",
    "https://developers.vtex.com/docs/apps/vtexventures.livestreaming",
    "https://developers.vtex.com/docs/apps/vtex.reviews-and-ratings",
    "https://developers.vtex.com/docs/apps/vtex.sandbox",
    "https://developers.vtex.com/docs/apps/vtex.seller-selector",
    "https://developers.vtex.com/docs/apps/vtex.store-drawer",
    "https://developers.vtex.com/docs/apps/vtex.store-locator",
    "https://developers.vtex.com/docs/apps/vtex.store-form",
    "https://developers.vtex.com/docs/apps/vtex.store-link",
    "https://developers.vtex.com/docs/apps/vtex.store-media",
    "https://developers.vtex.com/docs/apps/vtex.store-newsletter",
    "https://developers.vtex.com/docs/apps/vtex.store-video"
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    output_dir = './skills/vtex-io-core/components'
    os.makedirs(output_dir, exist_ok=True)

    component_links = LAYOUT_LINKS + BASIC_COMPONENTS_LINKS + ADVANCED_COMPONENTS_LINKS

    if not component_links:
        print("Nenhum link encontrado. Abortando.")
        sys.exit(0)

    print(f"Encontrados {len(component_links)} componentes. Iniciando scraping...\n")

    for link in component_links:
        scrape_component(link, output_dir)

    print("\nProcesso finalizado!")


if __name__ == '__main__':
    main()