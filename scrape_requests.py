import os
import sys
import re
import requests

# ---------------------------------------------------------------------------
# Marcadores de seção gerenciada pelo scraping
# ---------------------------------------------------------------------------
SCRAPE_START = "<!-- SCRAPED:START -->"
SCRAPE_END   = "<!-- SCRAPED:END -->"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}


# ---------------------------------------------------------------------------
# GitHub README fetch
# ---------------------------------------------------------------------------

def build_raw_url(github_url: str) -> str | None:
    """
    Converte uma URL do GitHub em URL raw para download direto.

    Suporta:
      https://github.com/vtex-apps/flex-layout
      https://github.com/vtex-apps/flex-layout/blob/master/docs/README.md
      https://raw.githubusercontent.com/...  (retorna sem alteração)

    Retorna None se a URL apontar apenas para o repo raiz
    (nesse caso fetch_readme tentará os caminhos padrão).
    """
    if 'raw.githubusercontent.com' in github_url:
        return github_url

    match = re.match(r'https://github\.com/([^/]+/[^/]+)', github_url)
    if not match:
        raise ValueError(f"URL GitHub inválida: {github_url}")

    # Se a URL aponta para um arquivo específico (blob ou tree)
    file_match = re.search(r'/(?:blob|tree)/([^/]+)/(.+)', github_url)
    if file_match:
        branch    = file_match.group(1)
        file_path = file_match.group(2)
        repo_path = match.group(1)
        return f"https://raw.githubusercontent.com/{repo_path}/{branch}/{file_path}"

    # URL apenas do repo — fetch_readme fará o fallback
    return None


def fetch_readme(github_url: str) -> tuple[str, str] | None:
    """
    Busca o README.md de um repositório GitHub.

    Tenta os caminhos e branches mais comuns nos vtex-apps, com fallback:
      master/README.md → master/docs/README.md → main/README.md → main/docs/README.md

    Retorna (titulo, conteudo_markdown) ou None se não encontrar.
    """
    raw_url = build_raw_url(github_url)
    if raw_url:
        return _fetch_raw(raw_url, github_url)

    match = re.match(r'https://github\.com/([^/]+)/([^/]+)', github_url)
    if not match:
        print(f"  [Erro] URL inválida: {github_url}")
        return None

    owner, repo = match.group(1), match.group(2)

    candidates = [
        (branch, path)
        for branch in ['master', 'main']
        for path in ['README.md', 'docs/README.md']
    ]

    for branch, path in candidates:
        url    = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
        result = _fetch_raw(url, github_url)
        if result:
            return result

    print(f"  [Erro] README não encontrado para {github_url}")
    return None


def _fetch_raw(raw_url: str, original_url: str) -> tuple[str, str] | None:
    """Faz o request para a URL raw e retorna (titulo, conteudo) ou None."""
    try:
        response = requests.get(raw_url, headers=HEADERS, timeout=15)
        if response.status_code == 404:
            return None
        response.raise_for_status()

        content = response.text
        title   = extract_title_from_markdown(content, original_url)
        return (title, content)

    except requests.RequestException as e:
        print(f"  [Erro] {raw_url}: {e}")
        return None


def extract_title_from_markdown(content: str, fallback_url: str) -> str:
    """
    Extrai o título do README a partir do primeiro H1 (`# Título`).
    Fallback: nome do repositório extraído da URL.
    """
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith('# '):
            return stripped[2:].strip()

    match = re.search(r'github\.com/[^/]+/([^/]+)', fallback_url)
    if match:
        return match.group(1).replace('-', ' ').title()

    return 'Unknown Component'


# ---------------------------------------------------------------------------
# Filename
# ---------------------------------------------------------------------------

def format_filename(title: str) -> str:
    """Formata o título para ser usado como nome de arquivo (slugify)."""
    filename = re.sub(r'[^\w\s-]', '', title).strip().lower()
    filename = re.sub(r'[-\s]+', '-', filename)
    return f"{filename}.md"


# ---------------------------------------------------------------------------
# Merge logic
# ---------------------------------------------------------------------------

def read_manual_content(filepath: str) -> tuple[str, str]:
    """
    Lê o conteúdo manual de um arquivo existente — tudo fora dos marcadores.

    Retorna (before, after):
      - before: texto antes de SCRAPED:START
      - after:  texto após SCRAPED:END (suas adições manuais, nunca sobrescritas)

    Se o arquivo não existir ou não tiver marcadores, retorna ("", "").
    Arquivos sem marcadores têm o conteúdo inteiro preservado como seção "after".
    """
    if not os.path.exists(filepath):
        return ("", "")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if SCRAPE_START not in content:
        print(f"  [Aviso] Arquivo sem marcadores. Conteúdo preservado como seção manual.")
        return ("", content)

    start_idx = content.index(SCRAPE_START)
    end_idx   = content.index(SCRAPE_END) + len(SCRAPE_END)

    before = content[:start_idx].rstrip('\n')
    after  = content[end_idx:].lstrip('\n')

    return (before, after)


