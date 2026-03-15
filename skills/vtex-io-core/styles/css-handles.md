# CSS Handles Guide

> **Purpose:** Style VTEX IO components using CSS Handles cross-app styling system  
> **Rule:** CSS Handles enable styling components from different apps (separation of concerns)

---

## 🎯 CORE CONCEPT

**CSS Handles are NOT traditional CSS classes.**

They are a **cross-app styling system** where:
- App A defines the component structure + CSS Handles
- App B (store-theme) applies the actual styling

```
Component App  → Defines handles
Store Theme    → Styles handles
```

**Critical:** You cannot style CSS Handles in the same app that defines them.

---

## 📂 FILE STRUCTURE

### Location
All CSS files must be inside `/styles/css/`

### Organization
Use folders to separate by component domain:

```
styles/css/
├── header/
│   ├── vtex.menu.css
│   └── vtex.store-header.css
├── footer/
│   └── vtex.store-footer.css
├── pdp/
│   ├── vtex.product-summary.css
│   └── vtex.store-components.css
├── home/
│   └── vtex.flex-layout.css
└── global/
    └── vtex.store-components.css
```

---

## 📝 FILE NAMING CONVENTION

### Pattern
```
{vendor}.{app-name}.css
```

### Examples

**Native VTEX apps:**
```
vtex.flex-layout.css
vtex.store-components.css
vtex.product-summary.css
vtex.menu.css
vtex.search-result.css
```

**Custom apps:**
```
mycompany.custom-banner.css
acme.product-badge.css
mystore.telemarketing.css
```

**Rule:** Always use the exact vendor and app name from the app's `manifest.json`.

---

## 🎨 CSS HANDLES SYNTAX

### Basic Handle

```css
.{vendor}-{app}-{major-version}-x-{handle} {
  /* styles */
}
```

### Real Example

```css
/* Styling flex-layout handles */
.vtex-flex-layout-0-x-flexRow {
  display: flex;
  gap: 1rem;
}

.vtex-flex-layout-0-x-flexCol {
  padding: 1rem;
}
```

### How Handles Work

1. Component declares handle: `useCssHandles(['container'])`
2. DOM renders as: `<div class="vtex-myapp-1-x-container">`
3. You style it: `.vtex-myapp-1-x-container { }`

---

## 🏷️ BLOCK CLASS CUSTOMIZATION

### What is blockClass?

A **custom identifier** added to blocks for specific styling.

### Declaration in JSON

```json
{
  "flex-layout.row#header": {
    "props": {
      "blockClass": "main-header"
    }
  }
}
```

### Styling blockClass

```css
/* Base handle */
.vtex-flex-layout-0-x-flexRow {
  /* Applies to ALL flex rows */
}

/* With blockClass modifier */
.vtex-flex-layout-0-x-flexRow--main-header {
  /* Applies ONLY to rows with blockClass="main-header" */
  background: #000;
  padding: 2rem;
}
```

**Pattern:** `{handle}--{blockClass}`

---

## 📋 COMMON CSS HANDLES BY COMPONENT

### flex-layout

```css
.vtex-flex-layout-0-x-flexRow { }
.vtex-flex-layout-0-x-flexRowContent { }
.vtex-flex-layout-0-x-flexCol { }
.vtex-flex-layout-0-x-flexColChild { }
```

### store-components

```css
.vtex-store-components-3-x-container { }
.vtex-store-components-3-x-productBrand { }
.vtex-store-components-3-x-productName { }
.vtex-store-components-3-x-productPrice { }
```

### product-summary

```css
.vtex-product-summary-2-x-container { }
.vtex-product-summary-2-x-element { }
.vtex-product-summary-2-x-image { }
.vtex-product-summary-2-x-nameContainer { }
```

### menu

```css
.vtex-menu-2-x-container { }
.vtex-menu-2-x-menuItem { }
.vtex-menu-2-x-menuContainer { }
```

**Note:** Check each app's documentation or component source code for complete handle list.

---

## 🚫 CSS SELECTOR RESTRICTIONS

### Allowed Selectors

