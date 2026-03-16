# VTEX IO — GraphQL in custom components (react-apollo)

> **Purpose:** Consume VTEX GraphQL APIs from Store Framework custom blocks using `react-apollo`.

---

## 🎯 WHEN TO USE THIS GUIDE

Load this guide when the task involves:
- Fetching VTEX data (Search/Catalog/other apps) inside a custom React component/block
- Writing `*.gql` / `*.graphql` queries or mutations
- Using Apollo hooks (`useQuery`, `useMutation`) from `react-apollo`
- Selecting a GraphQL **provider** with `@context(provider: "...")` (e.g. `vtex.search-graphql`)

**Related guides:**
- `skills/vtex-io-core/components/custom-components.md` → how to create blocks/components
- `skills/vtex-io-core/contexts/product-context.md` → prefer native product state when it fits

---

## 🧠 CORE CONCEPTS (VTEX IO)

### 1) GraphQL is multi-provider

In VTEX IO you often have **multiple GraphQL schemas** available (each app can expose its own schema). When querying a specific app’s schema, use:

```graphql
@context(provider: "vtex.search-graphql")
```

This routes the query to that provider.

### 2) Prefer `.gql` files and keep them colocated

A common pattern is:

```
react/
  graphql/
    queries/
    fragments/
  components/
```

This keeps queries stable and reusable across components.

### 3) `react-apollo` runs in Store Framework runtime

Store Framework already provides the Apollo runtime; your component code typically just:
- imports the `*.gql` document
- calls `useQuery` / `useMutation`
- renders based on `loading`, `error`, and `data`

---

## ✅ SETUP CHECKLIST

### 1) Ensure the provider app is installed (example: Search)

To query Search APIs, your app must depend on `vtex.search-graphql` in `manifest.json`:

```json
{
  "dependencies": {
    "vtex.search-graphql": "0.x"
  }
}
```

### 2) Ensure `react-apollo` is available to your React code

Install React Apollo in your app:

```bash
yarn add react-apollo
```

Then import hooks from `react-apollo`:

```ts
import { useQuery, useMutation } from 'react-apollo'
```

> Note: In VTEX IO, you **don’t** need the `graphql` builder to *consume* GraphQL APIs. The `graphql` builder is only for apps that *expose* a GraphQL API.

---

## 🧩 EXAMPLE — QUERYING `vtex.search-graphql`

### GraphQL query (`*.gql`)

Example inspired by `skills/vtex-io-core/graphql/examples/queries/searchProducts.gql`:

```graphql
query SearchProducts($fullText: String, $from: Int, $to: Int) {
  productSearch(fullText: $fullText, from: $from, to: $to)
    @context(provider: "vtex.search-graphql") {
    products {
      productId
      productName
      linkText
    }
  }
}
```

### React component using `useQuery`

```tsx
import React from 'react'
import { useQuery } from 'react-apollo'

import SEARCH_PRODUCTS from '../graphql/queries/searchProducts.gql'

type SearchProductsData = {
  productSearch?: {
    products: Array<{
      productId: string
      productName: string
      linkText: string
    }>
  }
}

type SearchProductsVars = {
  fullText?: string
  from?: number
  to?: number
}

type Props = { term: string }

const SearchPreview: React.FC<Props> = ({ term }) => {
  const { data, loading, error } = useQuery<SearchProductsData, SearchProductsVars>(
    SEARCH_PRODUCTS,
    {
      variables: { fullText: term, from: 0, to: 9 },
    }
  )

  if (loading) return <div>Loading…</div>
  if (error) return <div>Could not load products.</div>

  return (
    <ul>
      {(data?.productSearch?.products ?? []).map((p) => (
        <li key={p.productId}>{p.productName}</li>
      ))}
    </ul>
  )
}

export default SearchPreview
```

---

## 🧱 FRAGMENTS AND `#import` (REAL-WORLD QUERIES)

VTEX apps commonly use `#import` to compose queries from fragments (see `skills/vtex-io-core/graphql/examples`):

```graphql
#import "../fragments/product.gql"

query Search($fullText: String) {
  productSearch(fullText: $fullText) @context(provider: "vtex.search-graphql") {
    products {
      ...ProductFragment
    }
  }
}
```

Keep fragments small and domain-oriented (`product`, `item`, `seller`, `commertialOffer`, etc.).

---

## 🧷 TYPESCRIPT TYPING TIPS

When using `vtex.search-graphql`, you can type data using its exported schema types and `Pick` (see `skills/vtex-io-core/graphql/examples/types`):

```ts
import type { Product } from 'vtex.search-graphql'

export type ProductFragment = Pick<Product, 'productId' | 'productName' | 'linkText'>
```

Prefer typing only the fields you select, so the UI stays decoupled from the full schema.

---

## 🧯 TROUBLESHOOTING

- **Query works in IDE but fails in the component**: ensure the same `@context(provider: "...")` is present in your query file.
- **“Cannot query field …”**: you’re likely hitting a different schema/provider; add (or fix) the `@context(provider: ...)`.
- **TypeScript can’t find `vtex.search-graphql` types**: ensure `vtex.search-graphql` is a `manifest.json` dependency.
- **Over-fetching and slow render**: trim fields, paginate with `from/to`, and prefer native Store Framework contexts when available.

---

## 🧪 DEBUGGING WITH GRAPHQL IDE (ADMIN)

Install the GraphQL IDE app:

```bash
vtex install vtex.admin-graphql-ide
```

Then open **Admin → Apps → GraphQL IDE**, pick the app/provider, and run queries/mutations to validate schema, variables, and responses before wiring the UI.

---

## 🏗️ OPTIONAL — EXPOSING YOUR OWN GRAPHQL API (GRAPHQL BUILDER)

When your app needs to **create** a GraphQL API (instead of consuming one), use the `graphql` builder and define schema files under `graphql/` at the app root (commonly `graphql/schema.graphql`).

Reference guide: https://developers.vtex.com/docs/guides/vtex-io-documentation-graphql-builder/

---

## 🔗 REFERENCES

- Consuming data (react-apollo): https://developers.vtex.com/docs/guides/vtex-io-documentation-7-consuming-data
- `vtex.search-graphql` app: https://developers.vtex.com/docs/apps/vtex.search-graphql
- Local examples: `skills/vtex-io-core/graphql/examples`
