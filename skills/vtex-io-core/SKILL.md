---
name: vtex-io-core
description: Central VTEX IO knowledge system. Defines architectural standards, block behaviors, frontend patterns, React custom components, hooks, and VTEX backend (clients, middlewares, routes). This is not documentation — it's operational intelligence.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
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
   - guides/layout/flex-layout.md (🔴 CRITICAL)
   - guides/components/product-summary.md (🟠 HIGH)
4. Apply patterns from loaded guides
```

---

## 📂 GUIDE INDEX

| Guide | Priority | Triggers | Purpose |
|-------|----------|----------|---------|
| **Layout** ||||
| `guides/layout/flex-layout.md` | 🔴 **CRITICAL** | grid, row, col, layout, structure, flexbox | Flexbox layout system |
| `guides/layout/responsive-layout.md` | 🟡 MEDIUM | mobile, responsive, breakpoint, device | Responsive patterns |
| **Components** ||||
| `guides/components/custom-components.md` | 🔴 **CRITICAL** | create block, custom component, new block, React | Build custom blocks |
| `guides/components/product-summary.md` | 🟠 HIGH | product card, shelf, product list, showcase | Product displays |
| **Styling** ||||
| `guides/styles/css-handles.md` | 🔴 **CRITICAL** | Styling, CSS Handles, CSS | Styling custom blocks |
| **Contexts** ||||
| `guides/contexts/product-context.md` | 🟠 HIGH | product data, PDP, product info, product context | Product information or manipulate product infos and SKUs |
| `guides/contexts/useOrderForm.md` | 🟠 HIGH | cart, order, checkout, add to cart | Cart management |
| `guides/contexts/useRuntime.md` | 🟡 MEDIUM | route, navigation, query params, runtime | Runtime context |
| **Backend** ||||
| `guides/backend/services-api.md` | 🟡 **CRITICAL** | services, route handler, middleware, validation, API | Request handling |
| `guides/backend/clients.md` | 🔴 **CRITICAL** | API call, HTTP request, external API, fetch, clients | HTTP clients |
| `guides/backend/masterdata.md` | 🟠 HIGH | masterdata | Masterdata integration |


---

## 🎯 LOADING PROTOCOL

```
1. Match keywords from task to "Triggers" column
2. Load by priority if multiple matches (🔴 → 🟠 → 🟡)
3. Load on-demand only - never preload all guides
4. Start by identifying domain (layout/components/hooks/backend)
```

### Loading Examples

```
Task: "Create a custom product badge component"
→ Triggers: "create", "custom", "component"
→ Loads: guides/components/custom-components.md (🔴 CRITICAL)

Task: "Build PDP with product info and add to cart button"
→ Triggers: "product info", "add to cart"
→ Loads: guides/hooks/useProduct.md (🟠), guides/hooks/useOrderForm.md (🟠)

Task: "Create responsive grid layout for homepage"
→ Triggers: "responsive", "grid", "layout"
→ Loads: guides/layout/flex-layout.md (🔴), guides/layout/responsive-layout.md (🟡)

Task: "Fetch data from external API in backend"
→ Triggers: "API", "fetch", "backend"
→ Loads: guides/backend/clients.md (🔴 CRITICAL)

Task: "Add custom navigation menu"
→ Triggers: "navigation", "menu"
→ Loads: guides/components/menu.md (🟡)
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

**Guide:** `guides/components/custom-components.md`

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
  → Load: guides/layout/flex-layout.md (🔴)

🧩 Creating a new custom block
  → Load: guides/components/custom-components.md (🔴)

📦 Using native VTEX components
  → Load: guides/components/{component}.md (🟠/🟡)

📊 Need product/cart data in component
  → Load: guides/hooks/useProduct.md or useOrderForm.md (🟠)

🔌 Calling external APIs
  → Load: guides/backend/clients.md (🔴)

🔍 Building GraphQL integration
  → Load: guides/backend/graphql.md (🟠)

📱 Making layout responsive
  → Load: guides/layout/responsive-layout.md (🟡)

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
| Accessing product/cart/runtime data | **Hooks** | Load specific hook guide (🟠/🟡) |
| Creating custom hooks | **Hooks** | Load custom-hooks.md (🟡) |
| API calls, external services | **Backend** | Start with clients.md (🔴) |
| GraphQL queries/mutations | **Backend** | Load graphql.md (🟠) |
| Route handlers, validation | **Backend** | Load middlewares.md (🟡) |

**Quick Domain Identification:**
- Keywords: "layout", "grid", "row", "structure" → **Layout**
- Keywords: "component", "block", "create", "custom" → **Components**
- Keywords: "data", "fetch", "product", "cart", "hook" → **Hooks**
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
→ Load: guides/components/custom-components.md (🔴)

Task: "Build product listing with filters"
→ Domain: Components
→ Trigger match: "product", "listing", "filter"
→ Load: guides/components/search-result.md (🟠)

Task: "Fetch order history from API"
→ Domain: Backend
→ Trigger match: "fetch", "API"
→ Load: guides/backend/clients.md (🔴)
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