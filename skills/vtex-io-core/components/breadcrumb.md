<!-- SCRAPED:START -->
# Breadcrumb

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Navigation and search](</docs/guides/navigation-and-search>)

Breadcrumb

Official extension

Version: 1.9.6

Latest version: 1.9.6

The VTEX BreadCrumb is a navigation scheme that shows a user's browsing history up to their current location in your store.

![{"base64":"  ","img":{"width":2852,"height":1454,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":666089,"url":"https://user-images.githubusercontent.com/52087100/69836587-a4237380-1228-11ea-89c8-0f34cea3a96f.png"}}](https://user-images.githubusercontent.com/52087100/69836587-a4237380-1228-11ea-89c8-0f34cea3a96f.png)

## Configuration

  1. Import the breadcrumb's app to your theme's dependencies in the `manifest.json`, for example:




```
dependencies: {
    "vtex.breadcrumb": "1.x"
  }
```


  2. Add the `breadcrumb` block to the Product template. For example:




```
"breadcrumb": {
    "props": {
      "showOnMobile": true
    }
  },
```


Prop name| Type| Description| Default value  
---|---|---|---  
`showOnMobile`| `Boolean`| It determines whether Breadcrumb should also be displayed on mobile| `false`  
`homeIconSize`| `Number`| Controls the `size` property of [`IconHome`](<https://github.com/vtex-apps/store-icons#icons>)| `26`  
`caretIconSize`| `Number`| Controls the `size` property of [`IconCaret`](<https://github.com/vtex-apps/store-icons#icons>)| `8`  
  
:warning: The product's categories should appear as an array in one of this two formats:


```
categories = ['/Eletronics/', '/Eletronics/Computers']
```



```
categories = ['eletronics', 'eletronics-computers']
```


  3. Add the `breadcrumb.search` block to the Search template. For example:




```
"breadcrumb.search": {
    "props": {
      "showOnMobile": true
    }
  },
```


Prop name| Type| Description| Default value  
---|---|---|---  
`showOnMobile`| `Boolean`| It determines whether Breadcrumb should also be displayed on mobile| `false`  
`homeIconSize`| `Number`| Controls the `size` property of [`IconHome`](<https://github.com/vtex-apps/store-icons#icons>)| `26`  
`caretIconSize`| `Number`| Controls the `size` property of [`IconCaret`](<https://github.com/vtex-apps/store-icons#icons>)| `8`  
  
> _The`breadcrumb.search` block is specific for the Breadcrumb inside the search result page._

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](<https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization>).

CSS Handles  
---  
`container`  
`link`  
`arrow`  
`homeLink`  
`termArrow`
<!-- SCRAPED:END -->
