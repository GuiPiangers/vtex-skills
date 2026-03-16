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

**Critical:** If the CSS filename does not match `{vendor}.{app-name}.css`, VTEX won’t associate your rules with that app’s CSS Handles and the styles won’t be applied.

---

## 🎨 CSS HANDLES SYNTAX

### Basic Handle (recommended)

```css
.{handle} {
  /* styles */
}
```

### Real Example (`styles/css/vtex.flex-layout.css`)

```css
/* VTEX adds the vendor/app/version prefix during build/link */
.flexRow {
  display: flex;
  gap: 1rem;
}

.flexCol {
  padding: 1rem;
}
```

**Important:** The handle-only selectors (`.flexRow`, `.flexCol`, etc.) must live in the matching file (`vtex.flex-layout.css`). The CSS filename is what scopes the handles to a specific app.

### How Handles Work

1. Component declares handle: `useCssHandles(['container'])`
2. DOM renders as: `<div class="vtex-myapp-1-x-container">`
3. In `styles/css/{vendor}.{app}.css`, you style it as: `.container { }` (do **not** write the `vtex-myapp-1-x-` prefix)

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
.flexRow {
  /* Applies to ALL flex rows */
}

/* With blockClass modifier */
.flexRow--main-header {
  /* Applies ONLY to rows with blockClass="main-header" */
  background: #000;
  padding: 2rem;
}
```

**Pattern:** `{handle}--{blockClass}`

---

## 📋 COMMON CSS HANDLES BY COMPONENT

### flex-layout
File: `styles/css/**/vtex.flex-layout.css`

```css
.flexRow { }
.flexRowContent { }
.flexCol { }
.flexColChild { }
```

### store-components
File: `styles/css/**/vtex.store-components.css`

```css
.container { }
.productBrand { }
.productName { }
.productPrice { }
```

### product-summary
File: `styles/css/**/vtex.product-summary.css`

```css
.container { }
.element { }
.image { }
.nameContainer { }
```

### menu
File: `styles/css/**/vtex.menu.css`

```css
.container { }
.menuItem { }
.menuContainer { }
```

**Note:** Check each app's documentation or component source code for complete handle list.

---

## 🚫 CSS SELECTOR RESTRICTIONS

Customization using CSS selectors is mostly deprecated.

The following selectors are the only ones allowed for store customization:

```css
/* ✅ Class selectors */
.foo { }

/* ✅ Pseudo-classes */
.foo:hover { }
.foo:visited { }
.foo:active { }
.foo:disabled { }
.foo:focus { }
:local(.foo) { }
.foo:empty { }
.foo:target { }

/* ✅ :not() */
.foo:not(.bar) { }

/* ✅ First/last child */
.foo:first-child { }
.foo:last-child { }

/* ✅ nth-child */
.foo:nth-child(even) { }
.foo:nth-child(odd) { }
.foo:nth-child(2n) { }
.foo:nth-child(4n) { }

/* ✅ Pseudo-elements */
.foo::before { }
.foo::after { }
.foo::placeholder { }

/* ✅ Space combinator (descendant) */
.foo .bar { }

/* ✅ data-* attributes */
[data-testid] { }
[data-my-attr="value"] { }

/* ✅ Cross-app targeting (elements from other apps) */
:global(.vtex-{AppName}-{AppVersion}-x-{handle}) { }

/* ✅ Media queries */
@media (max-width: 768px) {
  .foo { }
}
@media (prefers-reduced-motion: reduce) {
  .foo { transition: none; }
}
```

CSS selectors that are not included in this list aren't supported. Using them can cause issues like app linking failure.

```css
/* ❌ Tag selectors / IDs / universal selector */
div { }
#header { }
* { }

/* ❌ Child combinator */
.foo > .bar { }

/* ❌ Attribute selectors outside [data-*] */
[alt="bar"] { }

/* ❌ Unsupported nth-child variants */
.foo:nth-child(2) { }

/* ❌ Other unsupported combinators/selectors */
.foo + .bar { }
.foo ~ .bar { }
```

**Rule:** Prefer styling via CSS Handles + `blockClass`, inside the correct `styles/css/{vendor}.{app}.css` file.

---

## ⚠️ IMPORTANT USAGE

### Avoid !important

```css
/* ❌ Bad */
.flexRow {
  padding: 2rem !important;
}

/* ✅ Good - Use specificity instead */
.flexRow--header {
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
.flexRow { }

/* Medium specificity - with blockClass */
.flexRow--header { }

/* High specificity - descendant */
.flexRow--header .flexCol { }

/* Higher specificity - pseudo-class */
.flexRow--header:not(.flexRow--mobile) { }
```

---

## 📐 RESPONSIVE DESIGN

### Mobile-First Approach

```css
/* Base (mobile) */
.flexRow {
  flex-direction: column;
  gap: 1rem;
}

/* Tablet */
@media screen and (min-width: 768px) {
  .flexRow {
    flex-direction: row;
    gap: 2rem;
  }
}

/* Desktop */
@media screen and (min-width: 1024px) {
  .flexRow {
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
.flexRow--product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  padding: 2rem;
}

@media screen and (max-width: 768px) {
  .flexRow--product-grid {
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
.flexRow--main-header {
  background: linear-gradient(to right, #000, #333);
  padding: 1.5rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.flexRow--main-header .flexCol {
  align-items: center;
}
```

---

### Example 3: Product Card Hover Effect

**CSS (styles/css/pdp/vtex.product-summary.css):**
```css
.container {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 8px;
  overflow: hidden;
}

.container:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

.image {
  transition: transform 0.3s ease;
}

.container:hover .image {
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
.banner--hero {
  position: relative;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: url('/assets/hero-bg.jpg') center/cover;
}

.title--hero {
  font-size: 3rem;
  font-weight: bold;
  color: white;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.cta--hero {
  padding: 1rem 2rem;
  background: #ff0000;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.cta--hero:hover {
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
✓ Keep selectors based on CSS Handles (and allowed selectors only)
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
❌ Attribute selectors outside [data-*]
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
/* In styles/css/{vendor}.{app}.css */
.{handle} { }
.{handle}--{blockClass} { }

/* If you must target elements from a different app */
:global(.vtex-{AppName}-{AppVersion}-x-{handle}) { }
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
