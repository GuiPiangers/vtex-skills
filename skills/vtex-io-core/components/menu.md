<!-- SCRAPED:START -->
# Menu

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Navigation and search](</docs/guides/navigation-and-search>)

Menu

Official extension

Version: 2.35.3

Latest version: 2.35.3

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)

The Menu component displays a navigation bar with links and dropdown submenus. It can be configured to display internal or external links and supports both category-based and custom menu items.

![{"base64":"  ","img":{"width":2876,"height":1636,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":1421988,"url":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-menu-0.png"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-menu-0.png)

## Configuration

  1. Add the app to the store theme dependencies in the `manifest.json` file.




```
"dependencies": {
    "vtex.menu": "2.x"
  }
```


  2. Add the `vtex.menu@2.x:menu` block to the [store header](<https://github.com/vtex-apps/store-header/blob/master/store/interfaces.json>) template.

  3. Configure the `menu-item` blocks to build the store menu options. These can be declared in two ways in `vtex.menu@2.x:menu`: as children or as props. The advantage of the second type of `menu-item` configuration is that Site Editor can be used to edit the blocks.




### `menu-item` as children

_Example:_


```
"vtex.menu@2.x:menu#websites": {
  "children": [
    "menu-item#shop",
    "menu-item#about-us"
  ]
},
"menu-item#shop": {
  "props": {
    "id": "menu-item-shop",
    "type": "custom",
    "highlight": false,
    "itemProps": {
      "type": "internal",
      "href": "#",
      "noFollow": false,
      "tagTitle": "Shop",
      "text": "Shop"
    },
    "iconProps": {
      "id": "bnd-logo",
      "size": 16,
      "viewBox": "0 0 16 16",
      "activeClassName": "rebel-pink",
      "mutedClassName": "c-action-primary"
    },
    "iconToTheRight": true
  }
}
```


### `menu-item` as props

_Example:_


```
"vtex.menu@2.x:menu#websites": {
  "props": {
    "items": [
      {
        "id": "menu-item-shop",
        "type": "custom",
        "highlight": false,
        "itemProps": {
          "type": "internal",
          "href": "#",
          "noFollow": false,
          "tagTitle": "Shop",
          "text": "Shop"
        }
      },
      {
        "id": "menu-item-about-us",
        "type": "custom",
        "highlight": false,
        "itemProps": {
          "type": "internal",
          "href": "/about-us",
          "noFollow": false,
          "tagTitle": "about-us",
          "text": "About Us"
        }
      }
    ]
  }
}
```


### Adding a submenu

You can define a submenu by adding the `submenu` block to a `menu-item`:


```
"menu-item#shop": {
  "props": {
    "type": "custom",
    "highlight": false,
    "itemProps": {
      "type": "internal",
      "href": "#",
      "noFollow": false,
      "tagTitle": "Shop",
      "text": "Shop"
    },
  },
  "blocks": ["vtex.menu@2.x:submenu#shop"] // Defining a submenu
},
"vtex.menu@2.x:submenu#shop": {
  "children": [
    "vtex.menu@2.x:menu#submenushop"
  ]
},
"vtex.menu@2.x:menu#submenushop": {
  "children": [
    "menu-item#shop"
  ]
}
```


> The Menu block doesn't require any specific child blocks to work

## `menu-item` props

The available `menu-item` block props are:

Prop name| Type| Description| Default value  
---|---|---|---  
`type`| `string`| Menu item type, either `category` or `custom`| `category`  
`id`| `string`| Menu item ID| `undefined`  
`highlight`| `boolean`| Indicates whether the item has a highlight| `undefined`  
`iconPosition`| `string`| Icon position relative to the menu item text, either to the `left` or `right`| `left`  
`iconProps`| `IconProps`| Icon props| `undefined`  
`onMountBehavior`| `enum`| Indicates whether the submenu should always be automatically displayed when its parent is hovered/clicked on (`open`) or (`close`)| `closed`  
`itemProps`| `CategoryItem` or `CustomItem`| Item props| `undefined`  
`blockClass`| `CustomCSSClasses`| Used to override default CSS handles. To learn how this prop works, check this description of [useCustomClasses](<https://github.com/vtex-apps/css-handles#usecustomclasses>). Please note that this is only useful when importing this block as a React component.| `undefined`  
  
### Icon props

Prop name| Type| Description| Default value  
---|---|---|---  
`id`| `string`| Icon ID| N/A  
`isActive`| `boolean`| Indicates if the item is active| `true`  
`size`| `number`| Icon size| 16  
`viewBox`| `string`| Icon view box| `0 0 16 16`  
`activeClassName`| `string`| Icon classname when `isActive` is true| N/A  
`mutedClassName`| `string`| Icon classname when `isActive` is false| N/A  
  
### Category-specific props

Prop name| Type| Description| Default value  
---|---|---|---  
`categoryId`| `number`| Item category ID| N/A  
`text`| `string`| Menu item text| N/A  
  
### Custom item props

Prop name| Type| Description| Default value  
---|---|---|---  
`type`| `string`| Menu item type, either `internal` or `external`| `internal`  
`href`| `string`| Link to the menu item destination| N/A  
`noFollow`| `boolean`| No follow attribute| N/A  
`tagTitle`| `string`| Menu item tag| N/A  
`text`| `string`| Menu item text| N/A  
  
## Customization

To apply CSS customizations to this and other blocks, please follow the instructions in [Using CSS Handles for store customization](<https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization>).

CSS Handle  
---  
`accordionIcon--isClosed`  
`accordionIcon--isOpen`  
`accordionIcon`  
`container`  
`linkLeft`  
`linkMiddle`  
`linkRight`  
`menuContainerNav`  
`menuContainer`  
`menuItemInnerDiv`  
`menuItem`  
`menuItem--isOpen`  
`menuItem--isClosed`  
`menuLinkDivLeft`  
`menuLinkDivMiddle`  
`menuLinkDivRight`  
`menuLinkNav`  
`renderLink`  
`styledLinkContainer`  
`styledLinkContent`  
`styledLinkIcon`  
`styledLink`  
`submenuAccordion`  
`submenuColumn`  
`submenuContainer`  
`submenuWrapper--isClosed`  
`submenuWrapper--isOpen`  
`submenuWrapper`  
`submenu`
<!-- SCRAPED:END -->
