<!-- SCRAPED:START -->
# Locale Switcher

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Navigation and search](</docs/guides/navigation-and-search>)

Locale Switcher

Official extension

Version: 0.5.6

Latest version: 0.5.6

The Locale Switcher app provides a component capable of changing the current language of your store.

![{"base64":"  ","img":{"width":73,"height":152,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":3496,"url":"https://user-images.githubusercontent.com/27777263/74359290-c2b5f700-4da1-11ea-8612-c05ccf1988d5.png"}}](https://user-images.githubusercontent.com/27777263/74359290-c2b5f700-4da1-11ea-8612-c05ccf1988d5.png)

## Configuration

  1. Add the Locale Switcher app to your theme's dependencies in the `manifest.json` file:




```
"dependencies": {
+  "vtex.locale-switcher": "0.x"
 }
```


  2. Add the `locale-switcher` block to your header. For example:




```
"header-row#desktop": {
  "children": [
    // (...)
    "locale-switcher",
    "login",
    "minicart.v2"
  ]
},
```


  3. Open a ticket to our support team in order to adjust your store's binding with the desired languages.



> _**Caution:** The third step is mandatory. If no ticket is opened requiring the desired languages, the selection list may not appear on the Locale Switcher component._

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](<https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization>).

CSS Handles  
---  
`button`  
`buttonText`  
`container`  
`list`  
`listElement`  
`localeIdText`  
`relativeContainer`
<!-- SCRAPED:END -->
