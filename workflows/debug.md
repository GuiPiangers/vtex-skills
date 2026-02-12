---
description: Debug VTEX Store Framework or VTEX IO apps.
---

# /debug - VTEX Debug

$ARGUMENTS

---

## Purpose

Systematic debugging for VTEX-only issues.

---

## Behavior

1. **Reproduce in workspace**
   - Confirm account/workspace
   - Validate with `vtex link` if needed

2. **Check VTEX-specific signals**
   - Admin > Apps > Logs
   - Render/runtime errors
   - OrderForm/Checkout events

3. **Isolate scope**
   - Blocks vs custom React
   - Master Data/OMS/Checkout integration

4. **Propose fix**
   - Minimal change first
   - Verify in workspace

---

## Examples

```
/debug shelf not rendering on mobile
/debug checkout customization not applied
/debug masterdata form not saving
```
