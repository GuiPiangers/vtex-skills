<!-- Manual content lives outside the SCRAPED markers. -->

<!-- SCRAPED:START -->
# Product Summary

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Product display](</docs/guides/product-display>)

Product Summary

Official extension

Version: 2.91.2

Latest version: 2.91.2

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)

Product Summary is an app for summarizing product information (such as name, price, and image) in other store blocks, such as the [Shelf](<https://developers.vtex.com/docs/guides/vtex-shelf/>) and the [Minicart](<https://developers.vtex.com/docs/guides/vtex-minicart/>).

![{"base64":"  ","img":{"width":596,"height":1074,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":177196,"url":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-0.png"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-0.png)

## Configurating the product summary

  1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:




```
"dependencies": {
    "vtex.product-summary": "2.x"
  }
```


Now, you can use all blocks exported by the `product-summary` app. See the full list below:

Block name| Description  
---|---  
[`list-context.product-list`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarylist>)| ![{"base64":"  ","img":{"width":69,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/-Mandatory-red"}}](https://img.shields.io/badge/-Mandatory-red) Renders the list of products in the Product Summary component. It fetches product information and provides it to the `product-summary.shelf` block. Then, this block provides its child blocks with the product information.  
`product-summary.shelf`| ![{"base64":"  ","img":{"width":69,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/-Mandatory-red"}}](https://img.shields.io/badge/-Mandatory-red) Logical block that provides the needed structure for the Product Summary component through its child blocks (listed below).  
[`product-summary-attachment-list`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryattachmentlist>)| Renders a list for product [attachments](<https://help.vtex.com/tutorial/adding-an-attachment--7zHMUpuoQE4cAskqEUWScU>).  
[`product-summary-brand`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarybrand>)| Renders the product brand.  
[`product-summary-buy-button`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarybuybutton>)| Renders the Buy button. This block must only be configured if your store uses the [Minicart v1](<https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md>). If your store uses the [Minicart v2](<https://developers.vtex.com/docs/guides/vtex-minicart>), please configure the [**Add to Cart button**](<https://developers.vtex.com/docs/guides/vtex-add-to-cart-button>) instead.  
[`product-summary-description`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarydescription>)| Renders the product description.  
[`product-summary-image`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryimage>)| Renders the product image.  
[`product-summary-name`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryname>)| Renders the product name.  
[`product-summary-sku-name`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryskuname>)| Renders the selected SKU name.  
`product-summary-price`| ![{"base64":"  ","img":{"width":73,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/-Deprecated-red"}}](https://img.shields.io/badge/-Deprecated-red) Renders the product price. This block has been deprecated in favor of the [Product Price](<https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-3.png>) app. Although support for this block is still available, we strongly recommend using the Product Price app.  
[`product-summary-sku-selector`](<https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryskuselector>)| Renders the SKU Selector block.  
[`product-specification-badges`](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummaryspecificationbadges>)| Renders badges based on product specifications.  
  
  2. Add the `list-context.product-list` block to a store template of your choice, and declare the `product-summary.shelf` in its block list. For example:




```
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
```


> Although the block name 'product-summary.shelf' alludes to the Shelf component, it is not necessary to use this block in order to create a shelf component. The Product Summary Shelf displays a summary of the product information in other components, such as the [Minicart](<https://developers.vtex.com/docs/guides/vtex-minicart>) and the [Search Results](<https://developers.vtex.com/docs/guides/vtex-search-result>) pages.

  3. Add the blocks from the list above as children of the `product-summary.shelf`, considering the product information you want to display in the product list. Take the following example in which the product name, description, image, price, SKU selector, and Buy button are all displayed in the Product Summary:




```
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
  "product-summary.shelf": {
    "children": [
      "product-summary-name",
      "product-summary-description",
      "product-summary-image",
      "product-summary-price",
      "product-summary-sku-selector",
      "product-summary-buy-button"
    ]
  }
}
```


## Customization

To apply CSS customizations to this and other blocks, follow the instructions given in the recipe on [Using CSS handles for store customization](<https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization>).

CSS handles  
---  
`aspectRatio`  
`buyButton`  
`buyButtonContainer`  
`clearLink`  
`column`  
`container`  
`containerNormal`  
`containerSmall`  
`containerInline`  
`description`  
`element`  
`image`  
`imageContainer`  
`imagePlaceholder`  
`information`  
`isHidden`  
`nameContainer`  
`priceContainer`  
`quantityStepperContainer`  
`spacer`
<!-- SCRAPED:END -->

## Mental Model (How to Think About It)

Product Summary is the base for product cards used in shelves/grids/search results.

In practice you always need:

- `list-context.product-list` as the data provider
- `product-summary.shelf` as the structure wrapper

Everything else is composition.

## Composition Patterns

### Pattern 1: Simple Shelf Card (Most Stores)

```json
{
  "list-context.product-list#shelf": {
    "blocks": ["product-summary.shelf#simple"]
  },
  "product-summary.shelf#simple": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-selling-price",
      "add-to-cart-button"
    ]
  }
}
```

### Pattern 2: Fashion Card (Badge + Variations)

```json
{
  "product-summary.shelf#fashion": {
    "children": [
      "stack-layout#image-badge",
      "product-summary-brand",
      "product-summary-name",
      "product-summary-sku-selector",
      "flex-layout.row#price",
      "add-to-cart-button"
    ]
  },
  "stack-layout#image-badge": {
    "children": ["product-summary-image", "product-specification-badges"]
  },
  "flex-layout.row#price": {
    "children": ["product-list-price", "product-selling-price"]
  }
}
```

### Pattern 3: Performance (Async Prices)

Use async prices when rendering large lists.

```json
{
  "search-result-layout.desktop": {
    "props": {
      "context": {
        "simulationBehavior": "skip"
      }
    }
  },
  "product-summary.shelf#async": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-price-suspense"
    ]
  },
  "product-price-suspense": {
    "children": ["product-selling-price", "product-installments", "add-to-cart-button"]
  }
}
```

## List Context Tuning (Pragmatic Defaults)

For shelves/grids:

- Prefer `skusFilter: "FIRST_AVAILABLE"` unless you need a SKU selector.
- Keep `maxItems` reasonable (12 is a good default).
- Use `hideUnavailableItems: true` when the experience should avoid out-of-stock cards.

Example:

```json
{
  "list-context.product-list#shelf": {
    "blocks": ["product-summary.shelf#simple"],
    "props": {
      "skusFilter": "FIRST_AVAILABLE",
      "maxItems": 12,
      "hideUnavailableItems": true
    }
  }
}
```

## Common Mistakes (Checklist)

- Declaring `product-summary.shelf` without `list-context.product-list` above it.
- Using deprecated/legacy blocks when modern apps exist (price and add-to-cart flows).
- Rendering too many items or fetching too many SKUs per card (slow shelves).
- Using "always add to cart" behavior without ensuring SKU selection.

## Internal References

- `skills/vtex-io-core/components/flex-layout.md`
- `skills/vtex-io-core/components/slider-layout.md`

