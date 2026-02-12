# Flex Layout Guide

> **Blocks:** `flex-layout.row` / `flex-layout.col`  
> **Purpose:** Flexbox-based structural layout system  
> **Rule:** Structure only — never business logic

---

## 🧱 BLOCK TYPES

### `flex-layout.row`
- Horizontal container (`flex-direction: row`)
- Must be the root of any flex layout
- Contains `flex-layout.col` children

### `flex-layout.col`
- Vertical container (`flex-direction: column`)
- Must be inside `flex-layout.row`
- Can contain another `flex-layout.row`

---

## 🏗️ STRUCTURE RULES (MANDATORY)

```
1. Always start with row
2. Only col goes inside row
3. Only row goes inside col
4. Always alternate: row → col → row → col
5. Never break alternation
```

### Valid Pattern

```json
{
  "flex-layout.row#main": {
    "children": [
      "flex-layout.col#left",
      "flex-layout.col#right"
    ]
  },
  
  "flex-layout.col#left": {
    "children": [
      "flex-layout.row#nested"
    ]
  }
}
```

---

## 📐 COLUMN WIDTH CONTROL

### Default Behavior
```
colSizing: "equal" (default)
→ All columns same width
→ width prop on col is IGNORED
```

### Custom Width
```json
{
  "flex-layout.row#main": {
    "props": {
      "colSizing": "auto"    // Required to enable width control
    },
    "children": [
      "flex-layout.col#left",
      "flex-layout.col#right"
    ]
  },
  
  "flex-layout.col#left": {
    "props": {
      "width": "30%"         // Now width works
    }
  },
  
  "flex-layout.col#right": {
    "props": {
      "width": "70%"
    }
  }
}
```

**Critical:** `colSizing: "auto"` on row enables `width` on cols.

---

## ⚙️ ESSENTIAL PROPS

### On `flex-layout.row`

| Prop | Default | Recommended | Why |
|------|---------|-------------|-----|
| `colSizing` | `"equal"` | `"auto"` | Enable column width control |
| `preserveLayoutOnMobile` | `false` | `true` | Keep structure on mobile (don't stack) |
| `fullWidth` | `false` | `true` | Remove unwanted container padding |

### Standard Configuration

```json
{
  "flex-layout.row#main": {
    "props": {
      "colSizing": "auto",
      "preserveLayoutOnMobile": true,
      "fullWidth": true
    }
  }
}
```

**Apply these by default unless you have a specific reason not to.**

---

## 📱 MOBILE BEHAVIOR

### Default VTEX Behavior
```
Mobile → row converts to column (stacks vertically)
```

### Prevent Stacking
```json
{
  "props": {
    "preserveLayoutOnMobile": true
  }
}
```

**Rule:** Layout structure should not change between devices — only spacing/sizing should adapt.

---

## 🎯 NAMING & IDENTIFICATION

### Always use semantic identifiers

```json
// ✅ Good
"flex-layout.row#product-main"
"flex-layout.col#image-area"
"flex-layout.col#info-area"

// ❌ Bad
"flex-layout.row"
"flex-layout.col"
```

**Never use anonymous blocks.**

---

## 🎨 STYLING

### ❌ Don't Style via Props

```json
// Wrong
{
  "props": {
    "marginTop": 5,
    "paddingLeft": 10,
    "colGap": 3
  }
}
```

### ✅ Style via CSS

```css
/* In your CSS file or another app */
.vtex-flex-layout-0-x-flexRow--product-main {
  margin-top: 2rem;
  gap: 1rem;
}
```

**Rule:** Props = structure. CSS = appearance.

---

## 🧬 DOM STRUCTURE (How it Renders)

`flex-layout.row` generates:

```html
<div class="vtex-flex-layout-0-x-flexRow flexRow--product-main">
  <div class="vtex-store-components-3-x-container">
    <div class="flexRowContent">
      <div class="flexRowContent--product-main stretchChildrenWidth items-stretch">
        <!-- Your col content here -->
      </div>
    </div>
  </div>
</div>
```

**Key insight:** `items-stretch` is the actual layout cell wrapper around each col.

---

## 🧩 CSS HANDLES

Available handles:
```
flexRow
flexRowContent
flexCol
flexColChild
```

**Usage:**
```css
.vtex-flex-layout-0-x-flexRow--product-main { }
.vtex-flex-layout-0-x-flexCol--image-area { }
```

---

## 🚫 ANTI-PATTERNS

```
❌ Breaking row/col alternation
❌ Anonymous layout blocks
❌ Styling via props
❌ Deep nesting without purpose
❌ Mixing layout with business logic
❌ Using colSizing: "equal" or not specifying it when you don't want equal columns
❌ Not using preserveLayoutOnMobile
```

---

## 📋 QUICK REFERENCE

### Minimal Working Example

```json
{
  "flex-layout.row#main": {
    "props": {
      "colSizing": "auto",
      "preserveLayoutOnMobile": true,
      "fullWidth": true
    },
    "children": [
      "flex-layout.col#left",
      "flex-layout.col#right"
    ]
  },
  
  "flex-layout.col#left": {
    "props": {
      "width": "40%"
    },
    "children": ["image-block"]
  },
  
  "flex-layout.col#right": {
    "props": {
      "width": "60%"
    },
    "children": ["content-block"]
  }
}
```

---

## 📚 OFFICIAL DOCS

- https://developers.vtex.com/docs/apps/vtex-flex-layout

---