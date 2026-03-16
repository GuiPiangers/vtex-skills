---
name: vtex-io-core
description: Central VTEX IO knowledge system. Defines architectural standards, block behaviors, frontend patterns, React custom components, hooks, and VTEX backend (clients, middlewares, routes). This is not documentation — it's operational intelligence.
---

# VTEX IO CORE SKILL

> Operational intelligence for VTEX IO Store Framework development

---

## 🎯 OPERATIONAL PROTOCOL

```
1. Identify task domain (use Domain Classification table)
2. Match keywords to Guide Index triggers
3. Load guide(s) by priority (🔴 → 🟠 → 🟡)
4. Apply patterns from guide
5. Never load all guides - load on-demand only
```

**Priority Loading Order:**
- 🔴 **CRITICAL** - Core architectural patterns (load first)
- 🟠 **HIGH** - Common features (load when needed)
- 🟡 **MEDIUM** - Specific implementations (load for specialized tasks)

**Example Workflow:**
```
User: "Create a product grid with custom styling"

Agent reasoning:
1. Domain: Layout + Components
2. Triggers match: "grid", "layout", "custom"
3. Priority loads:
   - skills/vtex-io-core/components/flex-layout.md (🔴 CRITICAL)
   - skills/vtex-io-core/components/product-summary.md (🟠 HIGH)
4. Apply patterns from loaded guides
```

---

## 📂 GUIDE INDEX

