# OrderForm Context Guide

> **Hook:** `useOrderForm()`  
> **Purpose:** Read and update cart/orderForm data in Store Framework components  
> **Package:** `vtex.order-manager`  
> **⚠️ Warning:** This package contains experimental code. Use at your own risk.

---

## Core Concept

In VTEX Store Framework, cart state is represented by the **OrderForm**. The `useOrderForm()` hook exposes the current orderForm and a setter to keep the local state in sync after mutations.

The OrderForm is managed by `OrderFormProvider`, which must be wrapped by `OrderQueueProvider`. The queue centralizes all requests to the Checkout API, ensuring they run sequentially and avoiding race conditions.

---

## Provider Setup

`useOrderForm()` must be used inside `OrderFormProvider`, which in turn must be inside `OrderQueueProvider`:

```tsx
import {
  OrderQueueProvider,
  useOrderQueue,
  useQueueStatus,
} from 'vtex.order-manager/OrderQueue'
import { OrderFormProvider, useOrderForm } from 'vtex.order-manager/OrderForm'

const MainComponent: FunctionComponent = () => (
  <OrderQueueProvider>
    <OrderFormProvider>
      <MyComponent />
    </OrderFormProvider>
  </OrderQueueProvider>
)
```

> **Note:** Most VTEX native blocks (minicart.v2, add-to-cart-button) already provide these providers. You only need to add them manually in custom root components.

---

## `useOrderForm()` — Return Type

```tsx
interface OrderFormContext {
  orderForm: OrderForm       // Current cart data. Do NOT mutate directly.
  setOrderForm: (nextValue: Partial<OrderForm>) => void  // Update local state after mutations
  loading: boolean           // true only during initial orderForm load
  error: ApolloError | undefined  // Apollo error if the orderForm query fails
}
```

### `orderForm` — Full Type

```tsx
interface OrderForm {
  // Identity
  orderFormId: string
  salesChannel: string
  loggedIn: boolean
  canEditData: boolean
  userProfileId: string | null
  userType: string | null

  // Cart contents
  items: Item[]

  // Financial summary — values in CENTS (e.g. 10990 = R$109,90)
  totalizers: Totalizer[]
  value: number

  // Customer and delivery
  clientProfileData: ClientProfileData | null
  shippingData: ShippingData | null
  paymentData: PaymentData

  // Other sections
  marketingData: MarketingData | null
  clientPreferencesData: ClientPreferencesData
  storePreferencesData: StorePreferencesData
  giftRegistryData: GiftRegistryData | null
  ratesAndBenefitsData: RatesAndBenefitsData
  sellers: Seller[]
  messages: Message[]
  openTextField: OpenTextField | null
  customData: CustomData | null
}
```

### Key Nested Types

```tsx
interface Item {
  id: string               // SKU ID
  name: string
  skuName: string
  productId: string
  refId: string
  quantity: number
  price: number            // in cents
  listPrice: number        // in cents
  sellingPrice: number     // in cents
  isGift: boolean
  seller: string
  imageUrl: string
  detailUrl: string
  measurementUnit: string
  unitMultiplier: number
  attachments: Attachment[]
  priceTags: PriceTag[]
  offerings: Offering[]
}

interface Totalizer {
  id: string     // e.g. "Items", "Shipping", "Discounts"
  name: string
  value: number  // in cents
}

interface ClientProfileData {
  email: string
  firstName: string
  lastName: string
  document: string
  documentType: string
  phone: string
  isCorporate: boolean
  corporateName: string | null
  tradeName: string | null
  corporateDocument: string | null
}

interface ShippingData {
  address: Address | null
  availableAddresses: Address[]
  logisticsInfo: LogisticsInfo[]  // one per item — contains SLA options
}

interface Address {
  addressId: string
  addressType: string   // "residential" | "commercial" | "pickup"
  receiverName: string
  postalCode: string
  city: string
  state: string
  country: string       // ISO 3-letter code e.g. "BRA"
  street: string
  number: string
  neighborhood: string
  complement: string | null
}
```

---

## Basic Usage

```tsx
import { useOrderForm } from 'vtex.order-manager/OrderForm'

const CartSummary = () => {
  const { orderForm, loading } = useOrderForm()

  if (loading) return <div>Loading cart...</div>

  const items = orderForm?.items ?? []
  const totalizers = orderForm?.totalizers ?? []
  const total = orderForm?.value ?? 0

  return (
    <div>
      <div>Items: {items.length}</div>
      <div>Total: {(total / 100).toFixed(2)}</div>
      {totalizers.map(t => (
        <div key={t.id}>{t.name}: {(t.value / 100).toFixed(2)}</div>
      ))}
    </div>
  )
}
```

---

## Using `setOrderForm` After Mutations

`setOrderForm` is **not** for direct mutations — it syncs local state after a successful Checkout API call:

