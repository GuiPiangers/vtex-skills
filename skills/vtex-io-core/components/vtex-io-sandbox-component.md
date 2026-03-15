<!-- SCRAPED:START -->
# VTEX IO Sandbox Component

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Layout and interaction patterns](</docs/guides/layout-and-interacion-patterns>)

VTEX IO Sandbox Component

Official extension

Version: 0.5.1

Latest version: 0.5.1

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)

Allows mounting arbitrary HTML content in extension points from the comfort and safety of an iframe.

### Example block


```
"sandbox.product": {
    "props": {
      "width": "200px",
      "height": "60px",
      "initialContent": "<script src='https://unpkg.com/jquery@3.3.1/dist/jquery.min.js'></script><h1 id='test'>initial</h1><script>function render(){ current = window.props.productQuery.product.items.findIndex(function(p){ return p.itemId === window.props.query.skuId }); if (current === -1) {current = 0}; $('#test').html(window.props.productQuery.product.items[current].sellers[0].commertialOffer.ListPrice)}; window.addEventListener('message', function(e){ console.log('got message in product', e.data, window.props); render();});</script>",
      "allowCookies": true
    }
  },
  "sandbox.order": {
    "props": {
      "width": "200px",
      "height": "60px",
      "initialContent": "<script>console.log('Current orderForm: ', window.props.orderForm)</script>",
      "allowCookies": true
    }
  },
  "sandbox#home": {
    "props": {
      "width": "200px",
      "height": "60px",
      "initialContent": "<h1 id='test'>home</h1><script>console.log(props, document.cookie); window.addEventListener('message', function(e){ console.log('got message in home', window.props) });</script>",
      "allowCookies": true
    }
  },
  "store.home": {
    "blocks": ["carousel#home", "shelf#home", "sandbox#home"]
  },
  "store.product": {
    "blocks": [
      "product-details#default",
      "sandbox#product"
    ]
  },
```
<!-- SCRAPED:END -->
