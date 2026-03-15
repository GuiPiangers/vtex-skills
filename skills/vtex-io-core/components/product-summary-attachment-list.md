<!-- SCRAPED:START -->
# Product Summary Attachment List

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Product display](</docs/guides/product-display>)

Product Summary Attachment List

[vtex.product-summary](<https://developers.vtex.com/docs/apps/vtex.product-summary>)

Version: 2.91.2

Latest version: 2.91.2

Product Summary Attachment is the block exported by the [Product Summary app](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary>) responsible for rendering the [attachment](<https://help.vtex.com/en/tutorial/o-que-e-um-anexo--aGICk0RVbqKg6GYmQcWUm>) options available for a product.

![{"base64":"  ","img":{"width":1164,"height":751,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":722236,"url":"https://user-images.githubusercontent.com/67270558/156370029-833f68ce-a270-4e01-ae20-5d63061f0a03.png"}}](https://user-images.githubusercontent.com/67270558/156370029-833f68ce-a270-4e01-ae20-5d63061f0a03.png)

## Configuration

  1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:




```
"dependencies": {
    "vtex.product-summary": "2.x"
  }
```


  2. Add the `product-summary-attachment-list` block to a store template of your choice as a child of the `product-summary.shelf` block. For example:




```
"product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-summary-sku-name",
+     "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```


After adding the `product-summary-attachment-list` block to your store theme, use the VTEX Admin to add attachments to your products to display the component in your store correctly. For more information, please refer to [Adding an attachment](<https://help.vtex.com/en/tutorial/cadastrar-um-anexo--7zHMUpuoQE4cAskqEUWScU>).

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](<https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization>) guide.

CSS Handles  
---  
`attachmentListContainer`  
`attachmentItemContainer`  
`attachmentItem`  
`attachmentItemProductText`
<!-- SCRAPED:END -->