| Guide | Priority | Triggers | Purpose |
|-------|----------|----------|---------|
| **Components** ||||
| `skills/vtex-io-core/components/flex-layout.md` | 🔴 **CRITICAL** | grid, row, col, layout, structure, flexbox | Flexbox layout system |
| `skills/vtex-io-core/components/slider-layout.md` | 🟡 MEDIUM | slider, carousel, slide | Slider layout system |
| `skills/vtex-io-core/components/responsive-layout.md` | 🟡 MEDIUM | mobile, responsive, breakpoint, device | Responsive patterns |
| `skills/vtex-io-core/components/custom-components.md` | 🔴 **CRITICAL** | create block, custom component, new block, React | Build custom blocks |
| `skills/vtex-io-core/components/product-summary.md` | 🟠 HIGH | product card, shelf, product list, showcase | Product displays |
| `skills/vtex-io-core/components/product-prices.md` | 🟠 HIGH | product prices, shelf, product price | Product prices display |
| **Components (Official Docs, Scraped)** ||||
| `skills/vtex-io-core/components/add-to-cart-button.md` | 🟠 HIGH | add to cart button, add-to-cart-button | Official component documentation (scraped): add to cart button |
| `skills/vtex-io-core/components/breadcrumb.md` | 🟠 HIGH | breadcrumb, breadcrumb | Official component documentation (scraped): breadcrumb |
| `skills/vtex-io-core/components/category-menu.md` | 🟡 MEDIUM | category menu, category-menu | Official component documentation (scraped): category menu |
| `skills/vtex-io-core/components/componente-desconhecido.md` | 🟡 MEDIUM | componente desconhecido, componente-desconhecido | Official component documentation (scraped): componente desconhecido |
| `skills/vtex-io-core/components/condition-layout.md` | 🟡 MEDIUM | condition layout, condition-layout | Official component documentation (scraped): condition layout |
| `skills/vtex-io-core/components/disclosure-layout.md` | 🟡 MEDIUM | disclosure layout, disclosure-layout | Official component documentation (scraped): disclosure layout |
| `skills/vtex-io-core/components/drawer.md` | 🟡 MEDIUM | drawer, drawer | Official component documentation (scraped): drawer |
| `skills/vtex-io-core/components/footer.md` | 🟠 HIGH | footer, footer | Official component documentation (scraped): footer |
| `skills/vtex-io-core/components/header.md` | 🟠 HIGH | header, header | Official component documentation (scraped): header |
| `skills/vtex-io-core/components/iframe.md` | 🟡 MEDIUM | iframe, iframe | Official component documentation (scraped): iframe |
| `skills/vtex-io-core/components/live-shopping.md` | 🟡 MEDIUM | live shopping, live-shopping | Official component documentation (scraped): live shopping |
| `skills/vtex-io-core/components/locale-switcher.md` | 🟡 MEDIUM | locale switcher, locale-switcher | Official component documentation (scraped): locale switcher |
| `skills/vtex-io-core/components/login.md` | 🟠 HIGH | login, login | Official component documentation (scraped): login |
| `skills/vtex-io-core/components/media.md` | 🟡 MEDIUM | media, media | Official component documentation (scraped): media |
| `skills/vtex-io-core/components/menu.md` | 🟠 HIGH | menu, menu | Official component documentation (scraped): menu |
| `skills/vtex-io-core/components/minicart.md` | 🟠 HIGH | minicart, minicart | Official component documentation (scraped): minicart |
| `skills/vtex-io-core/components/modal-layout.md` | 🟡 MEDIUM | modal layout, modal-layout | Official component documentation (scraped): modal layout |
| `skills/vtex-io-core/components/order-placed.md` | 🟠 HIGH | order placed, order-placed | Official component documentation (scraped): order placed |
| `skills/vtex-io-core/components/overlay-layout.md` | 🟡 MEDIUM | overlay layout, overlay-layout | Official component documentation (scraped): overlay layout |
| `skills/vtex-io-core/components/product-availability.md` | 🟡 MEDIUM | product availability, product-availability | Official component documentation (scraped): product availability |
| `skills/vtex-io-core/components/product-comparison.md` | 🟡 MEDIUM | product comparison, product-comparison | Official component documentation (scraped): product comparison |
| `skills/vtex-io-core/components/product-customizer.md` | 🟡 MEDIUM | product customizer, product-customizer | Official component documentation (scraped): product customizer |
| `skills/vtex-io-core/components/product-gifts.md` | 🟡 MEDIUM | product gifts, product-gifts | Official component documentation (scraped): product gifts |
| `skills/vtex-io-core/components/product-identifier.md` | 🟡 MEDIUM | product identifier, product-identifier | Official component documentation (scraped): product identifier |
| `skills/vtex-io-core/components/product-list.md` | 🟠 HIGH | product list, product-list | Official component documentation (scraped): product list |
| `skills/vtex-io-core/components/product-price.md` | 🟠 HIGH | product price, product-price | Official component documentation (scraped): product price |
| `skills/vtex-io-core/components/product-quantity.md` | 🟡 MEDIUM | product quantity, product-quantity | Official component documentation (scraped): product quantity |
| `skills/vtex-io-core/components/product-specification-badges.md` | 🟡 MEDIUM | product specification badges, product-specification-badges | Official component documentation (scraped): product specification badges |
| `skills/vtex-io-core/components/product-summary-attachment-list.md` | 🟡 MEDIUM | product summary attachment list, product-summary-attachment-list | Official component documentation (scraped): product summary attachment list |
| `skills/vtex-io-core/components/product-summary-brand.md` | 🟡 MEDIUM | product summary brand, product-summary-brand | Official component documentation (scraped): product summary brand |
| `skills/vtex-io-core/components/product-summary-buy-button.md` | 🟡 MEDIUM | product summary buy button, product-summary-buy-button | Official component documentation (scraped): product summary buy button |
| `skills/vtex-io-core/components/product-summary-description.md` | 🟡 MEDIUM | product summary description, product-summary-description | Official component documentation (scraped): product summary description |
| `skills/vtex-io-core/components/product-summary-image.md` | 🟡 MEDIUM | product summary image, product-summary-image | Official component documentation (scraped): product summary image |
| `skills/vtex-io-core/components/product-summary-list.md` | 🟡 MEDIUM | product summary list, product-summary-list | Official component documentation (scraped): product summary list |
| `skills/vtex-io-core/components/product-summary-name.md` | 🟡 MEDIUM | product summary name, product-summary-name | Official component documentation (scraped): product summary name |
| `skills/vtex-io-core/components/product-summary-sku-selector.md` | 🟡 MEDIUM | product summary sku selector, product-summary-sku-selector | Official component documentation (scraped): product summary sku selector |
| `skills/vtex-io-core/components/recommendation-shelf.md` | 🟡 MEDIUM | recommendation shelf, recommendation-shelf | Official component documentation (scraped): recommendation shelf |
| `skills/vtex-io-core/components/reviews-and-ratings.md` | 🟡 MEDIUM | reviews and ratings, reviews-and-ratings | Official component documentation (scraped): reviews and ratings |
| `skills/vtex-io-core/components/rich-text.md` | 🟠 HIGH | rich text, rich-text | Official component documentation (scraped): rich text |
| `skills/vtex-io-core/components/search-result.md` | 🟠 HIGH | search result, search-result | Official component documentation (scraped): search result |
| `skills/vtex-io-core/components/search.md` | 🟠 HIGH | search, search | Official component documentation (scraped): search |
| `skills/vtex-io-core/components/seller-selector.md` | 🟡 MEDIUM | seller selector, seller-selector | Official component documentation (scraped): seller selector |
| `skills/vtex-io-core/components/shelf.md` | 🟠 HIGH | shelf, shelf | Official component documentation (scraped): shelf |
| `skills/vtex-io-core/components/stack-layout.md` | 🟡 MEDIUM | stack layout, stack-layout | Official component documentation (scraped): stack layout |
| `skills/vtex-io-core/components/store-form.md` | 🟡 MEDIUM | store form, store-form | Official component documentation (scraped): store form |
| `skills/vtex-io-core/components/store-image.md` | 🟡 MEDIUM | store image, store-image | Official component documentation (scraped): store image |
| `skills/vtex-io-core/components/store-link.md` | 🟠 HIGH | store link, store-link | Official component documentation (scraped): store link |
| `skills/vtex-io-core/components/store-locator.md` | 🟡 MEDIUM | store locator, store-locator | Official component documentation (scraped): store locator |
| `skills/vtex-io-core/components/store-newsletter.md` | 🟡 MEDIUM | store newsletter, store-newsletter | Official component documentation (scraped): store newsletter |
| `skills/vtex-io-core/components/tab-layout.md` | 🟡 MEDIUM | tab layout, tab-layout | Official component documentation (scraped): tab layout |
| `skills/vtex-io-core/components/video.md` | 🟡 MEDIUM | video, video | Official component documentation (scraped): video |
| `skills/vtex-io-core/components/vtex-io-sandbox-component.md` | 🟡 MEDIUM | vtex io sandbox component, vtex-io-sandbox-component | Official component documentation (scraped): vtex io sandbox component |
| `skills/vtex-io-core/components/vtex-product-kit.md` | 🟡 MEDIUM | vtex product kit, vtex-product-kit | Official component documentation (scraped): vtex product kit |
| `skills/vtex-io-core/components/vtex-product-specification-badges.md` | 🟡 MEDIUM | vtex product specification badges, vtex-product-specification-badges | Official component documentation (scraped): vtex product specification badges |
| `skills/vtex-io-core/components/vtex-sticky-layout.md` | 🟡 MEDIUM | vtex sticky layout, vtex-sticky-layout | Official component documentation (scraped): vtex sticky layout |
| **Styling** ||||
| `skills/vtex-io-core/styles/css-handles.md` | 🔴 **CRITICAL** | styling, css handles, css | Styling custom blocks |
| **Contexts** ||||
| `skills/vtex-io-core/contexts/product-context.md` | 🟠 HIGH | product data, PDP, product info, product context | Product information and SKU selection state |
| `skills/vtex-io-core/contexts/useOrderForm.md` | 🟠 HIGH | cart, orderform, checkout, add to cart | Cart management via OrderForm |
| `skills/vtex-io-core/contexts/useRuntime.md` | 🟡 MEDIUM | route, navigation, query params, runtime | Runtime route/navigation context |
| **GraphQL** ||||
| `skills/vtex-io-core/graphql/graphql.md` | 🟠 HIGH | graphql, apollo, react-apollo, useQuery, useMutation, gql, provider, search-graphql | Consume VTEX GraphQL APIs from React components |
| **Backend** ||||
| `skills/vtex-io-core/backend/services-api.md` | 🟡 **CRITICAL** | services, route handler, middleware, validation, API | Request handling |
| `skills/vtex-io-core/backend/clients.md` | 🔴 **CRITICAL** | API call, HTTP request, external API, fetch, clients | HTTP clients |
| `skills/vtex-io-core/backend/masterdata.md` | 🟠 HIGH | masterdata | Master Data integration |


