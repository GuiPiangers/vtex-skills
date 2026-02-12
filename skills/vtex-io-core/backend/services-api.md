# VTEX IO Backend — Services & Routes Guide

> Operational guide for building Node.js backend services in VTEX IO

---

## 🎯 WHEN TO USE THIS GUIDE

Load this guide when the task involves:
- Creating routes/endpoints in a VTEX IO app
- Writing middleware functions
- Structuring the `node/` folder
- Declaring `service.json` settings
- Setting up `manifest.json` policies
- Wiring routes → middlewares in `node/index.ts`

**Related guides:**
- `guides/backend/clients.md` → for HTTP clients and external API calls
- `guides/backend/graphql.md` → for GraphQL schema and resolvers

---

## 📂 FILE STRUCTURE

```
node/
├── clients/
│   ├── index.ts        # Exports Clients class (extends IOClients)
│   └── myClient.ts     # Custom client implementations
├── middlewares/
│   └── myMiddleware.ts # Middleware functions
├── index.ts            # Service entry point — wires routes + clients
├── service.json        # Infrastructure config + route declarations
├── package.json        # Node dependencies
└── tsconfig.json       # TypeScript config
```

**Root:**
```
manifest.json   # App definition + builders + policies
```

---

## 🔧 STEP 1 — manifest.json

The `node` builder **must** be declared. Without it, the `node/` folder is ignored.

```json
{
  "vendor": "myvendor",
  "name": "my-service",
  "version": "0.1.0",
  "builders": {
    "node": "7.x"
  },
  "policies": [],
  "credentialType": "absolute"
}
```

### Policies

Policies grant the app permission to access external resources. **Without the correct policy, requests will be blocked.**

```json
"policies": [
  {
    "name": "outbound-access",
    "attrs": {
      "host": "api.externaldomain.com",
      "path": "/*"
    }
  },
  {
    "name": "outbound-access",
    "attrs": {
      "host": "api.vtex.com",
      "path": "/*"
    }
  },
  {
    "name": "ADMIN_DS"
  },
  {
    "name": "OMSViewer"
  },
  {
    "name": "colossus-fire-event"
  },
  {
    "name": "colossus-write-logs"
  }
]
```

**Common policies reference:**

| Policy | Purpose |
|--------|---------|
| `outbound-access` | Access to external URLs (require `host` + `path`) |
| `ADMIN_DS` | Read/write access to Master Data |
| `OMSViewer` | Read access to OMS (orders) |
| `colossus-fire-event` | Emit events |
| `colossus-write-logs` | Write logs to VTEX Colossus |

> ⚠️ **Rule:** Every external host the app calls must have a corresponding `outbound-access` policy. This includes VTEX's own APIs (e.g., `api.vtex.com`, `{account}.vtexcommercestable.com.br`).

---

## 🔧 STEP 2 — node/service.json

Declares infrastructure settings and **all routes** the service exposes.

```json
{
  "memory": 256,
  "ttl": 10,
  "timeout": 2,
  "minReplicas": 2,
  "maxReplicas": 4,
  "workers": 1,
  "routes": {
    "routeKey": {
      "path": "/_v/my-route/:param",
      "public": true
    }
  }
}
```

### Infrastructure fields

| Field | Type | Description |
|-------|------|-------------|
| `memory` | `integer` | MB allocated to the app (auto-adjusted on overuse) |
| `ttl` | `integer` | Minutes to keep the app alive after last request |
| `timeout` | `integer` | Seconds before a request is aborted |
| `minReplicas` | `integer` | Minimum running instances |
| `maxReplicas` | `integer` | Maximum instances (auto-scaled) |
| `workers` | `integer` | Worker threads per replica |

### Route declaration

```json
"routes": {
  "routeKey": {
    "path": "/_v/my-endpoint/:param",
    "public": true
  }
}
```

| Field | Description |
|-------|-------------|
| `routeKey` | Identifier used in `index.ts` to map this route to a middleware |
| `path` | URL path. Prefix `/_v/` for public routes. Supports `:params` |
| `public` | `true` = no auth required; `false` = requires VTEX token |