```tsx
import { useOrderForm } from 'vtex.order-manager/OrderForm'
import { useOrderQueue } from 'vtex.order-manager/OrderQueue'

const CouponInput = () => {
  const { orderForm, setOrderForm } = useOrderForm()
  const { enqueue } = useOrderQueue()

  const applyCoupon = (couponCode: string) => {
    enqueue(
      async () => {
        const response = await fetch('/api/checkout/pub/orderForm/coupons', {
          method: 'POST',
          body: JSON.stringify({ text: couponCode }),
        })
        const updatedOrderForm = await response.json()
        return updatedOrderForm
      },
      'coupon'  // id deduplicates rapid submissions — only last runs
    ).then((updatedOrderForm) => {
      setOrderForm(updatedOrderForm)  // sync local state
    })
  }

  return <button onClick={() => applyCoupon('PROMO10')}>Apply Coupon</button>
}
```

> **Rule:** Always call `setOrderForm(updatedOrderForm)` after a mutation resolves. This keeps all other `useOrderForm()` consumers in sync without a page reload.

---

## Using with `vtex.order-items`

For adding/removing/updating items, use `vtex.order-items` instead of calling the API directly:

```tsx
import { OrderFormProvider, useOrderForm } from 'vtex.order-manager/OrderForm'
import { OrderItemsProvider, useOrderItems } from 'vtex.order-items/OrderItems'

// Providers setup
const MainComponent: FunctionComponent = () => (
  <OrderFormProvider>
    <OrderItemsProvider>
      <CartComponent />
    </OrderItemsProvider>
  </OrderFormProvider>
)

// Component
const CartComponent = () => {
  const { orderForm: { items } } = useOrderForm()
  const { updateQuantity, removeItem } = useOrderItems()

  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>
          {item.name} x{item.quantity}
          <button onClick={() => updateQuantity({ id: item.id, quantity: item.quantity + 1 })}>
            +
          </button>
          <button onClick={() => removeItem({ id: item.id })}>
            Remove
          </button>
        </li>
      ))}
    </ul>
  )
}
```

---

## `loading` vs Queue Status

These are two different concepts — don't confuse them:

| | `loading` | `queueStatusRef.current` |
|---|---|---|
| **What it means** | OrderForm is being fetched on initial render | There are pending tasks in the queue |
| **Use case** | Show skeleton/loading on page load | Disable checkout button while cart is updating |
| **How to get** | `const { loading } = useOrderForm()` | `const { listen } = useOrderQueue()` + `useQueueStatus(listen)` |

```tsx
import { useOrderQueue, useQueueStatus, QueueStatus } from 'vtex.order-manager/OrderQueue'

const CheckoutButton = () => {
  const { loading } = useOrderForm()
  const { listen } = useOrderQueue()
  const queueStatusRef = useQueueStatus(listen)

  // loading: page just mounted and fetching orderForm
  // queueStatusRef: ongoing mutations (add item, coupon, etc.)
  const isDisabled = loading || queueStatusRef.current === QueueStatus.PENDING

  return <button disabled={isDisabled}>Checkout</button>
}
```

> **Note:** `queueStatusRef` is a ref — mutating it does **not** trigger re-render. To reactively disable a button, use queue events with `useState`.

---

## Handling `error`

If the orderForm query fails, an empty orderForm is returned and `error` is populated:

```tsx
const { orderForm, error } = useOrderForm()

if (error) {
  console.error('OrderForm failed to load:', error.message)
  return <div>Could not load cart. Please refresh.</div>
}
```

---

## `manifest.json` Dependency

```json
{
  "dependencies": {
    "vtex.order-manager": "0.x"
  }
}
```

---

## ⚠️ Practical Rules

```
✓ Always guard orderForm fields — they can be null/undefined before loading
✓ Values are in CENTS — divide by 100 for display
✓ Use setOrderForm only after a successful mutation — never for optimistic updates
✓ Use vtex.order-items for add/remove/update item operations
✓ Use enqueue() with an id to deduplicate rapid user actions (e.g. coupon typing)
✗ Never modify orderForm directly — always use setOrderForm
✗ Never use loading to detect ongoing mutations — use useQueueStatus instead
✗ Do not depend on queueStatusRef for re-renders — use state + listen events
```

---

## Common Hooks by Use Case

```tsx
// Read cart state
import { useOrderForm } from 'vtex.order-manager/OrderForm'

// Enqueue mutations + listen to queue status
import { useOrderQueue, useQueueStatus, QueueStatus } from 'vtex.order-manager/OrderQueue'

// Add/remove/update items (preferred over direct API calls)
import { useOrderItems } from 'vtex.order-items/OrderItems'

// Read payment data
import { useOrderPayment } from 'vtex.order-payment/OrderPayment'

// Read/update shipping
import { useOrderShipping } from 'vtex.order-shipping/OrderShipping'
```