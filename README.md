# VTEX Agent & LLM Context

## Objetivo

Este repositório fornece **contexto estruturado para ferramentas de IA (LLMs)**, com o intuito de gerar códigos, componentes e integrações precisas para projetos em **VTEX IO**.

Ao ser integrado ao repositório de uma loja, ele atua como base de conhecimento ("skills") para editores de código orientados a IA, como **Cursor, Cloud CLI, Codex e Antigravity**. Isso reduz respostas incorretas da IA e ajuda a ferramenta a entender os padrões arquiteturais, o uso correto de blocos, as regras de estilização (CSS handles) e as práticas de backend recomendadas para o Store Framework da VTEX.

---

## Mapeamento das Documentações (SKILL.md)

Para evitar que a IA receba excesso de informações desnecessárias em cada pedido, utilizamos um mapeamento de arquivos focado em palavras-chave.

O arquivo principal para esse controle é o [`skills/vtex-io-core/SKILL.md`](./skills/vtex-io-core/SKILL.md). Ele contém a tabela **Guide Index**, que faz a relação entre:
- O **caminho do arquivo** com a documentação.
- As **palavras-chave (triggers)** que indicam sobre o que ele se refere.

Quando um desenvolvedor solicita algo na IA (ex: *"criar um layout responsivo"*), a ferramenta lê o `SKILL.md`, identifica a palavra-chave `responsivo` e carrega **somente** o arquivo de documentação vinculado àquele termo.

---

## Adicionando Novas Documentações

Para adicionar novos guias ao repositório para que a IA os utilize:

1. **Crie o arquivo Markdown (.md):** Escreva a sua documentação e salve em uma das pastas dentro de `skills/vtex-io-core/` (como `components/` ou `contexts/`).
2. **Atualize o Mapeamento:** Abra o arquivo `skills/vtex-io-core/SKILL.md`, localize a tabela **Guide Index** e adicione uma linha relacionando o caminho do seu arquivo às palavras-chave adequadas.
   
Exemplo:
```markdown
| `skills/vtex-io-core/components/seu-guia.md` | 🟡 MEDIUM | palavras-chave, termos, de, busca | Descrição breve do arquivo |
```

---

## Documentações Automáticas (Scraping)

Para facilitar a manutenção, o script [`scrape_requests.py`](./scrape_requests.py) busca e baixa os arquivos descritivos `README.md` dos repositórios nativos da VTEX no GitHub. O conteúdo é convertido em arquivos Markdown e salvo dentro de `skills/vtex-io-core/components/`.

### Adicionando Notas Manuais em Arquivos de Scraping

Todo o conteúdo extraído do GitHub pelo script de scraping é delimitado por duas tags no arquivo gerado:

```markdown
<!-- SCRAPED:START -->
(Conteúdo oficial do GitHub atualizado pelo script)
<!-- SCRAPED:END -->
```

**Como editar:** Se você quiser adicionar informações personalizadas da sua equipe, exemplos ou dicas nestes arquivos, não edite dentro desse delimitador. 
Sempre escreva o novo conteúdo **antes** ou **depois** dessas tags. 

Dessa forma, na próxima vez que o script rodar, ele atualizará apenas a seção do meio mantendo as suas informações manuais a salvo nas extremidades do arquivo.

---

## Uso com Git Submodules

A melhor forma de integrar este banco de contexto com os repositórios reais da sua loja VTEX é o adicionando como um **Submódulo do Git**. 

Isso mantém as documentações versionadas e consumíveis pelo projeto raiz, sem misturar os conflitos de commit.

### 1. Adicionando ao Projeto da Loja

Na raiz da pasta da sua loja local, adicione este repositório como um submódulo nomeando a pasta como `.vtex-agent-skills`:

```bash
git submodule add <URL_DESTE_REPOSITORIO> .vtex-agent-skills
git commit -m "chore: adiciona submodule de skills para IA"
```

A IA já terá acesso ao conhecimento através do caminho `.vtex-agent-skills/skills/vtex-io-core/SKILL.md`.

### 2. Clonando o Projeto

Desenvolvedores que clonarem o repositório da loja precisam iniciar os submódulos para baixar este diretório:

```bash
git submodule update --init --recursive
```

### 3. Commitando Atualizações

Se você alterar informações dentro da pasta do submódulo (`.vtex-agent-skills`), o push deve ser feito **primeiro no submódulo** e, em seguida, **no projeto da loja** para atualizar a referência.

```bash
# Entra no submódulo
cd .vtex-agent-skills

# Garante a branch principal e faz o push
git checkout main
git add .
git commit -m "docs: atualizando componente com dicas manuais"
git push origin main

# Volta para a loja e atualiza o ponteiro do submódulo
cd ..
git add .vtex-agent-skills
git commit -m "chore: atualizando ponteiro do submodule de skills"
git push origin main
```