> ⚠️ **Rule:** The `routeKey` in `service.json` must exactly match the key used in `index.ts` routes map.

---

## 🔧 STEP 3 — node/index.ts

The service entry point. Declares clients config, global types, and maps routes to middleware handlers.

```typescript
import type { ClientsConfig, ServiceContext, RecorderState } from '@vtex/api'
import { LRUCache, method, Service } from '@vtex/api'

import { Clients } from './clients'
import { myMiddleware } from './middlewares/myMiddleware'

const TIMEOUT_MS = 800

// Optional: in-memory cache for clients
const memoryCache = new LRUCache<string, any>({ max: 5000 })
metrics.trackCache('status', memoryCache)

// Client configuration
const clients: ClientsConfig<Clients> = {
  implementation: Clients,
  options: {
    default: {
      retries: 2,
      timeout: TIMEOUT_MS,
    },
    status: {
      memoryCache,
    },
  },
}

// Global type declarations
declare global {
  type Context = ServiceContext<Clients, State>
  interface State extends RecorderState {
    code: number
  }
}

// Service wiring: routeKey → method → [middlewares]
export default new Service({
  clients,
  routes: {
    routeKey: method({
      GET: [myMiddleware],
    }),
  },
})
```

### `method()` HTTP verbs

```typescript
routes: {
  myRoute: method({
    GET:    [middlewareA],
    POST:   [middlewareB],
    PUT:    [middlewareC],
    DELETE: [middlewareD],
  }),
}
```

### Middleware pipeline

Multiple middlewares can be chained per route. Each must call `await next()` to pass execution forward.

```typescript
routes: {
  myRoute: method({
    GET: [validateMiddleware, fetchMiddleware, transformMiddleware],
  }),
}
```

---

## 🔧 STEP 4 — node/clients/index.ts

Exports the `Clients` class that bundles all clients for injection into the context.

```typescript
import { IOClients } from '@vtex/api'
import { OMS } from '@vtex/clients'
import MasterData from './masterdata'
import { MyCustomClient } from './myCustomClient'

export class Clients extends IOClients {
  public get oms() {
    return this.getOrSet('oms', OMS)
  }

  public get masterdata() {
    return this.getOrSet('masterdata', MasterData)
  }

  public get myCustomClient() {
    return this.getOrSet('myCustomClient', MyCustomClient)
  }
}
```

> See `guides/backend/clients.md` for how to build each type of client.

---

## 🔧 STEP 5 — node/middlewares/

Each middleware is an `async` function with `(ctx: Context, next: () => Promise<unknown>)` signature.

### GET middleware (read)

```typescript
export async function getOrderMiddleware(
  ctx: Context,
  next: () => Promise<unknown>
) {
  const { code } = ctx.vtex.route.params

  if (!code || typeof code !== 'string') {
    ctx.status = 400
    ctx.body = { message: 'code param is required' }
    return
  }

  try {
    const order = await ctx.clients.oms.order(code)
    ctx.status = 200
    ctx.body = order
    await next()
  } catch (error) {
    ctx.status = 500
    ctx.body = { message: 'Error fetching order' }
  }
}
```

### POST middleware (write)

```typescript
import { UserInputError } from '@vtex/api'
import { json } from 'co-body'

export async function saveDataMiddleware(
  ctx: Context,
  next: () => Promise<unknown>
) {
  try {
    const body = await json(ctx.req) as { field?: string }

    if (!body.field) {
      throw new UserInputError('field is required')
    }

    await ctx.clients.masterdata.createDocument({
      dataEntity: 'MY',
      fields: { field: body.field },
    })

    ctx.status = 200
    ctx.body = { message: 'Saved successfully' }
  } catch (error) {
    ctx.status = error instanceof UserInputError ? 400 : 500
    ctx.body = { message: error.message || 'Internal server error' }
  }

  await next()
}
```

---

## 📋 CONTEXT REFERENCE

The `ctx` object gives access to everything available in a middleware:

