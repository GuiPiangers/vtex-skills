# VTEX IO Backend — Clients Guide

> Operational guide for creating and using Clients in VTEX IO Node services

---

## 🎯 WHEN TO USE THIS GUIDE

Load this guide when the task involves:
- Calling VTEX APIs (Catalog, OMS, MasterData, Checkout, Logistics…)
- Integrating with external APIs (third-party services)
- Creating custom HTTP clients
- Using VBase for file/blob storage
- Using MasterData for CRUD operations

**Related guides:**
- `skills/vtex-io-core/backend/services-api.md` → for route/middleware setup

---

## 🧠 CONCEPT: WHAT IS A CLIENT?

A Client is the **only correct way** to make API calls inside VTEX IO. Never use raw `fetch` or `axios` directly from a middleware.

```
Middleware → ctx.clients.myClient.method() → Client → External/Internal API
```

**Why Clients over direct calls:**
- Built-in caching, retries, timeout
- Native metrics and billing tracking
- Centralized auth token handling
- Properly typed responses
- Managed by IOContext (account, workspace, etc.)

---

## 🗂️ CLIENT TYPES (from `@vtex/api`)

Choose the base class based on what you're connecting to:

| Base Class | Package | Use When |
|------------|---------|----------|
| `AppClient` | `@vtex/api` | Calling another VTEX IO app's private routes |
| `AppGraphQLClient` | `@vtex/api` | Calling another VTEX IO app's GraphQL API |
| `ExternalClient` | `@vtex/api` | Calling any external API outside VTEX |
| `JanusClient` | `@vtex/api` | Calling VTEX Core Commerce APIs via Janus Gateway |
| `InfraClient` | `@vtex/api` | Calling VTEX IO infrastructure services |

> **Rule of thumb:**
> - External API (GitHub, Stripe, ERP…) → `ExternalClient`
> - VTEX REST API (api.vtex.com, {account}.myvtex.com/api/…) → `JanusClient`
> - Another IO App → `AppClient` or `AppGraphQLClient`

---

## 📦 NATIVE CLIENTS — `@vtex/api`

Available directly from `@vtex/api` via `IOClients`. No extra install needed.

```typescript
import { IOClients } from '@vtex/api'
```

| Client | Access via `ctx.clients.` | Key Methods |
|--------|--------------------------|-------------|
| `masterdata` | `masterdata` | `getDocument`, `createDocument`, `updatePartialDocument`, `searchDocuments`, `scrollDocuments`, `deleteDocument`, `createOrUpdateSchema` |
| `id` | `id` | `getTemporaryToken`, `sendCodeToEmail`, `getEmailCodeAuthenticationToken`, `getPasswordAuthenticationToken` |
| `licenseManager` | `licenseManager` | `getAccountData`, `getTopbarData`, `canAccessResource` |
| `messagesGraphQL` | `messagesGraphQL` | `translateV2`, `translate`, `saveV2`, `userTranslations` |
| `catalogGraphQL` | `catalogGraphQL` | `sku`, `category`, `brand`, `product` |
| `paymentProvider` | `paymentProvider` | `callback`, `inbound` |

These are inherited automatically when your `Clients` class extends `IOClients` — no getter needed unless you want a named alias.

---

## 📦 NATIVE CLIENTS — `@vtex/clients`

Install in the `node/` folder:

```bash
yarn add @vtex/clients
```

### Available Clients

| Client | Import | Key Methods | Required Policy |
|--------|--------|-------------|-----------------|
| `Affiliate` | `import { Affiliate } from '@vtex/clients'` | `registerAffiliate`, `changeNotification`, `createSeller`, `getSellerList` | — |
| `Catalog` | `import { Catalog } from '@vtex/clients'` | `getProductsAndSkus`, `getSkuById`, `getSellerById`, `getSkuContext`, `getCategoryById`, `getBrandById` | — |
| `Checkout` | `import { Checkout } from '@vtex/clients'` | `getOrderFormConfiguration`, `setOrderFormConfiguration`, `setSingleCustomData` | — |
| `Logistics` | `import { Logistics } from '@vtex/clients'` | `getDockById`, `pickupById`, `listPickupPoints`, `nearPickupPoints`, `shipping`, `listInventoryBySku` | — |
| `OMS` | `import { OMS } from '@vtex/clients'` | `listOrders`, `userLastOrder`, `order`, `orderNotification`, `cancelOrder` | `OMSViewer` |
| `OmsApiProxy` | `import { OmsApiProxy } from '@vtex/clients'` | `orders`, `orderFormId`, `customData`, `register` | `OMSViewer` |
| `RatesAndBenefits` | `import { RatesAndBenefits } from '@vtex/clients'` | `getAllBenefits`, `getPromotionById`, `createOrUpdatePromotion`, `createMultipleSkuPromotion`, `updateMultipleSkuPromotion` | `ADMIN_TOKEN` (default) |
| `Suggestions` | `import { Suggestions } from '@vtex/clients'` | `getAllSuggestions`, `getSuggestionById`, `getAllVersions`, `getVersionById`, `sendSkuSuggestion`, `deleteSkuSuggestion` | — |

