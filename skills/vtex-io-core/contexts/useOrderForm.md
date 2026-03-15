# OrderForm Context Guide

> **Hook:** `useOrderForm()`  
> **Purpose:** Read and update cart/orderForm data in Store Framework components  
> **Package:** `vtex.order-manager`

---

## Core Concept

In VTEX Store Framework, cart state is represented by the **OrderForm**. The `useOrderForm()` hook exposes:

- The current orderForm (items, totals, client profile, shipping, payment data)
- Helpers to trigger orderForm updates (depending on the app APIs you use)

When you need to:

- Render minicart / cart summaries
- Read item list / totals
- React to cart changes

Prefer reading from `useOrderForm()` instead of storing cart state yourself.

---

## Basic Usage

```tsx
import { useOrderForm } from 'vtex.order-manager/OrderForm'

export const CartSummary = () => {
  const { orderForm } = useOrderForm()

  const items = orderForm?.items ?? []
  const totalizers = orderForm?.totalizers ?? []

  return (
    <div>
      <div>Items: {items.length}</div>
      <pre>{JSON.stringify(totalizers, null, 2)}</pre>
    </div>
  )
}
```

---

## Practical Notes

- `orderForm` can be `undefined` while loading; guard render paths.
- Avoid expensive derived computations on every render; compute only what you need.
- For mutations (add/remove items, attachments, shipping), use the official Store Framework/Checkout APIs in your app context; keep the UI in sync via `orderForm`.
