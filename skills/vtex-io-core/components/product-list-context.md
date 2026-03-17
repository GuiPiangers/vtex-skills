<!-- SCRAPED:START -->
📢 Use this project, contribute to it or open issues to help evolve it using Store Discussion.
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

# Product List Context

The Product List Context is responsible for storing product data from an app and then providing it to specific store product components, such as the Shelf.

⚠️ This app is not rendered and should only be used to provide product data to specific store blocks.

## Configuration

Add the `product-list-context` app to the app's dependencies list (in the `manifest.json`) from which you want fetch product data. For example:

```json
"dependencies": {
  "vtex.product-list-context": "0.x"
}
```

| Prop name | Type | Description | Default Value |
| --- | --- | --- | --- |
| `listName` | `string` | The list that you are providing the products (e.g. `Home Shelf` or `Search Result`) | `'List of products'` |


In the app's files, use the `ProductListProvider` to initialise the context. You'll need to wrap the file's rendered component with the provider in order for its children to have access to the context's data. For example:

```tsx
return (
  <div ref={ref} className={`${handles.container} pv4 pb9`}>
    <ProductListProvider listName="Shelf">
      <ProductList {...productListProps} />
    </ProductListProvider>
  </div>
)
```

The Product List Context state is comprised of a object with the following properties: `nextImpressions`: List of products that are going to be sent on the product impression event.
`sentIds`: Set of the IDs of the products that were already impressed or are marked to be impressed.

You can use two Hooks to handle the data contained in the Product List Context object: `useProductListState` and `useProductListDispatch`.

`useProductListState`: used to get the data stored in the context. In order to use it, you need to first import and then call the hook anywhere in any file under the component which is wrapped by ProductListProvider. For example:

```tsx
import { ProductListContext } from 'vtex.product-list-context'

//...

  const { useProductListState } = ProductListContext
  const { nextImpressions } = useProductListState()
```

`useProductListDispatch`: returns a dispatch function that is used to change the context state. Notice that you should only import and declare this hook if you wish to change data that's stored in the context.

```tsx
import { ProductListContext } from 'vtex.product-list-context'

//...

  const { useProductListDispatch } = ProductListContext
  const dispatch = useProductListDispatch()
```

Starting from the dispatch function, you can add new values to the `nextImpressions` array (`SEND_IMPRESSION`) or reset this array (`RESET_NEXT_IMPRESSIONS`). For example:

```tsx
const dispatch = useProductListDispatch()  useEffect(() => {
  if (inView) {
    dispatch({ type: 'SEND_IMPRESSION', args: { product: product }})
  }
}, [inView])
```

This app also contains `useProductImpression`, which is a hook that you can call when you want to send impression events of the products in the `nextImpressions` array. For example:

```tsx
import { useProductImpression } from 'vtex.product-list-context'

//...

  useProductImpression()
```

When calling this hook, the `product-list-context` will always check if there is anything in the `nextImpressions` array. If there is, and the array doesn't change for one second, all the products in it will be impressed and the array will be reseted.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
<!-- SCRAPED:END -->

---

## Custom product list contexts (practical guide)

Use `vtex.product-list-context` when you need to **create a logical “product list”** (e.g. “Instagram related products”, “Campaign shelf”, “Recommended”) while still allowing ecosystem components (e.g. `vtex.product-summary`, `vtex.shelf`) to **consume product/SKU correctly** and emit **impression events**.

### When this is useful

- **Custom carousels and shelves** (data comes from an external API, CMS, custom GraphQL, etc.) while keeping VTEX product components working.
- **Lists by page context** (e.g. `SearchResult`, `HomeShelf`, `CampaignShelf`) for analytics and traceability.
- **Per-item SKU selection** (e.g. forcing the SKU coming from a campaign/UGC).

### Recommended `listName` conventions

`listName` is the list’s semantic key and typically appears in events/telemetry.

- **Be specific and stable**: prefer `InstagramRelatedProducts`, `CampaignShelfSummer2026`, `HomeShelfTopSellers`.
- **Avoid generic names** like `Shelf` when multiple lists exist on the same page.
- **Use PascalCase** (or another convention) consistently across the project.

### Mental model (provider stacking)

In custom lists, you typically stack providers like this:

- `ProductListContext.ProductListProvider` (defines the list “container” and its events)
  - for each item:
    - `vtex.product-context` `ProductContextProvider` (defines the “active” product/SKU for that card)
    - `vtex.product-summary-context` `ProductSummaryProvider` (normalizes data for `vtex.product-summary` and sets `selectedItem`)