> Note: method availability can vary by `@vtex/clients` version. Prefer TypeScript types/IntelliSense as the source of truth and keep these lists as quick reminders.

### Available Factories

Factories create typed clients for specific data entities.

| Factory | Import | Key Methods |
|---------|--------|-------------|
| `masterDataFor` | `import { masterDataFor } from '@vtex/clients'` | `get`, `save`, `update`, `saveOrUpdate`, `saveOrUpdatePartial`, `delete`, `search`, `searchRaw`, `scroll` |
| `vbaseFor` | `import { vbaseFor } from '@vtex/clients'` | `get`, `getRaw`, `getWithMetadata`, `save`, `trySaveIfhashMatches` |

---

## 🔧 WIRING CLIENTS — `node/clients/index.ts`

All clients must be registered in the `Clients` class:

```typescript
import { IOClients } from '@vtex/api'
import { OMS, Catalog, Logistics } from '@vtex/clients'

import { MyExternalClient } from './myExternalClient'
import { MyJanusClient } from './myJanusClient'

export class Clients extends IOClients {
  // @vtex/clients
  public get oms() {
    return this.getOrSet('oms', OMS)
  }

  public get catalog() {
    return this.getOrSet('catalog', Catalog)
  }

  public get logistics() {
    return this.getOrSet('logistics', Logistics)
  }

  // Custom clients
  public get myExternalClient() {
    return this.getOrSet('myExternalClient', MyExternalClient)
  }

  public get myJanusClient() {
    return this.getOrSet('myJanusClient', MyJanusClient)
  }
}
```

> `getOrSet` ensures only one instance is created per request context (singleton per request).

---

## 🏗️ CUSTOM CLIENTS

### Pattern 1 — ExternalClient (external APIs)

Use for any API outside VTEX (Stripe, GitHub, ERP, custom services).

```typescript
import type { IOContext, InstanceOptions } from '@vtex/api'
import { ExternalClient } from '@vtex/api'

interface MyApiResponse {
  id: string
  name: string
}

export class MyExternalClient extends ExternalClient {
  // Private route map — keeps URLs organized
  private routes = {
    item:   (id: string) => `/items/${id}`,
    list:   () => '/items',
    create: () => '/items',
  }

  constructor(context: IOContext, options?: InstanceOptions) {
    super('https://api.myservice.com', context, {
      ...options,
      retries: 2,
      headers: {
        'x-vtex-use-https': 'true',
        'x-api-key': 'MY_KEY', // prefer env vars or app settings
        ...options?.headers,
      },
    })
  }

  public getItem(id: string) {
    return this.http.get<MyApiResponse>(this.routes.item(id), {
      metric: 'my-external-get-item',
    })
  }

  public listItems() {
    return this.http.get<MyApiResponse[]>(this.routes.list(), {
      metric: 'my-external-list-items',
    })
  }

  public createItem(data: Omit<MyApiResponse, 'id'>) {
    return this.http.post<MyApiResponse>(this.routes.create(), data, {
      metric: 'my-external-create-item',
    })
  }
}
```

**manifest.json policy required:**
```json
{
  "name": "outbound-access",
  "attrs": {
    "host": "api.myservice.com",
    "path": "/*"
  }
}
```

---

### Pattern 2 — JanusClient (VTEX Core APIs)

Use for VTEX REST APIs accessed via the Janus gateway (e.g., `/api/oms`, `/api/dataentities`).

```typescript
import type { IOContext, InstanceOptions } from '@vtex/api'
import { JanusClient } from '@vtex/api'

interface OrderData {
  orderId: string
  status: string
}

export class MyJanusClient extends JanusClient {
  constructor(context: IOContext, options?: InstanceOptions) {
    super(context, {
      ...options,
      headers: {
        ...options?.headers,
        // Forward auth token — required for authenticated VTEX APIs
        VtexIdclientAutCookie: context.authToken,
      },
    })
  }

  public async getOrder(orderId: string): Promise<OrderData> {
    return this.http.get(`/api/oms/pvt/orders/${orderId}`, {
      metric: 'janus-get-order',
    })
  }

  public async updateOrderStatus(orderId: string, status: string) {
    return this.http.post(
      `/api/oms/pvt/orders/${orderId}/status`,
      { status },
      { metric: 'janus-update-order-status' }
    )
  }
}
```

**manifest.json policy required:**
```json
{
  "name": "outbound-access",
  "attrs": {
    "host": "{account}.vtexcommercestable.com.br",
    "path": "/api/oms/*"
  }
}
```

