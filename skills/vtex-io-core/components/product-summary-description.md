<!-- SCRAPED:START -->
# Product Summary Description

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Product display](</docs/guides/product-display>)

Product Summary Description

[vtex.product-summary](<https://developers.vtex.com/docs/apps/vtex.product-summary>)

Version: 2.91.2

Latest version: 2.91.2

Product Summary Description is a block exported by the [Product Summary app](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary>) responsible for rendering the description of the product.

![{"base64":"  ","img":{"width":1895,"height":778,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":42263,"url":"https://user-images.githubusercontent.com/67270558/156373901-36a7a33d-9b32-4e0d-8798-ee4ddd01982d.png"}}](https://user-images.githubusercontent.com/67270558/156373901-36a7a33d-9b32-4e0d-8798-ee4ddd01982d.png)

## Configuration

  1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:




```
dependencies: {
    "vtex.product-summary": "2.x"
  }
```


  2. Add the `product-summary-description` block to your store theme as a child of `product-summary.shelf`. For example:




```
"product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
+     "product-summary-description",
      "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```


## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization>) guide.

CSS Handles  
---  
`description`
<!-- SCRAPED:END -->
