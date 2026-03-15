# Custom Components Guide

> **Purpose:** Create custom VTEX IO blocks with React  
> **Rule:** Custom blocks are declarative units rendered by Store Framework, not traditional React components

---

## 🧱 COMPONENT ARCHITECTURE

A VTEX IO custom component consists of:

1. **manifest.json** - App definition
2. **store/interfaces.json** - Block declaration
3. **React component** - Implementation (`/react`)
4. **Schema** - Site Editor config (optional)
5. **CSS Handles** - Styling hooks

---

## 📂 FILE STRUCTURE

```
my-app/
├── manifest.json
├── react/
│   ├── MyComponent.tsx      # Must export default
│   └── components/
│       └── OtherComponent.tsx
└── store/
    ├── interfaces.json      # Block declarations live here, inside /store
    └── blocks.json
```

---

## 🔧 SETUP STEPS

### 1. Define Block in `store/interfaces.json`

```json
{
  "my-app.my-component": {
    "component": "MyComponent"
  }
}
```

**Rules:**
- File lives inside `/store/interfaces.json`, not in the root
- Key = block name used in JSON (`my-app.my-component`)
- `component` = React component file name in `/react`
- Component must be **default export**

---

### 2. Create React Component

```tsx
// react/MyComponent.tsx
import React from 'react'
import { useCssHandles } from 'vtex.css-handles'

interface Props {
  title: string
  showIcon?: boolean
}

const CSS_HANDLES = ['container', 'title', 'icon'] as const

const MyComponent: React.FC<Props> = ({ title, showIcon = true }) => {
  const handles = useCssHandles(CSS_HANDLES)

  return (
    <div className={handles.container}>
      <h2 className={handles.title}>{title}</h2>
      {showIcon && <span className={handles.icon}>✓</span>}
    </div>
  )
}

export default MyComponent
```

---

### 3. Use Block in Storefront

```json
{
  "my-app.my-component#telemarketing": {
    "props": {
      "title": "Central de Vendas",
      "showIcon": true
    }
  }
}
```

---

## 🎯 BLOCK NAMING

### Convention
```
vendor.app.component#semantic-context
```

### Examples
```
store.telemarketing.slot#pdp
acme.custom-banner#homepage
mystore.product-info#main
```

**Rule:** `#context` defines semantic scope, not technical instance.

---

## 🧾 SCHEMA (Site Editor Configuration)

Enables visual editing in VTEX Admin.

```tsx
// Add to component file
MyComponent.schema = {
  title: 'Telemarketing Component',
  type: 'object',
  properties: {
    title: {
      type: 'string',
      title: 'Title',
      default: 'Customer Service'
    },
    showIcon: {
      type: 'boolean',
      title: 'Show Icon',
      default: true
    }
  }
}
```

**Without schema = no Site Editor support**

---

## 🎨 CSS HANDLES

### Declaration

```tsx
import { useCssHandles } from 'vtex.css-handles'

const CSS_HANDLES = ['container', 'title', 'icon'] as const

const MyComponent = () => {
  const handles = useCssHandles(CSS_HANDLES)

  return (
    <div className={handles.container}>
      <span className={handles.title}>Text</span>
    </div>
  )
}
```

### Generated Classes

```html
<div class="vtex-my-app-1-x-container">
  <span class="vtex-my-app-1-x-title">Text</span>
</div>
```

---

## ⚠️ CRITICAL: Cross-App Styling Rule

**CSS Handles only work when styled from a different app.**

### ❌ Same App (Won't Work)

```css
/* In my-app */
.container { 
  padding: 1rem;  /* IGNORED */
}
```

### ✅ Different App (Correct)

```css
/* In store-theme or another app */
.vtex-my-app-1-x-container {
  padding: 1rem;  /* WORKS */
}
```

**Rule:** Component defines structure. Another app defines style.

> **Tip:** Prefer Tachyons utility classes for simple layout and spacing needs, as they are already available in Store Framework without requiring cross-app styling.

---

## 🧩 COMPOSITION:

### `children` - Direct Composition

**In `store/interfaces.json`:**

```json
{
  "my-component": {
    "component": "MyComponent",
    "composition": "children"
  }
}
```

Renders blocks directly, in same declaration order.

```json
{
  "my-component": {
    "children": [
      "flex-layout.row#header",
      "flex-layout.row#content"
    ]
  }
}
```

**In React custom component:**
```tsx
import React, { PropsWithChildren } from 'react'

const MyComponent: React.FC<PropsWithChildren<Props>> = ({ children }) => (
  <div>{children}</div> // renders flex-layout.row#header and flex-layout.row#content in declaration order
)
```

**Use for:** Layout, children composition

---

### `Blocks`
Dynamic injection via `<ExtensionPoint />`.

**In React:**
```tsx
import { ExtensionPoint } from 'vtex.render-runtime'

const MyComponent = () => {
  return (
    <div>
      <h1>Header</h1>
      <ExtensionPoint 
        id="custom-block"
        {...props} // You can pass props to the injected component. If the component has schema declared, the user can overwrite these props in Site Editor
      />
    </div>
  )
}
```

**In `store/interfaces.json`:**
```json
{
  "my-component": {
    "component": "MyComponent",
    "composition": "blocks",
    "allowed": ["custom-block"]
  },
  "custom-block": {}
}
```

**In store JSON:**
```json
{
  "my-component": {
    "blocks": [
      "custom-block"
    ]
  },
  "custom-block": {}
}
```

**Use for:** Plugin system

---

### `Slots`
Dynamic injection via props.