```css
/* ✅ Class selectors */
.vtex-flex-layout-0-x-flexRow { }

/* ✅ Pseudo-classes */
.vtex-menu-2-x-menuItem:hover { }
.vtex-store-components-3-x-container:first-child { }

/* ✅ Pseudo-elements */
.vtex-product-summary-2-x-nameContainer::before { }

/* ✅ Descendant combinators */
.vtex-flex-layout-0-x-flexRow .vtex-product-summary-2-x-container { }

/* ✅ Child combinators */
.vtex-flex-layout-0-x-flexRow > .vtex-flex-layout-0-x-flexCol { }

/* ✅ Attribute selectors (on CSS Handles only) */
.vtex-menu-2-x-menuItem[class*="--active"] { }
```

### Forbidden Selectors

```css
/* ❌ Tag selectors */
div { }
span { }
a { }

/* ❌ ID selectors */
#header { }

/* ❌ Universal selector */
* { }

/* ❌ Direct tag + class */
div.vtex-flex-layout-0-x-flexRow { }

/* ❌ Attribute selectors on non-CSS-Handle classes */
[data-attribute="value"] { }
```

**Rule:** Only use class selectors based on CSS Handles. No direct tag or ID styling.

---

## ⚠️ IMPORTANT USAGE

### Avoid !important

```css
/* ❌ Bad */
.vtex-flex-layout-0-x-flexRow {
  padding: 2rem !important;
}

/* ✅ Good - Use specificity instead */
.vtex-flex-layout-0-x-flexRow--header {
  padding: 2rem;
}
```

**Why avoid:**
- Makes debugging difficult
- Breaks cascade hierarchy
- Hard to override later

**When to use:** Only as last resort for overriding third-party styles.

---

## 🎯 SPECIFICITY STRATEGY

### Increase Specificity Without !important

```css
/* Low specificity */
.vtex-flex-layout-0-x-flexRow { }

/* Medium specificity - with blockClass */
.vtex-flex-layout-0-x-flexRow--header { }

/* High specificity - parent + blockClass */
.vtex-store-components-3-x-container .vtex-flex-layout-0-x-flexRow--header { }

/* Higher specificity - pseudo-class */
.vtex-flex-layout-0-x-flexRow--header:not(.vtex-flex-layout-0-x-flexRow--mobile) { }
```

---

## 📐 RESPONSIVE DESIGN

### Mobile-First Approach

```css
/* Base (mobile) */
.vtex-flex-layout-0-x-flexRow {
  flex-direction: column;
  gap: 1rem;
}

/* Tablet */
@media screen and (min-width: 768px) {
  .vtex-flex-layout-0-x-flexRow {
    flex-direction: row;
    gap: 2rem;
  }
}

/* Desktop */
@media screen and (min-width: 1024px) {
  .vtex-flex-layout-0-x-flexRow {
    gap: 3rem;
  }
}
```

### Common Breakpoints

```css
/* Mobile: default */
/* Tablet: 768px */
/* Desktop: 1024px */
/* Large Desktop: 1440px */
```

---

## 🧩 PRACTICAL EXAMPLES

### Example 1: Styling Product Grid

**JSON (blocks/home.json):**
```json
{
  "flex-layout.row#products": {
    "props": {
      "blockClass": "product-grid"
    },
    "children": ["product-summary.shelf"]
  }
}
```

**CSS (styles/css/home/vtex.flex-layout.css):**
```css
.vtex-flex-layout-0-x-flexRow--product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  padding: 2rem;
}

@media screen and (max-width: 768px) {
  .vtex-flex-layout-0-x-flexRow--product-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
}
```

---

### Example 2: Custom Header Styling

**JSON (blocks/header.json):**
```json
{
  "flex-layout.row#header": {
    "props": {
      "blockClass": "main-header"
    }
  }
}
```

**CSS (styles/css/header/vtex.flex-layout.css):**
```css
.vtex-flex-layout-0-x-flexRow--main-header {
  background: linear-gradient(to right, #000, #333);
  padding: 1.5rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.vtex-flex-layout-0-x-flexRow--main-header .vtex-flex-layout-0-x-flexCol {
  align-items: center;
}
```