---

## 🎯 LOADING PROTOCOL

```
1. Match keywords from task to "Triggers" column
2. Load by priority if multiple matches (🔴 → 🟠 → 🟡)
3. Load on-demand only - never preload all guides
4. Start by identifying domain (layout/components/contexts/backend)
```

### Loading Examples

```
Task: "Create a custom product badge component"
→ Triggers: "create", "custom", "component"
→ Loads: skills/vtex-io-core/components/custom-components.md (🔴 CRITICAL)

Task: "Build PDP with product info and add to cart button"
→ Triggers: "product info", "add to cart"
→ Loads: skills/vtex-io-core/contexts/product-context.md (🟠), skills/vtex-io-core/contexts/useOrderForm.md (🟠)

Task: "Create responsive grid layout for homepage"
→ Triggers: "responsive", "grid", "layout"
→ Loads: skills/vtex-io-core/components/flex-layout.md (🔴), skills/vtex-io-core/components/responsive-layout.md (🟡)

Task: "Fetch data from external API in backend"
→ Triggers: "API", "fetch", "backend"
→ Loads: skills/vtex-io-core/backend/clients.md (🔴 CRITICAL)

```

---

## 🧠 VTEX IO FUNDAMENTALS

### Core Concept

VTEX IO is a **declarative block composition system**, not traditional frontend.

