<!-- SCRAPED:START -->
# Add To Cart Button

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Cart and checkout](</docs/guides/cart-and-checkout>)

Add To Cart Button

Official extension

Version: 0.31.0

Latest version: 0.31.0

![{"base64":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAABCAIAAAB2XpiaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAFUlEQVR4nGNgY2Mz1Nfll1L8f2c+AAvzA2QiBBaKAAAAAElFTkSuQmCC","img":{"src":"https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square","width":110,"height":20,"type":"svg"}}](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)

The `add-to-cart-button` block is designed to add products to the [Minicart](<https://developers.vtex.com/docs/apps/vtex.minicart/>) (`minicart.v2`).

![{"base64":"  ","img":{"width":2094,"height":1052,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":407330,"url":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-add-to-cart-button-0.png"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-add-to-cart-button-0.png)

> The **Add to Cart** button is only compatible with stores using Minicart v2. For these stores, it will function correctly on the Shelf component and the Product Details page. If you are using [Minicart v1](<https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md>), you should configure the [Buy Button block](<https://developers.vtex.com/docs/apps/vtex.store-components/buybutton>) on the Product Details page and the [Product Summary Buy button](<https://developers.vtex.com/docs/apps/vtex.product-summary/productsummarybuybutton>) on the Shelf component instead.

## Configuration

  1. Import the `vtex.add-to-cart-button` app to your theme dependencies in the `manifest.json` file, as follows:




```
"dependencies": {
  "vtex.add-to-cart-button": "0.x"
}
```


  2. Add the `add-to-cart-button` to another theme block using the product context, such as the `product-summary.shelf`. In the example below, the `add-to-cart-button` is added to the `flex-layout.row` block from the `store.product` template, which uses the product context:




```
"store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
      "add-to-cart-button"
    ]
  }
```


Prop name| Type| Description| Default value  
---|---|---|---  
`onClickBehavior`| `enum`| Controls what happens when users click the button. Possible values are: `go-to-product-page`, `add-to-cart`, `ensure-sku-selection` (if multiple SKUs are available, users will be redirected to the product page to select the desired one. If the product only has 1 SKU available, it will be automatically added to the cart when the button is clicked) and `add-to-cart-and-trigger-shipping-modal` (opens a modal for ZIP code input if none is provided; otherwise, it adds the item to the cart. See more in [vtex.shipping-option-components](<https://github.com/vtex-apps/shipping-option-components>)).| `add-to-cart`  
`onClickEventPropagation`| `enum`| Controls whether the 'onClick' event, triggered upon user clicks, should propagate to the parent elements of the page. Possible values are: `disabled` and `enabled`.| `disabled`  
`isOneClickBuy`| `boolean`| Determines whether the user should be redirected to the checkout page (`true`) or not (`false`) when the **Add to Cart** button is clicked.| `false`  
`customOneClickBuyLink`| `string`| Defines the link to which users will be redirected when the **Add to Cart** button is clicked, and the `isOneClickBuy` prop is set to `true`.| `/checkout/#/cart`  
`customToastUrl`| `string`| Defines the link to which users will be redirected when the toast (pop-up notification displayed when adding an item to the minicart) is clicked.| `/checkout/#/cart`  
`text`| `string`| Defines a custom text message to be displayed on the **Add to Cart** button.| `Add to cart` _(automatic translation will be applied following your store default language)_  
`unavailableText`| `string`| Defines a custom text message to be displayed on the **Add to Cart** button when a product is unavailable.| `Unavailable` _(automatic translation will be applied following your store default language)_  
`customPixelEventId`| `string`| Defines the `id` for the event that the button will send upon user interaction.| `undefined`  
  
## Customization

To apply CSS customizations to this and other blocks, follow the instructions in [Using CSS Handles for store customization](<https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization>).

CSS Handles  
---  
`buttonText`  
`buttonDataContainer`  
`tooltipLabelText`
<!-- SCRAPED:END -->
