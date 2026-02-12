---
description: VTEX-only routing note. Multi-agent orchestration is disabled.
---

# /orchestrate - VTEX Only

$ARGUMENTS

---

## Purpose

This repository uses a **single VTEX specialist agent**. Multi-agent orchestration is intentionally disabled to avoid non-VTEX context.

---

## Behavior

- Do **not** invoke non-VTEX agents
- Keep solutions inside VTEX IO / Store Framework
- If request is non-VTEX, ask to re-scope

---

## Example

```
/orchestrate checkout issue
```