```typescript
// Route params (declared in service.json path as :param)
ctx.vtex.route.params.myParam

// Auth token (for authenticated calls)
ctx.vtex.authToken

// Account and workspace info
ctx.vtex.account
ctx.vtex.workspace

// All injected clients
ctx.clients.myClient

// Request body (must parse manually for POST/PUT)
const body = await json(ctx.req)

// Set response
ctx.status = 200
ctx.body = { ... }
```

---

## 🔁 MIDDLEWARE PIPELINE RULES

```
1. Always call `await next()` at the end if the pipeline should continue
2. If returning early (error/guard), do NOT call `await next()`
3. Never throw uncaught errors — always wrap in try/catch
4. Set BOTH ctx.status and ctx.body before finishing
5. Use `UserInputError` from `@vtex/api` for 400-class errors
```

### Early return pattern (guard middleware)

```typescript
export async function validateMiddleware(
  ctx: Context,
  next: () => Promise<unknown>
) {
  const { id } = ctx.vtex.route.params

  if (!id) {
    ctx.status = 400
    ctx.body = { message: 'id is required' }
    return  // Stops pipeline here — next() is NOT called
  }

  await next()  // Continues to next middleware
}
```

---

## ⚠️ COMMON ERRORS & FIXES

| Error | Cause | Fix |
|-------|-------|-----|
| `403 Forbidden` on external request | Missing `outbound-access` policy | Add policy to `manifest.json` with correct `host` |
| Route returns 404 | `routeKey` mismatch between `service.json` and `index.ts` | Ensure keys match exactly |
| `Cannot read property of undefined` on params | Missing param in path or wrong key name | Check `service.json` path matches param name |
| Request body is empty on POST | Body not parsed | Use `await json(ctx.req)` from `co-body` |
| App crashes on deploy | `await next()` missing in middleware | Always call `await next()` at pipeline end |
| `401 Unauthorized` on VTEX API call | Auth token not forwarded in client | Add `VtexIdclientAutCookie: context.authToken` to headers |

---

## 🏗️ FULL EXAMPLE — Wiring a GET + POST route

### service.json
```json
{
  "memory": 256,
  "ttl": 10,
  "timeout": 2,
  "minReplicas": 2,
  "maxReplicas": 4,
  "workers": 1,
  "routes": {
    "getItem":  { "path": "/_v/item/:id",  "public": true },
    "saveItem": { "path": "/_v/item",      "public": true }
  }
}
```

### node/index.ts
```typescript
import { LRUCache, method, Service } from '@vtex/api'
import type { ClientsConfig, ServiceContext, RecorderState } from '@vtex/api'

import { Clients } from './clients'
import { getItemMiddleware } from './middlewares/getItem'
import { saveItemMiddleware } from './middlewares/saveItem'

const clients: ClientsConfig<Clients> = {
  implementation: Clients,
  options: { default: { retries: 2, timeout: 800 } },
}

declare global {
  type Context = ServiceContext<Clients, State>
  interface State extends RecorderState { code: number }
}

export default new Service({
  clients,
  routes: {
    getItem:  method({ GET:  [getItemMiddleware] }),
    saveItem: method({ POST: [saveItemMiddleware] }),
  },
})
```

---

## ✅ CHECKLIST

- [ ] `node` builder declared in `manifest.json`
- [ ] `credentialType: "absolute"` set in `manifest.json`
- [ ] All external hosts have `outbound-access` policy
- [ ] Route keys match exactly between `service.json` and `index.ts`
- [ ] Every middleware calls `await next()` unless returning early
- [ ] POST bodies parsed with `await json(ctx.req)`
- [ ] All errors caught in try/catch, `ctx.status` always set
- [ ] `UserInputError` used for 400-class validation errors
- [ ] `Clients` class in `node/clients/index.ts` exports all clients

---

## 📚 REFERENCES

- Service app boilerplate: https://github.com/vtex-apps/service-example
- Official guide: https://developers.vtex.com/docs/guides/calling-commerce-apis-1-getting-the-service-app-boilerplate
- Policies: https://developers.vtex.com/docs/guides/vtex-io-documentation-policies