> ⚠️ **Always forward `VtexIdclientAutCookie`** in JanusClient headers. Without it, authenticated VTEX APIs will return 401.

---

### Pattern 3 — MasterData via `@vtex/api` (generic)

Built into `IOClients`. Access via `ctx.clients.masterdata`.

```typescript
// In middleware — no custom client file needed

// Search documents
const results = await ctx.clients.masterdata.searchDocuments<MyEntity>({
  dataEntity: 'MY',
  fields: ['id', 'email', 'field1'],
  where: `email="${email}"`,
  pagination: { page: 1, pageSize: 10 },
})

// Get single document
const doc = await ctx.clients.masterdata.getDocument<MyEntity>({
  dataEntity: 'MY',
  id: documentId,
  fields: ['id', 'email'],
})

// Create document
const { DocumentId } = await ctx.clients.masterdata.createDocument({
  dataEntity: 'MY',
  fields: { email, name },
})

// Partial update
await ctx.clients.masterdata.updatePartialDocument({
  dataEntity: 'MY',
  id: documentId,
  fields: { name: 'New name' },
})

// Delete
await ctx.clients.masterdata.deleteDocument({
  dataEntity: 'MY',
  id: documentId,
})
```

---

### Pattern 4 — MasterData via `masterDataFor` factory (typed, recommended)

Creates a fully typed client bound to a specific data entity.

```typescript
// node/clients/productReviews.ts
import { masterDataFor } from '@vtex/clients'

interface ProductReview {
  id?: string
  productId: string
  rating: number
  comment: string
  reviewerEmail: string
}

// Creates a typed client for the 'PR' data entity
const ProductReviewsClient = masterDataFor<ProductReview>('PR')

export { ProductReviewsClient }
```

```typescript
// node/clients/index.ts
import { IOClients } from '@vtex/api'
import { ProductReviewsClient } from './productReviews'

export class Clients extends IOClients {
  public get productReviews() {
    return this.getOrSet('productReviews', ProductReviewsClient)
  }
}
```

```typescript
// In middleware
const reviews = await ctx.clients.productReviews.search(
  { page: 1, pageSize: 10 },
  ['productId', 'rating', 'comment'],
  '',
  `productId=${productId}`
)

await ctx.clients.productReviews.save({
  productId,
  rating: 5,
  comment: 'Great product',
  reviewerEmail: email,
})
```

---

### Pattern 5 — VBase (file/blob storage)

VBase stores files and JSON blobs, versioned per app. Useful for configs, generated files, cached content.

```typescript
// node/clients/index.ts
import { IOClients } from '@vtex/api'
import { vbaseFor } from '@vtex/clients'

interface SiteConfig {
  bannerUrl: string
  promoActive: boolean
}

const SiteConfigVBase = vbaseFor<SiteConfig>()

export class Clients extends IOClients {
  public get siteConfig() {
    return this.getOrSet('siteConfig', SiteConfigVBase)
  }
}
```

```typescript
// In middleware
const BUCKET = 'site-config'
const FILE   = 'config.json'

// Save
await ctx.clients.siteConfig.save(BUCKET, FILE, {
  bannerUrl: 'https://cdn.example.com/banner.jpg',
  promoActive: true,
})

// Get
const config = await ctx.clients.siteConfig.get(BUCKET, FILE, null)

// Get raw (returns Buffer)
const raw = await ctx.clients.siteConfig.getRaw(BUCKET, FILE)
```

---

## 🔌 HttpClient Methods Reference

All custom clients (ExternalClient, JanusClient) expose `this.http` with these methods:

| Method | HTTP | Use |
|--------|------|-----|
| `this.http.get<T>(url, config?)` | GET | Fetch a resource |
| `this.http.getRaw<T>(url, config?)` | GET | Fetch with full response (headers, status) |
| `this.http.getWithBody<T>(url, data, config?)` | GET | GET with request body (only when required) |
| `this.http.getBuffer(url, config?)` | GET | Fetch binary data (Buffer) |
| `this.http.getStream(url, config?)` | GET | Fetch binary data (Stream) |
| `this.http.put<T>(url, data, config?)` | PUT | Replace a resource |
| `this.http.putRaw<T>(url, data, config?)` | PUT | PUT with full response (headers, status) |
| `this.http.post<T>(url, data, config?)` | POST | Create a resource |
| `this.http.postRaw<T>(url, data, config?)` | POST | POST with full response (headers, status) |
| `this.http.patch<T>(url, data, config?)` | PATCH | Partial update |
| `this.http.delete<T>(url, config?)` | DELETE | Remove a resource |
| `this.http.head<T>(url, config?)` | HEAD | Fetch headers only |

**Config options:**

