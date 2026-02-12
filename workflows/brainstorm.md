---
description: VTEX-focused discovery and option exploration before implementation.
---

# /brainstorm - VTEX Discovery

$ARGUMENTS

---

## Purpose

Structured exploration of VTEX solutions **only**. Use before committing to a VTEX IO/Store Framework approach.

---

## Behavior

When `/brainstorm` is triggered:

1. **Clarify VTEX scope**
   - Account and workspace
   - Store Framework vs custom VTEX IO app
   - Pages/blocks involved
   - Integration needs (Master Data, OMS, Checkout)

2. **Generate VTEX-only options**
   - At least 2-3 approaches using VTEX blocks and VTEX IO apps
   - Note tradeoffs in Site Editor maintenance and performance

3. **Recommend a VTEX path**
   - Prefer block composition over custom code
   - Prefer minimal breakpoints in responsive layout

---

## Output Format

```markdown
## VTEX Brainstorm: [Topic]

### Context
[Brief VTEX scope]

---

### Option A: [VTEX Approach]
[Description]

Pros:
- [benefit]

Cons:
- [tradeoff]

---

### Option B: [VTEX Approach]
[Description]

Pros:
- [benefit]

Cons:
- [tradeoff]

---

## Recommendation
[Chosen VTEX-first approach + reasoning]
```

---

## Examples

```
/brainstorm homepage hero with banners
/brainstorm custom product shelf behavior
/brainstorm checkout customization
```