**In React:**
```tsx
import React, { ReactElement } from 'react'

interface Props {
  CustomComponent: ReactElement
}

const MyComponent = ({ CustomComponent }: Props) => {
  return (
    <div>
      <h1>Header</h1>
      <CustomComponent 
        {...props} // You can pass props to the injected component. If the component has schema declared, the user can overwrite these props in Site Editor
      />
    </div>
  )
}
```

**In `store/interfaces.json`:**
```json
{
  "my-component": {
    "component": "MyComponent"
  }
}
```

**In store JSON:**
```json
{
  "my-component": {
    "props": {
      "CustomComponent": "any-component"
    }
  }
}
```

**Rules**: 

- Slot props **must** be declared in PascalCase: `CustomComponent` ✅ — `custom_component` ❌
- Slot props **cannot** be nested inside other objects:
  - ✅ `"props": { "CustomComponent": "any-component" }`
  - ❌ `"props": { "nested": { "CustomComponent": "any-component" } }`
- No need to declare `allowed` in `interfaces.json` — any block from any app can be passed as a slot

**Use for:** Plugin system, dynamic content

---

## 📋 COMPARISON TABLE

| Feature | `children` | `blocks` | `slots` |
|---------|-----------|----------|---------|
| **Mechanism** | Direct render | ExtensionPoint injection | Props injection |
| **Structure** | Fixed | Dynamic | Dynamic |
| **Use case** | Layout hierarchy | Plugin System | Plugin System |
| **Requires** | `PropsWithChildren` in React | `<ExtensionPoint />` in React, `allowed` in `interfaces.json`, dependencies in `manifest.json` | Nothing extra |

---

**Prefer Slots over Blocks** — simpler and more flexible. Use `children` for fixed layout hierarchy.

---

## 📡 DATA FETCHING

**Never access APIs directly from components.**

### ✅ Use Hooks

```tsx
import { useProduct } from 'vtex.product-context'
import { useOrderForm } from 'vtex.order-manager/OrderForm'

const MyComponent = () => {
  const product = useProduct()
  const { orderForm } = useOrderForm()
  
  return <div>{product?.productName}</div>
}
```

### ✅ Use Props

```tsx
interface Props {
  data: ProductData
}

const MyComponent: React.FC<Props> = ({ data }) => {
  return <div>{data.name}</div>
}
```

### ❌ Don't Use Direct API Calls

```tsx
// WRONG
const MyComponent = () => {
  const [data, setData] = useState()
  
  useEffect(() => {
    fetch('/api/products')  // ❌ Never do this
      .then(res => setData(res))
  }, [])
}
```

---

## 🚦 BEST PRACTICES

```
✓ Use TypeScript for Props interface
✓ Use CSS Handles for all styling
✓ Prefer Tachyons for simple layout/spacing
✓ Add Schema for Site Editor support
✓ Use semantic block naming
✓ Separate concerns (structure/behavior/style)
✓ Use hooks for data fetching
✓ Export component as default
✓ Use PropsWithChildren when using children composition
```

---

## 🚫 ANTI-PATTERNS

```
❌ Inline styles
❌ Styling CSS handles in same app
❌ Direct API calls from component
❌ Using `any` type
❌ God components (too many responsibilities)
❌ Anonymous blocks (no #context)
❌ Missing default export
❌ Lowercase slot prop names (use PascalCase)
❌ Nested slot props inside objects
```

---

## 📋 COMPLETE EXAMPLE

### store/interfaces.json
```json
{
  "store.product-badge": {
    "component": "ProductBadge"
  }
}
```

### react/ProductBadge.tsx
```tsx
import React from 'react'
import { useCssHandles } from 'vtex.css-handles'
import { useProduct } from 'vtex.product-context'

interface Props {
  label?: string
  showDiscount?: boolean
}

const CSS_HANDLES = ['badge', 'label', 'discount'] as const

const ProductBadge: React.FC<Props> = ({ 
  label = 'New',
  showDiscount = true 
}) => {
  const handles = useCssHandles(CSS_HANDLES)
  const product = useProduct()
  
  const discount = product?.discountPercentage

  return (
    <div className={handles.badge}>
      <span className={handles.label}>{label}</span>
      {showDiscount && discount && (
        <span className={handles.discount}>-{discount}%</span>
      )}
    </div>
  )
}

ProductBadge.schema = {
  title: 'Product Badge',
  type: 'object',
  properties: {
    label: {
      type: 'string',
      title: 'Label',
      default: 'New'
    },
    showDiscount: {
      type: 'boolean',
      title: 'Show Discount',
      default: true
    }
  }
}

export default ProductBadge
```

### store/blocks/product.json
```json
{
  "store.product-badge#featured": {
    "props": {
      "label": "Featured",
      "showDiscount": false
    }
  }
}
```

### Styling (in store-theme)
```css
.vtex-store-1-x-badge {
  display: inline-flex;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #000;
  color: #fff;
}

.vtex-store-1-x-label {
  font-weight: bold;
}

.vtex-store-1-x-discount {
  color: #ff0000;
}
```

---

## 🧠 MENTAL MODEL

```
store/interfaces.json  → Declares block exists (lives inside /store, not root)
React component        → Implements behavior
Schema                 → Enables admin config
CSS Handles            → Provides style hooks (styled from another app)
JSON blocks            → Uses block in storefront
Another app CSS        → Applies visual style
```

---

## 📚 COMMON HOOKS

```tsx
// Product data
import { useProduct } from 'vtex.product-context'

// Cart/Order
import { useOrderForm } from 'vtex.order-manager/OrderForm'

// Runtime context
import { useRuntime } from 'vtex.render-runtime'

// Pixel events
import { usePixel } from 'vtex.pixel-manager'
```

---