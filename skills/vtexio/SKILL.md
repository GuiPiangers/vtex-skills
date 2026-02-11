---
name: vtex-io-core
description: Central VTEX IO knowledge system. Defines architectural standards, block behaviors, frontend patterns, React custom components, hooks, and VTEX backend (clients, middlewares, routes). This is not documentation — it's operational intelligence.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# VTEX IO CORE SKILL SYSTEM

> **Philosophy:** VTEX IO is not about blocks — it's about architecture, behavior, and consistency.  
> **Core Principle:** Standardize thinking, not just implementation.

---

# 🎯 Selective Reading Rule (MANDATORY)

**Load only the guides required for the current task. Never load everything.**

---

## 🧱 Layout System (Store Framework)

| Guide | Status | When to Read |
|------|--------|--------------|
| [layout/flex-layout.md](guides/layout/flex-layout.md) | 🔴 REQUIRED | Any grid/row/col layout |
| [layout/slider-layout.md](guides/layout/slider-layout.md) | 🔴 REQUIRED | Carousels / sliders |
| [layout/store-blocks.md](guides/layout/store-blocks.md) | 🔴 REQUIRED | store-block usage |
| [layout/container-patterns.md](guides/layout/container-patterns.md) | ⚪ Optional | Structural patterns |
| [layout/responsive-system.md](guides/layout/responsive-system.md) | ⚪ Optional | Breakpoints/responsiveness |

---

## 🧩 Store Components (Granular Blocks)

| Block | Guide | Docs |
|------|------|------|
| Product Price | guides/store-components/product-price.md | vtex.store-components |
| SKU Selector | guides/store-components/sku-selector.md | vtex.store-components |
| Buy Button | guides/store-components/buy-button.md | vtex.store-components |
| Product Name | guides/store-components/product-name.md | vtex.store-components |
| Product Image | guides/store-components/product-image.md | vtex.store-components |
| Breadcrumb | guides/store-components/breadcrumb.md | vtex.store-components |
| Minicart | guides/store-components/minicart.md | vtex.minicart |
| Search Result | guides/store-components/search-result.md | vtex.search-result |
| Filters | guides/store-components/filters.md | vtex.search-result |

**Docs base:**
- https://developers.vtex.com/docs/apps/vtex.store-components  
- https://developers.vtex.com/docs/apps/vtex.search-result  
- https://developers.vtex.com/docs/apps/vtex.minicart  

---

## 🛒 Shelf / Vitrine System

| Guide | Status | Scope |
|------|--------|-------|
| [shelf/product-summary.md](guides/shelf/product-summary.md) | 🔴 REQUIRED | Base summary |
| [shelf/product-summary-shelf.md](guides/shelf/product-summary-shelf.md) | 🔴 REQUIRED | Shelf rendering |
| [shelf/product-summary-list.md](guides/shelf/product-summary-list.md) | ⚪ Optional | List view |
| [shelf/shelf-composition.md](guides/shelf/shelf-composition.md) | 🔴 REQUIRED | Vitrine architecture |
| [shelf/shelf-patterns.md](guides/shelf/shelf-patterns.md) | ⚪ Optional | UX patterns |

**Docs:**
- https://developers.vtex.com/docs/apps/vtex.product-summary  
- https://developers.vtex.com/docs/apps/vtex.shelf  

---

## 🧾 PDP System

| Guide | Status | Scope |
|------|--------|-------|
| [pdp/pdp-architecture.md](guides/pdp/pdp-architecture.md) | 🔴 REQUIRED | PDP structure |
| [pdp/sku-logic.md](guides/pdp/sku-logic.md) | 🔴 REQUIRED | SKU handling |
| [pdp/seller-logic.md](guides/pdp/seller-logic.md) | 🔴 REQUIRED | Seller rules |
| [pdp/availability.md](guides/pdp/availability.md) | ⚪ Optional | Stock rules |
| [pdp/pricing-logic.md](guides/pdp/pricing-logic.md) | 🔴 REQUIRED | Price logic |
| [pdp/pdp-layout.md](guides/pdp/pdp-layout.md) | 🔴 REQUIRED | Layout composition |

**Docs:**
- https://developers.vtex.com/docs/guides/product-detail-page  
- https://developers.vtex.com/docs/apps/vtex.product-context  

