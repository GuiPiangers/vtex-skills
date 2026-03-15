<!-- SCRAPED:START -->
# Drawer

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Navigation and search](</docs/guides/navigation-and-search>)

Drawer

Official extension

Version: 0.18.3

Latest version: 0.18.3

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)

The **Drawer** component is a sliding panel that displays additional options and menus when expanded. It is typically used in mobile layouts and responsive web designs where screen space is limited.

![{"base64":"  ","img":{"width":640,"height":1155,"type":"gif","mime":"image/gif","wUnits":"px","hUnits":"px","length":1858982,"url":"https://github-production-user-asset-6210df.s3.amazonaws.com/60782333/245488096-46358b77-e41a-4014-8443-c65cbe947fc2.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260315%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260315T102414Z&X-Amz-Expires=300&X-Amz-Signature=a0adfc80b530c8090546a588f60416653dcdfcb5b575985aef4af1b343b5d3fe&X-Amz-SignedHeaders=host"}}](https://github.com/vtex-apps/reviews-and-ratings/assets/60782333/46358b77-e41a-4014-8443-c65cbe947fc2)

When closed, the **Drawer** component is represented by an icon button positioned at the edge of the screen. Upon interaction, the drawer slides into view, revealing its content. Users can interact with the exposed content, perform actions, and navigate menus. To dismiss the drawer, users can either tap outside the drawer or use the close button.

## Configuration

  1. Open your store theme in the code editor of your preference.
  2. Open the `manifest.json` file and add the `vtex.store-drawer` app to your store theme dependencies as in the following:




```
"dependencies": {
  "vtex.store-drawer": "0.x"
}
```


  2. Add the `drawer` block to your app. The following example is from the [Store Theme](<https://github.com/vtex-apps/store-theme>).




```
"drawer": {
  "children": [
    "menu#drawer"
  ]
},
"menu#drawer": {
  "children": [
    "menu-item#category-clothing",
    "menu-item#category-decoration",
    "menu-item#custom-sale"
  ],
  "props": {
    "orientation": "vertical"
  }
},
```


  3. Use the `drawer-trigger` block to customize the icon that triggers the opening of the drawer as follows:




```
"drawer": {
  "children": [
    "menu#drawer"
  ],
  "blocks": ["drawer-trigger"]
},
"drawer-trigger": {
  "children": ["rich-text#open-drawer"]
},
"rich-text#open-drawer": {
  "props": {
    "text": "Open drawer"
  }
}
"menu#drawer": {
  "children": [
    "menu-item#category-clothing",
    "menu-item#category-decoration",
    "menu-item#custom-sale"
  ],
  "props": {
    "orientation": "vertical"
  }
},
```


  4. Use the `drawer-header` block to customize the header containing the button that closes the drawer. For example:




```
// blocks.json
{
  "drawer": {
    "blocks": ["drawer-header#my-drawer"]
  },
  "drawer-header#my-drawer": {
    "children": [
      // you need to include the block `drawer-close-button` somewhere inside here
      "flex-layout.row#something",
      // ...
      "drawer-close-button"
    ]
  }
}
```


### Using the Drawer as a standalone component

If you are using this component as a standalone module, you will need to import it into the specific component where you want to use it. For example:


```
import { Drawer, DrawerHeader, DrawerCloseButton } from "vtex.store-drawer";
const Menu = () => (
  <Drawer
    header={
      <DrawerHeader>
        <DrawerCloseButton />
      </DrawerHeader>
    }
  >
    <ul>
      <li>Link 1</li>
      <li>Link 2</li>
      <li>Link 3</li>
      <li>Link 4</li>
      <li>Link 5</li>
      <li>Link 6</li>
    </ul>
  </Drawer>
);
```


### Props

#### `drawer`

Prop name| Type| Description| Default value  
---|---|---|---  
`maxWidth`| `number` or `string`| Defines the maximum width of the open drawer.| `450`  
`isFullWidth`| `boolean`| Controls whether the open drawer should occupy the full available width.| `false`  
`slideDirection`| `'horizontal'`|`'vertical'`|`'rightToLeft'`|`'leftToRight'`| Controls the direction of the opening animation for the drawer.| `'horizontal'`  
`backdropMode`| `'default'`|`'none'`| Controls whether the backdrop should be displayed when the drawer is open.|   
`renderingStrategy`| `'lazy'`|`'eager'`| Controls the rendering strategy for the children of the drawer component. It determines whether the children should be rendered only when the drawer is clicked (`lazy`) or immediately when the page loads (`eager`). Enabling the `eager` strategy may improve SEO performance. However, it may also result in slower page rendering.| `'lazy'`  
`customPixelEventId`| `string`| Defines the store event ID responsible for triggering the `drawer` to automatically open on the interface.| `undefined`  
`customPixelEventName`| `string`| Defines the store event name responsible for triggering the `drawer` to automatically open on the interface. Some examples are: `'addToCart'` and `'removeFromCart'` events. Note that if no `customPixelEventId` is set, using this prop will cause the drawer to open in every event with the specified name.| `undefined`  
  
#### `drawer-close-button`

Prop name| Type| Description| Default value  
---|---|---|---  
`size`| `number`| Defines the size of the icon inside the button.| `30`  
`type`| `'filled'`|`'line'`| Defines the type of the icon.| `'line'`  
`text`| `string`| Defines the text inside the button. The icon will not be rendered if `text` is defined.| `undefined`  
  
#### `drawer-trigger`

Prop name| Type| Description| Default value  
---|---|---|---  
`customPixelEventId`| `string`| Defines the event ID to be sent whenever users interact with the Drawer component.| `undefined`  
  
## Customization

In order to apply CSS customizations to this and other blocks, follow the instructions in [Using CSS handles for store customizations](<https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization>).

CSS handles  
---  
`drawer`  
`opened`  
`overlay`  
`overlay--visible`  
`closed`  
`moving`  
`drawerContent`  
`drawerHeader`  
`drawerTriggerContainer`  
`openIconContainer`  
`closeIconContainer`  
`closeIconButton`  
`childrenContainer`
<!-- SCRAPED:END -->