def build_merged_content(readme_markdown: str, before: str, after: str) -> str:
    """
    Monta o arquivo final mesclando o README scraped com o conteúdo manual.

    Estrutura resultante:
      {before}                ← conteúdo manual acima (se houver)
      <!-- SCRAPED:START -->
      {readme_markdown}       ← README do GitHub, atualizado a cada scraping
      <!-- SCRAPED:END -->
      {after}                 ← suas adições manuais (nunca sobrescritas)
    """
    scraped_block = (
        f"{SCRAPE_START}\n"
        f"{readme_markdown.strip()}\n"
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

def scrape_component(github_url: str, output_dir: str) -> None:
    """Busca o README de um repositório GitHub e salva como markdown."""
    print(f"Scrape: {github_url}")

    result = fetch_readme(github_url)
    if not result:
        return

    title, readme_markdown = result

    filename  = format_filename(title)
    filepath  = os.path.join(output_dir, filename)
    file_exists = os.path.exists(filepath)

    before, after = read_manual_content(filepath)
    final_content = build_merged_content(readme_markdown, before, after)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        action = "Atualizado" if file_exists else "Criado"
        print(f"  -> {action}: {filepath}  [{title}]")
    except IOError as e:
        print(f"  [Erro] Falha ao salvar {filepath}: {e}")


# ---------------------------------------------------------------------------
# Repositórios
# ---------------------------------------------------------------------------

BASIC_COMPONENTS = [
    "https://github.com/vtex-apps/add-to-cart-button",
    "https://github.com/vtex-apps/breadcrumb",
    "https://github.com/vtex-apps/store-footer",
    "https://github.com/vtex-apps/store-header",
    "https://github.com/vtex-apps/locale-switcher",
    "https://github.com/vtex-apps/login",
    "https://github.com/vtex-apps/menu",
    "https://github.com/vtex-apps/minicart",
    "https://github.com/vtex-apps/order-placed",
    "https://github.com/vtex-apps/product-customizer",
    "https://github.com/vtex-apps/product-identifier",
    "https://github.com/vtex-apps/product-list",
    "https://github.com/vtex-apps/product-price",
    "https://github.com/vtex-apps/product-quantity",
    "https://github.com/vtex-apps/product-summary",
    "https://github.com/vtex-apps/rich-text",
    "https://github.com/vtex-apps/search",
    "https://github.com/vtex-apps/search-result",
    "https://github.com/vtex-apps/shelf",
    "https://github.com/vtex-apps/store-image",
]

LAYOUT = [
    "https://github.com/vtex-apps/condition-layout",
    "https://github.com/vtex-apps/flex-layout",
    "https://github.com/vtex-apps/disclosure-layout",
    "https://github.com/vtex-apps/modal-layout",
    "https://github.com/vtex-apps/overlay-layout",
    "https://github.com/vtex-apps/responsive-layout",
    "https://github.com/vtex-apps/slider-layout",
    "https://github.com/vtex-apps/stack-layout",
    "https://github.com/vtex-apps/sticky-layout",
    "https://github.com/vtex-apps/tab-layout",
]

ADVANCED_COMPONENTS = [
    "https://github.com/vtex-apps/category-menu",
    "https://github.com/vtex-apps/iframe",
    "https://github.com/vtex-apps/product-availability",
    "https://github.com/vtex-apps/product-comparison",
    "https://github.com/vtex-apps/product-gifts",
    "https://github.com/vtex-apps/product-kit",
    "https://github.com/vtex-apps/recommendation-shelf",
    "https://github.com/vtex-apps/product-specification-badges",
    "https://github.com/vtex-apps/reviews-and-ratings",
    "https://github.com/vtex-apps/sandbox",
    "https://github.com/vtex-apps/seller-selector",
    "https://github.com/vtex-apps/store-drawer",
    "https://github.com/vtex-apps/store-locator",
    "https://github.com/vtex-apps/store-form",
    "https://github.com/vtex-apps/store-link",
    "https://github.com/vtex-apps/store-media",
    "https://github.com/vtex-apps/store-newsletter",
    "https://github.com/vtex-apps/store-video",
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    output_dir = './skills/vtex-io-core/components'
    os.makedirs(output_dir, exist_ok=True)

    all_links = LAYOUT + BASIC_COMPONENTS + ADVANCED_COMPONENTS

    print(f"Total: {len(all_links)} repositórios. Iniciando scraping...\n")

    for link in all_links:
        scrape_component(link, output_dir)

    print("\nProcesso finalizado!")


if __name__ == '__main__':
    main()