---

# ⚛️ React Custom System

| Guide | Status | Scope |
|------|--------|-------|
| [react/custom-components.md](guides/react/custom-components.md) | 🔴 REQUIRED | Custom blocks |
| [react/render-runtime.md](guides/react/render-runtime.md) | 🔴 REQUIRED | VTEX runtime |
| [react/css-handles.md](guides/react/css-handles.md) | 🔴 REQUIRED | Styling system |
| [react/blockclass-strategy.md](guides/react/blockclass-strategy.md) | 🔴 REQUIRED | blockClass |
| [react/props-mapping.md](guides/react/props-mapping.md) | 🔴 REQUIRED | JSON schema mapping |
| [react/composition.md](guides/react/composition.md) | ⚪ Optional | Advanced composition |

**Docs:**
- https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-custom-apps  
- https://developers.vtex.com/docs/guides/render-runtime  

---

# 🪝 Hooks System

| Hook | Guide | Docs |
|------|------|------|
| useProduct | guides/hooks/useProduct.md | vtex.product-context |
| useOrderForm | guides/hooks/useOrderForm.md | vtex.order-manager |
| useRuntime | guides/hooks/useRuntime.md | vtex.render-runtime |
| useCssHandles | guides/hooks/useCssHandles.md | vtex.css-handles |
| Custom Hooks | guides/hooks/custom-hooks.md | internal patterns |

---

# 🧠 Backend VTEX IO System

## Architecture
- [backend/architecture.md](guides/backend/architecture.md)
- [backend/service-json.md](guides/backend/service-json.md)
- [backend/context.md](guides/backend/context.md)

## HTTP Layer
- [backend/routes.md](guides/backend/routes.md)
- [backend/middlewares.md](guides/backend/middlewares.md)
- [backend/error-handling.md](guides/backend/error-handling.md)

## Clients
- [backend/clients.md](guides/backend/clients.md)
- [backend/auth.md](guides/backend/auth.md)
- [backend/retries.md](guides/backend/retries.md)
- [backend/timeouts.md](guides/backend/timeouts.md)

## Observability
- [backend/logging.md](guides/backend/logging.md)
- [backend/metrics.md](guides/backend/metrics.md)
- [backend/tracing.md](guides/backend/tracing.md)

**Docs:**
- https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-backend-apps  
- https://developers.vtex.com/docs/guides/vtex-io-documentation-routing  
- https://developers.vtex.com/docs/guides/vtex-io-documentation-using-clients  

---

# 🔗 Integration System

| Guide | Scope |
|------|-------|
| [integration/external-apis.md](guides/integration/external-apis.md) | APIs externas |
| [integration/webhooks.md](guides/integration/webhooks.md) | Webhooks |
| [integration/auth.md](guides/integration/auth.md) | Auth flows |
| [integration/retries.md](guides/integration/retries.md) | Resilience |
| [integration/fallback.md](guides/integration/fallback.md) | Failover |
| [integration/error-strategy.md](guides/integration/error-strategy.md) | Error handling |

---

# 🚦 Decision Rules

1. **Prefer native blocks**
2. **Extend with custom React only when necessary**
3. **Encapsulate logic in hooks**
4. **Encapsulate I/O in clients**
5. **Never mix layout with business logic**
6. **Never mix frontend logic with backend integration**
7. **Never access APIs directly from components**
8. **Never centralize multiple responsibilities in one block**
9. **Never create “god components”**
10. **Always isolate domain responsibility**

---

# 🧠 Behavior Over Documentation Rule

> Documentation tells *what VTEX allows*.  
> This system defines *how your architecture must behave*.

---

# 🧬 Related Skills

| Skill | Purpose |
|------|--------|
| **vtex-io-core** | VTEX IO architecture |
| **frontend-design** | UX/UI thinking |
| **web-design-guidelines** | Accessibility & performance |
| **software-architecture** | SOLID & Clean Architecture |
| **api-design** | API design patterns |

---

## 🧠 Operational Rule

If task = VTEX:
→ Load vtex-io-core
→ Load only the micro-guides needed
→ Apply patterns
→ Follow internal rules
→ Use VTEX docs only as validation
