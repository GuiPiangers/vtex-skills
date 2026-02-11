# Flex Layout Guide (VTEX IO)

> **Component:** `flex-layout.row` / `flex-layout.col`
> **Domain:** Layout System
> **Purpose:** Structural layout composition using flexbox semantics in VTEX IO
> **Nature:** Architectural block (never business logic)

---

# 🧱 Core Blocks

## `flex-layout.row`

* Horizontal container (flex-direction: row)
* Top-level layout unit
* Always the **root element** in a flex layout

## `flex-layout.col`

* Vertical container (flex-direction: column)
* Child unit
* Used only inside rows

---

# ⚠️ Structural Rules (MANDATORY)

```txt
1. A layout ALWAYS starts with a row
2. You can only place col inside row
3. You can only place row inside col
4. Structure must alternate: row → col → row → col
5. Never use flex-layout as a first-level block
6. Never break alternation
```

---

# 🧬 Rendering Model (REAL DOM STRUCTURE)

`flex-layout.row` always renders:

```
.vtex-flex-layout-0-x-flexRow
└── .vtex-store-components-3-x-container
    └── .flexRowContent
        └── .items-stretch   (one for each child col)
```

### Key Insight

> `items-stretch` is the **true layout cell**.

You are not controlling the col directly — you are controlling the **container generated for it**.

---

# 📐 Column Width Control (CRITICAL RULE)

### Default Behavior

```txt
colSizing = equal (default)
→ All columns have the same width
→ width on flex-layout.col is ignored
```

### Controlled Width Behavior

```json
"flex-layout.row": {
  "props": {
    "colSizing": "auto"
  }
}
```

Then:

```json
"flex-layout.col#left": {
  "props": {
    "width": "30%"
  }
}

"flex-layout.col#right": {
  "props": {
    "width": "70%"
  }
}
```

### Rule

> ❗ To control column width:
>
> * `colSizing: auto` on `flex-layout.row`
> * define `width` on `flex-layout.col` only if it's needed for the component, otherwise don't use this prop to keep de default value ("width": "auto")

---

# ✅ Default Architecture Rules

Always apply unless there is a **clear reason not to**:

```txt
✔ colSizing: auto
✔ preserveLayoutOnMobile: true
✔ fullWidth: true
```

### Why

| Prop                   | Reason                            |
| ---------------------- | --------------------------------- |
| colSizing: auto        | Enables real layout control       |
| preserveLayoutOnMobile | Prevents mobile column collapse   |
| fullWidth              | Avoids unwanted container padding |

---

# 📱 Mobile Behavior

### Default VTEX Behavior

```txt
Mobile → row breaks into column
```

### Correct Behavior

```json
"preserveLayoutOnMobile": true
```

### Rule

> Layout architecture must not change between devices.
> Only spacing and flow should adapt — not structure.

---

# 🎯 Identification & Targeting

### Rule

> Always explicitly identify blocks.

```json
"flex-layout.row#product-main": {}
"flex-layout.col#image-area": {}
"flex-layout.col#info-area": {}
```

Never use anonymous layout blocks.

---

# 🎨 Styling Strategy

## ❌ Forbidden

```txt
- Styling via props
- Layout tuning via padding/margin props
- Visual spacing via colGap/rowGap
```

## ✅ Correct

```txt
- Styling via CSS
- Layout spacing via CSS
- Visual control via CSS
```

### Rule

> Props define structure.
> CSS defines appearance.

---

# 🧱 Composition Pattern

### Standard Pattern

```
row
└── col
    └── row
        └── col
```

Example:

```json
"flex-layout.row#pdp-main": {
  "props": {
    "colSizing": "auto",
    "preserveLayoutOnMobile": true,
    "fullWidth": true
  },
  "children": [
    "flex-layout.col#left",
    "flex-layout.col#right"
  ]
}
```

---

# 🚫 Anti-Patterns

```txt
✘ Deep nesting without purpose
✘ Visual layout via props
✘ colSizing: equal by default
✘ Anonymous rows/cols
✘ Mobile layout breaking
✘ Using flex-layout as design tool
✘ Layout mixed with business logic
✘ God-layout structures
```

# 🧩 CSS Handles

```txt
flexRow
flexRowContent
flexCol
flexColChild
```

---

# 📚 Official References

* [https://developers.vtex.com/docs/apps/vtex-flex-layout](https://developers.vtex.com/docs/apps/vtex-flex-layout)
* [https://developers.vtex.com/docs/guides/store-framework](https://developers.vtex.com/docs/guides/store-framework)

---

# 🧠 Operational Rules Summary

```txt
1. Always start with row
2. Always alternate row/col
3. Always use colSizing: auto
4. Always use preserveLayoutOnMobile: true
5. Always use fullWidth: true
6. Always identify blocks
7. Always style via CSS
```

---