```
You don't build pages.
You compose block trees.
```

### Architecture Layers

```
JSON Blocks      → Structure (what)
React Components → Behavior (how)
CSS Handles      → Style (appearance)
Node/GraphQL     → Data (backend)
```

---

## 🧱 BLOCK SYSTEM

### What is a Block?

Declarative UI unit defined in JSON representing visual or structural components.

### Block Declaration

```json
{
  "vendor.app.component#context": {
    "props": {
      "fullWidth": true
    },
    "children": [
      "flex-layout.col#left",
      "flex-layout.col#right"
    ]
  }
}
```

### Naming Convention

```
vendor.app.component#semantic-context
```

**Examples:**
- `store.home`
- `flex-layout.row#header`
- `product-summary.shelf#recommendations`

---

## 🏗️ FILE STRUCTURE

```
store-theme/
├── manifest.json              # App definition
├── store/
│   ├── blocks/               # Block declarations (.json)
│   │   ├── home.json
│   │   ├── product.json
│   │   └── search.json
│   └── interfaces.json       # Block → React component mapping
└── react/                    # Custom React components
    └── components/
```

---

## 📦 MANIFEST.JSON

Defines the VTEX IO app.

```json
{
  "vendor": "company",
  "name": "store-theme",
  "version": "1.0.0",
  "builders": {
    "store": "0.x",
    "react": "3.x"
  },
  "dependencies": {
    "vtex.store": "2.x",
    "vtex.flex-layout": "0.x",
    "vtex.store-components": "3.x"
  }
}
```

**Key sections:**
- `vendor` + `name` = app identifier
- `builders` = what this app can build
- `dependencies` = installed VTEX apps

---

## 🧩 COMPONENT TYPES

### Native Components

Provided by official VTEX apps:
- `vtex.store-components` (generic UI)
- `vtex.flex-layout` (layout system)
- `vtex.product-summary` (product displays)
- `vtex.search-result` (search pages)
- `vtex.menu` (navigation)

### Custom Components

**Flow:**
1. Create React component in `/react`
2. Register in `interfaces.json`
3. Declare in `manifest.json`
4. Use declaratively in JSON blocks

**Guide:** `skills/vtex-io-core/components/custom-components.md`

---

## 🔗 COMPOSITION PATTERNS

### `children` (Direct Composition)

Renders blocks in sequence, like React children.

```json
{
  "flex-layout.row#main": {
    "children": [
      "flex-layout.col#left",
      "flex-layout.col#right"
    ]
  }
}
```

**Mental model:** Fixed structure tree

---

### `blocks` (Extension Points)

Dynamic injection via `<ExtensionPoint />`.

```json
{
  "store.home": {
    "blocks": [
      "telemarketing-slot"
    ]
  }
}
```

**Requires in React:**
```tsx
<ExtensionPoint id="telemarketing-slot" />
```

**Mental model:** Plugin slots

---

## 🚦 ARCHITECTURAL RULES

### Hierarchy (MANDATORY)

```
1. Prefer native VTEX blocks
2. Create custom React blocks only when necessary
3. Never access APIs directly from components
4. Always declare informative titles for blocks with custom props on site-editor
5. Create folder structure for complex json components, do not create a single json file with all the components

```

### Separation of Concerns (MANDATORY)

```
✓ JSON blocks = structure
✓ React = behavior
✓ CSS Handles = styling (cross-app)
✓ Hooks = data/state
✓ Clients = backend integration

✗ Never mix layout with business logic
✗ Never mix frontend with direct API calls
✗ Never style CSS handles in same app that defines them
✗ Never create "god components"
```

---

## 🚀 QUICK DECISION TREE

**What are you trying to do?**

```
📐 Building page layout / structure
  → Load: skills/vtex-io-core/components/flex-layout.md (🔴)

🧩 Creating a new custom block
  → Load: skills/vtex-io-core/components/custom-components.md (🔴)

📦 Using native VTEX components
  → Load: skills/vtex-io-core/components/{component}.md (🟠/🟡)

📊 Need product/cart data in component
  → Load: skills/vtex-io-core/contexts/product-context.md or skills/vtex-io-core/contexts/useOrderForm.md (🟠)

🔌 Calling external APIs
  → Load: skills/vtex-io-core/backend/clients.md (🔴)

📱 Making layout responsive
  → Load: skills/vtex-io-core/components/responsive-layout.md (🟡)

🎨 Styling components
  → Reference: CSS Handles (cross-app styling)
```

