---
description: Publish VTEX IO apps safely.
---

# /deploy - VTEX Deploy

$ARGUMENTS

---

## Purpose

Guide VTEX publish/release flow with validation.

---

## Behavior

1. **Prechecks**
   - `manifest.json` builders/deps
   - Workspace validated with `vtex link`
   - Critical flows tested (PDP, cart, checkout)

2. **Publish**
   - `vtex publish`
   - Note version and changelog

3. **Release (if applicable)**
   - `vtex release`
   - Rollback plan defined

---

## Examples

```
/deploy app v1.2.0
/deploy hotfix for checkout issue
```
