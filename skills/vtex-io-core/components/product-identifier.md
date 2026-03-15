<!-- SCRAPED:START -->
# Product Identifier

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Product display](</docs/guides/product-display>)

Product Identifier

Official extension

Version: 0.5.1

Latest version: 0.5.1

![{"base64":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAABCAIAAAB2XpiaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAFUlEQVR4nGNgY2Mz1Nfll1L8f2MmAAvlA1rgBHAGAAAAAElFTkSuQmCC","img":{"src":"https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square","width":110,"height":20,"type":"svg"}}](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)

The Product Identifier app is responsible for showing a product identifier, such as a product reference, product ID, SKU EAN, or SKU reference.

![{"base64":"  ","img":{"width":208,"height":224,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":15885,"url":"https://user-images.githubusercontent.com/60782333/90151384-0abbd380-dd5d-11ea-9022-69ba4685e1d0.png"}}](https://user-images.githubusercontent.com/60782333/90151384-0abbd380-dd5d-11ea-9022-69ba4685e1d0.png)

## Configuration

  1. Add the `vtex.product-identifier` app to your Store Theme's dependencies in the `manifest.json` file:


```
"dependencies": {
    "vtex.product-identifier": "0.x"
}
```


  2. Add `product-identifier.product` block as a child of `product-summary.shelf`.


```
"product-identifier.product": {
  "props": {
    "label": "default", //'default' | 'custom' | 'hide'
    "customLabel": "teste", // text if label is custom
    "idField": "skuReferenceId" //'itemId' | 'productId' | 'productReference' | 'skuEan' | 'skuReferenceId'
  }
},
```





The `product-identifier` interface can also be configured in the [Site Editor](<https://developers.vtex.com/docs/guides/store-framework-working-with-site-editor>). You can choose to display the following identifiers:

  * Product Reference
  * Product ID
  * SKU EAN
  * SKU Reference ID
  * Item ID



It's also possible to customize or hide the label text. In the following example, the "Reference" text was substituted by "Foo."

![{"base64":"  ","img":{"width":208,"height":230,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":20602,"url":"https://user-images.githubusercontent.com/60782333/90145130-004a0b80-dd56-11ea-9cbd-5ee621da4d69.png"}}](https://user-images.githubusercontent.com/60782333/90145130-004a0b80-dd56-11ea-9cbd-5ee621da4d69.png)

## Customization

To apply CSS customization to this and other blocks, follow the instructions in the [Using CSS Handles for store customization](<https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization>) guide.

CSS Handles  
---  
`product-identifier`  
`product-identifier__label`  
`product-identifier__separator`  
`product-identifier__value`
<!-- SCRAPED:END -->