This allows each card to have **its own product/SKU** while inheriting the **list name** for tracking.

### Full example: related products slider (Instagram)

This example shows:
- product normalization for `ProductSummary`
- explicit SKU selection (`selectedItem`)
- wrapping each card with `ProductContextProvider` + `ProductSummaryProvider`
- `ProductListProvider` with a custom `listName`

```tsx
import React, { useMemo } from 'react'
import { SliderLayout } from 'vtex.slider-layout'
import { ProductSummaryContext } from 'vtex.product-summary-context'
import { ProductListContext } from 'vtex.product-list-context'
import { ProductContextProvider } from 'vtex.product-context'
import ProductSummary from 'vtex.product-summary/ProductSummaryCustom'

import type { InstagramRelatedProduct } from '../types'
import styles from '../style.css'
import { findItemBySku } from '../utils/findItemBySku'
import { RelatedProductCard } from './RelatedProductCard'

const { ProductListProvider } = ProductListContext

interface RelatedProductsSliderProps {
  products: InstagramRelatedProduct[]
  loading: boolean
}

const RelatedProductsSlider: React.FC<RelatedProductsSliderProps> = ({
  products,
  loading,
  children,
}) => {
  const normalizedProducts = useMemo(
    () =>
      products.map(entry => {
        const normalizedProduct =
          ProductSummary.mapCatalogProductToProductSummary(entry.product)

        const selectedItem =
          findItemBySku({
            items: normalizedProduct?.items,
            skuId: entry.skuId,
          }) || normalizedProduct?.items?.[0]

        return { ...entry, normalizedProduct, selectedItem }
      }),
    [products]
  )

  if (loading) {
    return (
      <p className={styles.productsStateMessage}>
        Loading related products...
      </p>
    )
  }

  if (!products.length) {
    return (
      <p className={styles.productsStateMessage}>No related products</p>
    )
  }

  return (
    <ProductListProvider listName="InstagramRelatedProducts">
      <div className={styles.relatedProductsSliderWrapper}>
        <SliderLayout
          itemsPerPage={{ desktop: 2, tablet: 2, phone: 2 }}
          showNavigationArrows="desktopOnly"
          infinite={false}
          fullWidth
        >
          {normalizedProducts.map((entry, index) => (
            <ProductContextProvider
              key={`${entry.product?.productId}-${entry.skuId}-${index}`}
              product={entry.normalizedProduct}
              query={{ skuId: entry.skuId }}
            >
              <ProductSummaryContext.ProductSummaryProvider
                product={entry.normalizedProduct}
                selectedItem={entry.selectedItem}
              >
                <RelatedProductCard
                  product={entry.product}
                  targetSkuId={entry.skuId}
                >
                  {children}
                </RelatedProductCard>
              </ProductSummaryContext.ProductSummaryProvider>
            </ProductContextProvider>
          ))}
        </SliderLayout>
      </div>
    </ProductListProvider>
  )
}

export default RelatedProductsSlider
```

### Common pitfalls (and how to avoid them)

- **Repeated/ambiguous `listName`**: makes event analysis harder. Standardize names and document them.
- **Product “without a selected SKU”**: if you render `product-summary` with a specific SKU, ensure `selectedItem` (e.g. via `findItemBySku`).
- **Mixing “raw product” vs “normalized product”**: `ProductSummaryProvider` and `ProductContextProvider` may expect different shapes depending on your flow. In general:
  - **for `ProductSummary`**: use the “normalized” product in the `product-summary` shape.
  - **for your app’s auxiliary data**: keep the original `entry.product` in parallel.
- **Unstable keys**: in dynamic lists, use a deterministic key (e.g. `productId` + `skuId`) to avoid remounts and state loss.

---

## Quick reference (LLM-friendly)

### Goal

Create a custom product list with impression tracking/state using `ProductListProvider`, and ensure each card has `ProductContext` + `ProductSummaryContext` configured correctly.

### Minimal checklist

- **Dependency**: `vtex.product-list-context` in `manifest.json`.
- **List provider**: `ProductListContext.ProductListProvider` wrapping the whole list.
- **List name**: a semantic `listName` that is unique per context.
- **Per item**:
  - `ProductContextProvider` with `product` and (if needed) `query={{ skuId }}`.
  - `ProductSummaryContext.ProductSummaryProvider` with `product` and `selectedItem`.

### Common imports snippet

```ts
import { ProductListContext } from 'vtex.product-list-context'
import { ProductContextProvider } from 'vtex.product-context'
import { ProductSummaryContext } from 'vtex.product-summary-context'
```
