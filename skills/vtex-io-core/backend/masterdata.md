# VTEX IO Backend — MasterData Guide

> Complete operational guide for using MasterData v1 and v2 in VTEX IO Node services

---

## 🎯 WHEN TO USE THIS GUIDE

Load this guide when the task involves:

* Reading, creating, updating, or deleting documents in MasterData
* Searching/filtering with `search` or `scroll`
* Using native entities (CL, AD) or custom entities
* Defining JSON schemas (v2)
* Deciding between MasterData v1 or v2

**Related guides:**

* `guides/backend/clients.md` → registering clients in the `Clients` index
* `guides/backend/services-api.md` → middleware and route structure

---

## ⚡ V1 vs V2 — FUNDAMENTAL DIFFERENCES

|                          | **MasterData v1**                        | **MasterData v2**                                     |
| ------------------------ | ---------------------------------------- | ----------------------------------------------------- |
| **Configuration**        | Via VTEX Admin (GUI)                     | Via API or `masterdata` builder (code)                |
| **Entity naming**        | 2-letter uppercase acronyms (`CL`, `AD`) | Free names (`Client`, `BookReview`)                   |
| **Field validation**     | Fixed format configured in Admin         | JSON Schema (flexible, supports nested objects)       |
| **Nested fields**        | ✗ Not supported                          | ✓ Supports nested objects and arrays                  |
| **Schemas**              | Does not exist                           | Mandatory for indexing and validation                 |
| **VTEX IO Builder**      | No specific builder                      | `masterdata` builder manages schemas                  |
| **Native VTEX entities** | `CL` (clients), `AD` (addresses), etc.   | Custom entities with `{vendor}_{app}_{entity}` prefix |
| **When to use**          | Native VTEX entities or legacy projects  | Custom entities in new apps                           |

---

## 🗂️ ACCESS APPROACHES

There are three ways to access MasterData via VTEX IO:

```
1. ctx.clients.masterdata               → native @vtex/api client (v1 and v2)
2. masterDataFor() factory              → @vtex/clients, entity-typed (v1 and v2)
3. masterdata builder + masterDataFor   → v2 only, schemas managed by the app
```

Decision table:

| Scenario                                 | Recommended approach                          |
| ---------------------------------------- | --------------------------------------------- |
| Native VTEX entities (`CL`, `AD`)        | Direct `ctx.clients.masterdata`               |
| Simple custom entity, no schema          | `masterDataFor` factory (v1)                  |
| Custom entity with app-controlled schema | `masterdata` builder + `masterDataFor` (v2)   |
| Fast CRUD without strong typing          | Direct `ctx.clients.masterdata`               |
| Distributed/published app (App Store)    | `masterdata` builder (v2) — versioned schemas |

---

## 📦 SETUP — REQUIRED POLICIES

Add to `manifest.json`:

```json
"policies": [
  {
    "name": "outbound-access",
    "attrs": {
      "host": "api.vtex.com",
      "path": "/api/*"
    }
  },
  {
    "name": "ADMIN_DS"
  }
]
```

> ⚠️ Without `ADMIN_DS`, MasterData calls return `403 Forbidden`.

---

## 🔵 MASTERDATA V1 — via `ctx.clients.masterdata`

Automatically available via `@vtex/api`. No custom client required.

### Direct access in middleware

```ts
const docs = await ctx.clients.masterdata.searchDocuments({ ... })
```

### Create document

```ts
const { DocumentId } = await ctx.clients.masterdata.createDocument({
  dataEntity: 'CL',
  fields: {
    email: 'user@example.com',
    firstName: 'John',
    lastName: 'Doe',
  },
})
```

### Get document by ID

```ts
const doc = await ctx.clients.masterdata.getDocument<ClientDocument>({
  dataEntity: 'CL',
  id: '0807f150-68bb-11ec-82ac-12fdbe358f3f',
  fields: ['id', 'email', 'firstName', 'birthDate'],
})
```

### Search documents

```ts
const results = await ctx.clients.masterdata.searchDocuments<ClientDocument>({
  dataEntity: 'CL',
  fields: ['id', 'email', 'firstName', 'birthDate'],
  where: `email="user@example.com"`,
  pagination: { page: 1, pageSize: 10 },
  sort: 'firstName ASC',
})
```

### Partial update (recommended)

```ts
await ctx.clients.masterdata.updatePartialDocument({
  dataEntity: 'CL',
  id: documentId,
  fields: {
    birthDate: '1990-05-20',
    phone: '+55 11 99999-0000',
  },
})
```

---

## 🟢 MASTERDATA V2 — via `masterDataFor` factory

### Installation

```bash
yarn add @vtex/clients
```

### Typed client

```ts
import { masterDataFor } from '@vtex/clients'

export interface ProductReview {
  id?: string
  productId: string
  rating: number
  comment: string
  reviewerEmail: string
  createdAt?: string
}

export const ProductReviewsClient = masterDataFor<ProductReview>('PR')
export const ProductReviewsClientV2 = masterDataFor<ProductReview>('PR', undefined, 2)
```

---

## 🟣 MASTERDATA V2 — via `masterdata` builder

Use when your app must control the schema.

### Folder structure

```
masterdata/
└── bookReview/
    ├── schema.json
    └── triggers/
        └── onSave.json
```

### Example schema

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "bookReview",
  "type": "object",
  "properties": {
    "bookId": { "type": "string" },
    "rating": { "type": "number" },
    "comment": { "type": "string" },
    "reviewerEmail": { "type": "string" },
    "approved": { "type": "boolean" }
  },
  "required": ["bookId", "rating", "reviewerEmail"],
  "v-default-fields": ["bookId", "rating", "comment"],
  "v-indexed": ["bookId", "reviewerEmail", "rating"]
}
```

---

## 🔍 `where` SYNTAX (FILTERS)

```ts
where: `email="user@example.com"`
where: `rating>3`
where: `status="pending" AND active=true`
where: `(status="pending" OR status="processing") AND active=true`
```

---

## ⚠️ COMMON ERRORS

| Error                 | Cause              | Fix                          |
| --------------------- | ------------------ | ---------------------------- |
| `403 Forbidden`       | Missing `ADMIN_DS` | Add policy                   |
| `404 Not Found`       | Invalid ID         | Handle with try/catch        |
| `where` error         | Field not indexed  | Add `v-indexed` or Is Filter |
| Duplicate scroll data | No sort            | Add `sort`                   |
| 60 schema limit       | Too many versions  | Delete old schemas           |

---

## ✅ CHECKLIST

* [ ] `ADMIN_DS` policy
* [ ] `outbound-access` policy
* [ ] Indexed filter fields
* [ ] Scroll uses `mdToken`
* [ ] Prefer partial updates
* [ ] Typed interfaces
* [ ] `masterDataFor(..., 2)` for v2
* [ ] Old schemas cleaned
* [ ] `getDocument` wrapped in try/catch

---

## 📚 REFERENCES

* [https://developers.vtex.com/docs/guides/interacting-with-master-data-v1-through-vtex-io-services](https://developers.vtex.com/docs/guides/interacting-with-master-data-v1-through-vtex-io-services)
* [https://developers.vtex.com/docs/guides/create-master-data-crud-app](https://developers.vtex.com/docs/guides/create-master-data-crud-app)
* [https://developers.vtex.com/docs/guides/extracting-data-from-master-data-with-search-and-scroll](https://developers.vtex.com/docs/guides/extracting-data-from-master-data-with-search-and-scroll)
* [https://github.com/vtex/io-clients](https://github.com/vtex/io-clients)
