<!-- SCRAPED:START -->
# Iframe

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Layout and interaction patterns](</docs/guides/layout-and-interacion-patterns>)

Iframe

Official extension

Version: 0.8.0

Latest version: 0.8.0

![{"base64":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAABCAIAAAB2XpiaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAFUlEQVR4nGNgY2Mz1Nfll1L8f2c+AAvzA2QiBBaKAAAAAElFTkSuQmCC","img":{"src":"https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square","width":110,"height":20,"type":"svg"}}](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)

An app that makes it possible to render external iframes on a store.

![{"base64":"  ","img":{"width":354,"height":636,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":184249,"url":"https://user-images.githubusercontent.com/18701182/67055752-abcb0500-f11f-11e9-8c24-50234214d474.png"}}](https://user-images.githubusercontent.com/18701182/67055752-abcb0500-f11f-11e9-8c24-50234214d474.png)

## Configuration - standard Iframe

  1. Add the `vtex.iframe` to the theme's dependencies on the `manifest.json`




```
"dependencies": {
 "vtex.iframe": "0.x"
}
```


  2. Add the interface `iframe` to any **custom page** (Iframes are not allowed outside custom pages).




```
{
  "store.custom#about-us": {
    "blocks": ["flex-layout.row#about-us", "iframe"]
  },
  "iframe": {
    "props": {
      "src": ""
    }
  }
}
```


Prop name| Type| Description| Default value  
---|---|---|---  
`src`| String| Source address the iframe should render| `null`  
`width`| Number| Width attribute of the iframe| `null`  
`height`| Number| Height attribute of the iframe| `null`  
`allow`| String| allow attribute of the iframe| `null`  
  
## Configuration - dynamic Iframe

  1. Add the `vtex.iframe` to the theme's dependencies on the `manifest.json`




```
"dependencies": {
  "vtex.iframe": "0.x"
}
```


  2. Add the dynamicIframe block and its properties to the blocks.json file




```
{
  "store.custom#locationPage": {
    "children": ["iframe.dynamic-src"]
  },
  "iframe.dynamic-src": {
    "props": {
      "dynamicSrc": "https://www.test.com/exampleStaticPathName/{dynamicParam1}/{dynamicParam2}/exampleStaticPageName",
      "width": "1920",
      "height": "1000",
      "title": "exampleStaticPageName iframe wrapper for {account}",
      "allow": "geolocation"
    }
  }
}
```


  3. register your new page in routes.json with appropriate parameters passed into the page url




```
{
  "store.custom#locationPage": {
    "path": "/:param1/:param2/pagename"
  }
}
```


Prop name| Type| Description| Default value  
---|---|---|---  
`dynamicSrc`| String| iframe src with dynamic parameters from page URL enclosed in '{}'| `null`  
`width`| Number| Width attribute of the iframe| `null`  
`height`| Number| Height attribute of the iframe| `null`  
`title`| String| title attribute of the iframe| `null`  
`allow`| String| allow attribute of the iframe| `null`  
`id`| String| ID attribute of the iframe| `null`  
`className`| String| class attribute of the iframe| `null`  
`onLoad`| String| onLoad attribute of the iframe| `null`  
`srcAccount`| Object| Object with account name and src| `null`  
  
### srcAccount

Using srcAccount


```
"iframe#logout": {
    "props": {
      "src": "//www.mywebsiteprod.com/logout",
      "srcAccount": {
        "mywebsiteprod": "//www.mywebsite.com/logout",
        "mywebsiteqa": "//qa.mywebsite.com/logout"
      },
      "onLoad": "setTimeout(() => {window.location.href='/'}, 5000)",
      "className": "iframeLogout",
      "id": "iframeLogout"
    }
  },
```


## Customization

There is a `.container` handle that wraps the iframe, it's also possible to use `blockClass`.
<!-- SCRAPED:END -->