---

## 🎯 DOMAIN CLASSIFICATION

Use this to identify which domain your task belongs to:

| Task involves... | Domain | Guide Priority |
|-----------------|--------|----------------|
| Grid, rows, columns, page structure | **Layout** | Start with flex-layout.md (🔴) |
| Creating new custom blocks with React | **Components** | Start with custom-components.md (🔴) |
| Using/customizing native VTEX blocks | **Components** | Load specific component guide (🟠/🟡) |
| Accessing product/cart/runtime data | **Contexts** | Load specific context guide (🟠/🟡) |
| API calls, external services | **Backend** | Start with clients.md (🔴) |
| Route handlers, validation | **Backend** | Start with services-api.md (🟡) |

**Quick Domain Identification:**
- Keywords: "layout", "grid", "row", "structure" → **Layout**
- Keywords: "component", "block", "create", "custom" → **Components**
- Keywords: "data", "fetch", "product", "cart", "orderform" → **Contexts**
- Keywords: "API", "backend", "GraphQL", "client" → **Backend**

---

## 📋 COMMON DEPENDENCIES

```json
{
  "dependencies": {
    "vtex.store": "2.x",              // Core store blocks
    "vtex.flex-layout": "0.x",        // Layout system
    "vtex.store-components": "3.x",   // Generic UI components
    "vtex.product-summary": "2.x",    // Product cards/displays
    "vtex.search-result": "3.x",      // Search & category pages
    "vtex.menu": "2.x",               // Navigation menus
    "vtex.minicart": "2.x"            // Shopping cart
  }
}
```

---

## 🧬 RELATED SKILLS

- **frontend-design** → UX/UI patterns
- **software-architecture** → SOLID principles
- **api-design** → GraphQL/REST patterns

---

## 📚 VALIDATION SOURCES

Official VTEX docs (for validation only, NOT primary source):
- https://developers.vtex.com/docs/guides/store-framework
- https://developers.vtex.com/docs/apps/

---

## ⚡ QUICK START WORKFLOW

```
User asks VTEX IO task
↓
Use Quick Decision Tree or Domain Classification
↓
Match keywords to Guide Index triggers
↓
Load guide(s) by priority (🔴 → 🟠 → 🟡)
↓
Apply patterns from guide
↓
Validate if needed
```

**Real Examples:**

```
Task: "Create homepage banner component"
→ Domain: Components (custom block creation)
→ Trigger match: "create", "component"
→ Load: skills/vtex-io-core/components/custom-components.md (🔴)

Task: "Build product listing with filters"
→ Domain: Components (native blocks + composition)
→ Trigger match: "product", "listing", "filter"
→ Load: skills/vtex-io-core/components/flex-layout.md (🔴), skills/vtex-io-core/components/product-summary.md (🟠)

Task: "Fetch order history from API"
→ Domain: Backend
→ Trigger match: "fetch", "API"
→ Load: skills/vtex-io-core/backend/clients.md (🔴)
```

---

## ✅ VTEX IO CHECKLIST

**Before deploying to production:**

### Critical (Must Fix):
- [ ] No waterfalls in data fetching (parallel fetch where possible)
- [ ] Custom components exported as default
- [ ] CSS Handles defined for all custom components
- [ ] No direct API calls from React components
- [ ] All blocks have semantic identifiers (`#context`)

### High Priority:
- [ ] interfaces.json properly maps all custom blocks
- [ ] Schema added for Site Editor support (when needed)
- [ ] Data fetched via hooks (not direct API calls)
- [ ] No inline styles (use CSS handles)

### Medium Priority:
- [ ] No anonymous blocks
- [ ] TypeScript interfaces defined for props
- [ ] Backend clients properly configured
- [ ] GraphQL queries optimized (no N+1)

### Styling Rules:
- [ ] CSS Handles styled from different app (cross-app styling)
- [ ] No styling via props
- [ ] Semantic CSS handle names

---

## 🔴 CRITICAL REMINDERS

1. **Load guides on-demand** — never preload everything
2. **VTEX IO is declarative** — compose blocks, don't build pages
3. **Separation is mandatory** — structure/behavior/style/data are isolated
4. **Native first** — prefer VTEX blocks over custom code
5. **Cross-app styling** — CSS handles work across apps, not within same app
6. **Semantic identifiers** — all blocks must have `#context`

---