---

### Example 3: Product Card Hover Effect

**CSS (styles/css/pdp/vtex.product-summary.css):**
```css
.vtex-product-summary-2-x-container {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 8px;
  overflow: hidden;
}

.vtex-product-summary-2-x-container:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

.vtex-product-summary-2-x-image {
  transition: transform 0.3s ease;
}

.vtex-product-summary-2-x-container:hover .vtex-product-summary-2-x-image {
  transform: scale(1.05);
}
```

---

### Example 4: Custom Component Styling

**Component declares handles:**
```tsx
const CSS_HANDLES = ['banner', 'title', 'subtitle', 'cta'] as const
const handles = useCssHandles(CSS_HANDLES)
```

**JSON with blockClass:**
```json
{
  "mystore.custom-banner#hero": {
    "props": {
      "blockClass": "hero"
    }
  }
}
```

**CSS (styles/css/home/mystore.custom-banner.css):**
```css
.mystore-custom-banner-1-x-banner--hero {
  position: relative;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: url('/assets/hero-bg.jpg') center/cover;
}

.mystore-custom-banner-1-x-title--hero {
  font-size: 3rem;
  font-weight: bold;
  color: white;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.mystore-custom-banner-1-x-cta--hero {
  padding: 1rem 2rem;
  background: #ff0000;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.mystore-custom-banner-1-x-cta--hero:hover {
  background: #cc0000;
}
```

---

## 🔍 FINDING CSS HANDLES

### Method 1: Browser DevTools

1. Inspect element in browser
2. Look for classes matching pattern: `vtex-{app}-{version}-x-{handle}`
3. Note the handle name (after `-x-`)

### Method 2: Component Source Code

Check the component's React code:
```tsx
const CSS_HANDLES = ['container', 'title', 'image']
```

### Method 3: Official Documentation

- VTEX Developers: https://developers.vtex.com/docs/apps/
- Each app lists available CSS Handles

---

## 🚦 BEST PRACTICES

```
✓ Organize CSS files by domain (header, footer, pdp, etc.)
✓ Use blockClass for specific customizations
✓ Follow naming convention: {vendor}.{app}.css
✓ Avoid !important (use specificity instead)
✓ Use mobile-first responsive approach
✓ Keep selectors based on CSS Handles only
✓ Use semantic blockClass names
✓ Document complex selectors with comments
```

---

## 🚫 ANTI-PATTERNS

```
❌ Styling in same app that defines handles
❌ Using tag selectors (div, span, a)
❌ Using ID selectors (#header)
❌ Excessive !important usage
❌ Direct attribute selectors on non-handles
❌ Universal selector (*)
❌ Inline styles in JSON blocks
❌ CSS files outside /styles/css/
❌ Wrong file naming (not matching vendor.app pattern)
```

---

## 📋 COMPLETE WORKFLOW

### 1. Identify Component
```
Which component needs styling?
→ Check app name in manifest.json or block declaration
```

### 2. Create CSS File
```
Path: styles/css/{domain}/{vendor}.{app}.css
Example: styles/css/header/vtex.flex-layout.css
```

### 3. Find CSS Handles
```
→ Inspect element in browser
→ Check component documentation
→ Look for pattern: vtex-{app}-{version}-x-{handle}
```

### 4. Add blockClass (if needed)
```json
{
  "component-name": {
    "props": {
      "blockClass": "custom-identifier"
    }
  }
}
```

### 5. Write CSS
```css
.{vendor}-{app}-{version}-x-{handle} { }
.{vendor}-{app}-{version}-x-{handle}--{blockClass} { }
```

### 6. Test
```
→ Check in browser
→ Verify specificity
→ Test responsive breakpoints
```

---

## 🔗 RELATED CONCEPTS

- **Custom Components** → Define your own CSS Handles
- **flex-layout** → Most common layout handles
- **blockClass** → Enable specific targeting
- **Responsive Design** → Mobile-first approach

---

## 📚 OFFICIAL REFERENCES

- https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization

---