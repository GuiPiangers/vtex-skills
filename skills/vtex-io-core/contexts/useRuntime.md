# Runtime Context Guide

> **Hook:** `useRuntime()`  
> **Purpose:** Access route, query params, navigation helpers, and account/workspace context  
> **Package:** `vtex.render-runtime`

---

## Core Concept

`useRuntime()` provides access to runtime information about the current page:

- Route and query parameters
- Device hints and rendering context
- Navigation helpers (push/replace when available)

Use it when you need to:

- Read URL params (for conditional rendering)
- Navigate programmatically
- Identify current page/route context

---

## Basic Usage

```tsx
import { useRuntime } from 'vtex.render-runtime'

export const DebugRuntime = () => {
  const runtime = useRuntime()

  return (
    <pre style={{ whiteSpace: 'pre-wrap' }}>
      {JSON.stringify({ route: runtime?.route, query: runtime?.query }, null, 2)}
    </pre>
  )
}
```

---

## Practical Notes

- Treat runtime data as environment context, not as business state.
- Prefer declarative navigation via blocks/links when possible; use runtime navigation when necessary.
