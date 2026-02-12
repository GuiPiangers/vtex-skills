---
description: Create VTEX IO apps, Store Framework blocks, or integrations.
---

# /create - VTEX Create

$ARGUMENTS

---

## Purpose

Start a **VTEX-only** creation flow. No non-VTEX stacks.

---

## Behavior

1. **Scope**
   - What is being created? (block composition, custom component, backend service)
   - Target account/workspace
   - Existing app to extend or new app

2. **Choose VTEX path**
   - Prefer Store Framework blocks when possible
   - Use custom VTEX IO app only when needed

3. **Define builders & dependencies**
   - `store` / `react` / `node` / `messages` as required
   - Document required VTEX apps

4. **Plan output**
   - Files/blocks to add
   - Changes needed in `manifest.json` and `store/blocks`

---

## Examples

```
/create new banner block for home
/create custom product badge component
/create masterdata integration for lead capture
```
