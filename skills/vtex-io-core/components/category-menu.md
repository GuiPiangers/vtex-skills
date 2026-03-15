<!-- SCRAPED:START -->
# Category Menu

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Navigation and search](</docs/guides/navigation-and-search>)

Category Menu

Official extension

Version: 2.18.1

Latest version: 2.18.1

![{"base64":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAABCAIAAAB2XpiaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAFUlEQVR4nGNgY2Mz1Nfll1L8f2MmAAvlA1rgBHAGAAAAAElFTkSuQmCC","img":{"src":"https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square","width":110,"height":20,"type":"svg"}}](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)

The Category Menu is a store component that displays a list of departments in a configurable menu layout. It helps organize and present categories and subcategories to improve navigation.

> An error occurred while loading the image https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/vtex-menu-0.png

## Configuration

  1. Add the app to your store theme's dependencies in the `manifest.json`.




```
dependencies: {
    "vtex.category-menu": "2.x"
  }
```


  2. Add the `category-menu` block to your store theme.




```
{
  "category-menu": {
    "props": {
      "showAllDepartments": true,
      "showSubcategories": true,
      "menuDisposition": "center",
      "departments": [],
      "sortSubcategories": "name"
    }
  }
}
```


### `category-menu` props

Prop name| Type| Description| Default Value  
---|---|---|---  
`showAllDepartments`| `Boolean`| Shows all department categories in the menu| `true`  
`menuDisposition`| `Enum`| Indicates the menu's position on the screen. Possible values: `left`, `center`, `right`| `center`  
`showSubcategories`| `Boolean`| Defines if the subcategories will be displayed| `true`  
`departments`| `Array(items)`| List of department `items` to be displayed on the menu| `[]`  
`mobileMode`| `Boolean`| Renders the category menu in a sidebar if set to `true`| `false`  
`sortSubcategories`| `Enum`| Determines how subcategories are sorted. Possible value: `name`|   
  
### `category-menu` items

Prop name| Type| Description  
---|---|---  
`id`| `Number`| The department ID to be displayed on the menu  
  
## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions on [Using CSS Handles for store customization](<https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization>).

CSS Handles  
---  
`container`  
`departmentLink`  
`departmentList`  
`firstLevelLink`  
`firstLevelLinkContainer`  
`firstLevelList`  
`itemContainer`  
`itemContainer--category`  
`itemContainer--department`  
`menuContainer`  
`secondLevelLink`  
`secondLevelLinkContainer`  
`secondLevelList`  
`section--category`  
`section--department`  
`sidebar`  
`sidebarContainer`  
`sidebarContent`  
`sidebarHeader`  
`sidebarItem`  
`sidebarItemContainer`  
`sidebarOpen`  
`sidebarScrim`  
`submenuItem`  
`submenuList`
<!-- SCRAPED:END -->
