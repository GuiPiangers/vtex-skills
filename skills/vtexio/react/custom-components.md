# Custom Components

Utiliza o builder React para criar componentes customizados.


# 🧩 Composição de Blocos no Storefront (Correção Conceitual)

> **children** e **blocks** não são a mesma coisa e não têm o mesmo papel arquitetural.

## `children`

### Modelo mental

`children` funciona exatamente como `children` em um componente React.

### Comportamento

* Recebe um **array de blocos**
* Renderiza todos **em sequência direta**
* Não depende de ExtensionPoint
* É composição **estrutural**

### Semântica

```json
{
  "children": [
    "flex-layout.row#header",
    "flex-layout.row#content"
  ]
}
```

Equivale a:

```tsx
<Component>
  <Header />
  <Content />
</Component>
```

📌 **children = composição direta de layout**

---

## `blocks`

### Modelo mental

`blocks` é um sistema de **injeção dinâmica de componentes** via `ExtensionPoint`.

### Funcionamento técnico

* Renderizado pelo `vtex.render-runtime`
* Depende de `<ExtensionPoint />`
* O `id` do ExtensionPoint deve ser **idêntico** ao nome do bloco

### Exemplo

#### Interface do componente

```tsx
import { ExtensionPoint } from 'vtex.render-runtime'

const TelemarketingSlot = () => {
  return <ExtensionPoint id="telemarketing" />
}
```

#### Declaração no JSON

```json
{
  "blocks": [
    "telemarketing"
  ]
}
```

Isso renderiza o bloco **no ponto exato** onde o ExtensionPoint foi definido.

📌 **blocks = composição por injeção (slot system)**

---

# 🧠 Regra Arquitetural

| Propriedade | Função                     | Tipo de composição |
| ----------- | -------------------------- | ------------------ |
| `children`  | Renderização direta        | Estrutural         |
| `blocks`    | Injeção via ExtensionPoint | Slot / Plugin      |

---

# 🧬 Modelo Mental Correto

* `children` → árvore fixa
* `blocks` → pontos de extensão

```text
children  = estrutura
blocks    = extensão
```

---

# 🚦 Regras de uso

### Use `children` quando:

* Layout
* Estrutura
* Organização visual
* Hierarquia de página

### Use `blocks` quando:

* Customização dinâmica
* Injeção de funcionalidades
* Extensibilidade
* Plugin architecture
* Ponto de integração