```typescript
{
  metric: 'my-metric-name',  // Strongly recommended (metrics/observability)
  params: { q: 'query' },    // URL query params (?q=query)
  headers: { ... },          // Per-request headers (merged with instance headers)
  timeout: 3000,             // Override instance timeout (ms)
}
```

---

## ⚙️ InstanceOptions Reference

Configure your client in the constructor:

```typescript
constructor(context: IOContext, options?: InstanceOptions) {
  super('https://base-url.com', context, {
    ...options,          // Always spread incoming options
    retries: 2,          // Number of retry attempts on failure
    timeout: 3000,       // Request timeout in ms
    headers: {
      'x-vtex-use-https': 'true',  // Force HTTPS (recommended)
      Authorization: `Bearer ${token}`,
      ...options?.headers,          // Preserve any caller-provided headers
    },
  })
}
```

| Option | Type | Description |
|--------|------|-------------|
| `authType` | `string` | Auth strategy (when applicable) |
| `baseURL` | `string` | Base URL for relative requests |
| `concurrency` | `number` | Max concurrent requests |
| `diskCache` | `any` | Disk-based cache |
| `exponentialTimeoutCoefficient` | `number` | Timeout backoff coefficient (retries) |
| `exponentialBackoffCoefficient` | `number` | Backoff coefficient (retries) |
| `headers` | `object` | Default headers sent on every request |
| `httpsAgent` | `any` | Custom HTTPS agent |
| `initialBackoffDelay` | `number` | Initial backoff delay (ms) |
| `memoryCache` | `LRUCache` | In-memory cache instance (from `node/index.ts`) |
| `middlewares` | `Array<(ctx, next) => Promise<void>>` | HttpClient middlewares |
| `metrics` | `any` | Metrics configuration |
| `name` | `string` | Client name (metrics/debugging) |
| `params` | `object` | Default query params |
| `retries` | `number` | Retry count |
| `serverTimings` | `boolean` | Enable server-timing headers |
| `timeout` | `number` | Milliseconds before request aborts |
| `verbose` | `boolean` | Verbose logging |

---

## 🚦 DECISION TREE — Which client to use?

```
What are you calling?
│
├── VTEX Core API (/api/oms, /api/catalog, /api/checkout…)
│   ├── Already in @vtex/clients? → Use it (OMS, Catalog, Checkout, Logistics…)
│   └── Not in @vtex/clients?     → Create JanusClient
│
├── MasterData
│   ├── Simple CRUD, generic types  → ctx.clients.masterdata (@vtex/api)
│   └── Typed entity, complex ops   → masterDataFor factory (@vtex/clients)
│
├── VBase (files/blobs/configs)     → vbaseFor factory (@vtex/clients)
│
├── Another VTEX IO App
│   ├── REST endpoint               → AppClient (@vtex/api)
│   └── GraphQL endpoint            → AppGraphQLClient (@vtex/api)
│
└── External API (any non-VTEX URL) → ExternalClient (@vtex/api)
```

---

## ⚠️ COMMON ERRORS & FIXES

| Error | Cause | Fix |
|-------|-------|-----|
| `403 Forbidden` on external call | Missing `outbound-access` policy | Add policy in `manifest.json` for the specific host |
| `401 Unauthorized` on VTEX API | `authToken` not forwarded | Add `VtexIdclientAutCookie: context.authToken` to JanusClient headers |
| `TypeError: Cannot read property 'X' of undefined` | Client not registered in `Clients` class | Add getter in `node/clients/index.ts` |
| Client method returns `undefined` | Wrong response path or missing `await` | Use `getRaw` to inspect full response; always `await` |
| `Timeout` errors on heavy requests | Default timeout too low | Increase `timeout` in `InstanceOptions` or `service.json` |
| MasterData returns empty array | Wrong `where` clause syntax | Use `field="value"` (not `field: value`) |

---

## ✅ CHECKLIST

- [ ] Client extends the correct base class (`ExternalClient`, `JanusClient`, etc.)
- [ ] `outbound-access` policy added in `manifest.json` for every external host
- [ ] `VtexIdclientAutCookie: context.authToken` forwarded in JanusClient
- [ ] Constructor spreads `...options` before custom options
- [ ] Constructor spreads `...options?.headers` before custom headers
- [ ] Every `this.http.*` call has a `metric` string
- [ ] Client registered in `node/clients/index.ts` with `getOrSet`
- [ ] TypeScript interfaces defined for all request/response shapes
- [ ] `@vtex/clients` installed in `node/` if using `OMS`, `Catalog`, etc.

---

## 📚 REFERENCES

- `@vtex/clients` source: https://github.com/vtex/io-clients
- Native clients docs: https://developers.vtex.com/docs/guides/vtex-io-documentation-clients
- Custom clients guide: https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients
