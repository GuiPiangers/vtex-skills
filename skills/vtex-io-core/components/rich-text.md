<!-- SCRAPED:START -->
# Rich Text

[VTEX IO Apps](</docs/vtex-io-apps>)

Rich Text

Official extension

Version: 0.16.1

Latest version: 0.16.1

The Rich Text block converts text written in Markdown to HTML and displays it on your storefront.

![{"base64":"  ","img":{"width":1792,"height":1250,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":452544,"url":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-rich-text-0.png"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-rich-text-0.png)

For example, the following Markdown content


```
[Help](https://developers.vtex.com/vtex-developer-docs/docs/welcome).\n**Be Bold!**\n*This is italic*
```


would be rendered as


```
<div>
     <p>
        <a href="https://developers.vtex.com/">Help</a><br />
        <span class="b">Be Bold!</span><br />
        <span class="i">This is italic</span>
     </p>
</div>
```


Learn more in [Markdown documentation](<https://www.markdownguide.org/cheat-sheet/>).

## Configuration

  1. Add the `rich-text` app to your theme’s dependencies in the `manifest.json` file:




```
"dependencies": {
    "vtex.rich-text": "0.x"
  }
```


  2. Add the `rich-text` block to your block files in the desired template position. Example:




```
"rich-text": {
  "props": {
    "textAlignment": "CENTER",
    "textPosition": "CENTER",
    "text": "Visit our [help](https://developers.vtex.com/) section.\n**Be Bold!**\n*This is italic*",
    "textColor": "c-on-emphasis",
    "font": "t-heading-5",
    "blockClass": "help-message"
  }
}
```


## Props

Prop name| Type| Description  
---|---|---  
`blockClass`| `string`| Unique class name appended to block classes. Default: ''  
`font`| `string`| Tachyon token used as font. Default: `t-body`.  
`htmlId`| `String`| HTML ID of the element.  
`textColor`| `string`| Tachyon token used as text color. Default: `c-on-base`.  
`text`| `string`| Text written in Markdown.  
`textAlignment`| `TextAlignmentEnum`| Text alignment inside the component. Default: `"LEFT"`.  
`textPosition`| `TextPostionEnum`| Text position relative to the component. Default: `"LEFT"`.  
  
  * **`TextAlignmentEnum` possible values**

Enum name| Enum value| Description  
---|---|---  
Left| 'LEFT'| Aligns text to the left.  
Center| 'CENTER'| Aligns text to the center.  
Right| 'RIGHT'| Aligns text to the right.  
  
  * **`TextPostionEnum` possible values**

Enum name| Enum value| Description  
---|---|---  
Left| 'LEFT'| Positions content at the left of the component.  
Center| 'CENTER'| Positions content at the horizontal center of the component.  
Right| 'RIGHT'| Positions content at the right of the component.  
  
## Customization

To apply CSS customizations to this and other blocks, follow the guide [Using CSS handles for store customization](<https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization>).

CSS Handle  
---  
`container`  
`heading`  
`headingLevel1`  
`headingLevel2`  
`headingLevel3`  
`headingLevel4`  
`headingLevel5`  
`headingLevel6`  
`image`  
`italic`  
`link`  
`list`  
`listItem`  
`listOrdered`  
`paragraph`  
`strong`  
`table`  
`tableBody`  
`tableHead`  
`tableTd`  
`tableTh`  
`tableTr`  
`wrapper`
<!-- SCRAPED:END -->
