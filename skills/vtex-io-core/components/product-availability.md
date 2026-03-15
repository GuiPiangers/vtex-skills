<!-- SCRAPED:START -->
# Product Availability

[VTEX IO Apps](</docs/vtex-io-apps>)

Shopper experience

Product Availability

Official extension

Version: 0.3.2

Latest version: 0.3.2

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)

The Product Availability app displays text messages regarding the in-stock quantity for products.

![{"base64":"  ","img":{"width":2406,"height":1124,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":515402,"url":"https://user-images.githubusercontent.com/52087100/99307082-c8f76900-2834-11eb-96f2-df5e9d2bc49a.png"}}](https://user-images.githubusercontent.com/52087100/99307082-c8f76900-2834-11eb-96f2-df5e9d2bc49a.png)

## Configuration

  1. Add the Product Availability app to your theme's dependencies in the `manifest.json` file:




```
"dependencies": {
+  "vtex.product-availability": "0.x"
 }
```


  2. Add the `product-availability` block to the desired theme block whose data is fetched from the [Product Context](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-context>), such as the [Minicart](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-minicart>). For example:




```
"product-availability": {
  "props": {
    "threshold": "10",
    "lowStockMessage": "Only {quantity} left!",
    "highStockMessage": "Item in stock!"
  }
}
```


Prop name| Type| Description| Default value  
---|---|---|---  
`threshold`| `number`| Minimum product quantity that makes the low stock message to be displayed (if any message is set in the `lowStockMessage` prop).| `0`  
`lowStockMessage`| `string`| Message text to be displayed when the in-stock quantity is lower than the quantity defined in the `threshold` prop. This prop value must have `{quantity}` inside the string text in order to properly display the stock quantity according to the threshold. For example: `"Only {quantity} left!`. Notice: if this prop's value is left empty, no message will be shown.| `""`  
`highStockMessage`| `string`| Message text to be displayed when the in-stock quantity is higher or equal than the quantity defined in the `threshold` prop. Notice: if this prop's value is left empty, no message will be shown.| `""`  
  
## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization>).

CSS Handles  
---  
`container`  
`highStockText`  
`lowStockHighlight`  
`lowStockText`
<!-- SCRAPED:END -->
