# Responsive Layout Guide

> **Blocks:** `responsive-layout.desktop` / `responsive-layout.mobile` / `responsive-layout.phone` / `responsive-layout.tablet`
> **Purpose:** Render different layouts per breakpoint
> **Team rule:** **Do NOT use** `responsive-layout.tablet` (see mandatory rule below)

---

## 🎯 WHAT IS RESPONSIVE LAYOUT?

Responsive Layout lets you **render different block trees for different breakpoints**. It is a conditional layout wrapper: only the matching breakpoint renders its children.

---

## 🧱 AVAILABLE BLOCKS

| Block | Purpose | Use in our projects |
|-------|---------|---------------------|
| `responsive-layout.desktop` | Content for desktop breakpoint | ✅ Yes |
| `responsive-layout.mobile` | Content for **phone + tablet** in our standard | ✅ Yes |
| `responsive-layout.phone` | Phone-only breakpoint | ⚠️ Only if absolutely necessary |
| `responsive-layout.tablet` | Tablet-only breakpoint | ❌ **Never use** |

---

## 🚫 MANDATORY RULE: NO `responsive-layout.tablet`

We **do not use** `responsive-layout.tablet`. Use **only** `responsive-layout.mobile` for **both phone and tablet**.

**Why?** To avoid multiple client configurations. Even if the same `rich-text` is used on desktop and mobile, the Site Editor requires editing both blocks separately. Keeping only `desktop` + `mobile` reduces duplication and maintenance risk.

**Allowed pattern:**
- `responsive-layout.desktop` for desktop
- `responsive-layout.mobile` for **phone + tablet**

---

## ✅ BASIC SETUP

### 1) Add dependency

```json
{
  "dependencies": {
    "vtex.responsive-layout": "0.x"
  }
}
```

### 2) Basic structure (recommended)

```json
{
  "store.custom#about": {
    "blocks": [
      "responsive-layout.desktop#about",
      "responsive-layout.mobile#about"
    ]
  },

  "responsive-layout.desktop#about": {
    "children": ["rich-text#about-desktop"]
  },

  "responsive-layout.mobile#about": {
    "children": ["rich-text#about-mobile"]
  }
}
```

---

## 📋 COMMON PATTERNS

### Pattern 1: Same content, different layout

```json
{
  "store.home": {
    "blocks": [
      "responsive-layout.desktop#home",
      "responsive-layout.mobile#home"
    ]
  },

  "responsive-layout.desktop#home": {
    "children": [
      "flex-layout.row#home-desktop"
    ]
  },

  "responsive-layout.mobile#home": {
    "children": [
      "flex-layout.row#home-mobile"
    ]
  }
}
```

### Pattern 2: Mobile uses a simplified block tree

```json
{
  "store.custom#promo": {
    "blocks": [
      "responsive-layout.desktop#promo",
      "responsive-layout.mobile#promo"
    ]
  },

  "responsive-layout.desktop#promo": {
    "children": [
      "slider-layout#promo-banners"
    ]
  },

  "responsive-layout.mobile#promo": {
    "children": [
      "image#promo-banner"
    ]
  }
}
```

---

## ✅ DO / ❌ DON'T

**Do**
- Use `desktop` + `mobile` as the default structure
- Keep mobile layout minimal to reduce Site Editor maintenance
- Prefer `flex-layout` and `slider-layout` inside each breakpoint

**Don't**
- Use `responsive-layout.tablet`
- Create extra breakpoint trees unless there is a clear UX requirement

---

## 🔍 QUICK CHECKLIST

- Dependency added: `vtex.responsive-layout`
- Only `desktop` + `mobile` used
- `tablet` is not declared anywhere
- Mobile tree is intentionally simplified

