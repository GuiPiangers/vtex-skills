<!-- SCRAPED:START -->
# Video

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Product display](</docs/guides/product-display>)

Video

Official extension

Version: 1.4.3

Latest version: 1.4.3

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)

The Video app allows you to display video assets on your store pages.

![{"base64":"  ","img":{"width":1420,"height":854,"type":"png","mime":"image/png","wUnits":"px","hUnits":"px","length":1189801,"url":"https://storecomponents.vtexassets.com/arquivos/ids/155640"}}](https://storecomponents.vtexassets.com/arquivos/ids/155640)

## Configuration

  1. Add the `store-video` app to your theme's dependencies in the `manifest.json` file:




```
"dependencies ": {
+  "vtex.store-video": "1.x"
 }
```


  2. In any desired theme template, add the `video` block with the desirable props. For example:




```
"video#background": {
    "props": {
      "width": "100%",
      "height": "600px",
      "loop": false,
      "autoPlay": true,
      "muted": false,
      "src": "https://www.youtube.com/watch?v=wygFqZXMIco",
      "blockClass": "videoEl"
    }
  }
```


### `video` props

Prop name| Type| Description| Default value  
---|---|---|---  
`name`| `string`| Video name for SEO and accessibility.| `undefined`  
`description`| `string`| Video description for SEO and accessibility.| `undefined`  
`src`| `string`| Video URL. It can be a `youtube` URL, `vimeo` URL or a self-hosted video URL.| `undefined`  
`type`| `string`| Video type.| `undefined`  
`poster`| `string`| Cover image URL to be displayed before the video playback.| `undefined`  
`controlsType`| `enum`| The type of controls. It can be `custom-vtex`( only works if the video URL represents a HTML5 player ), `native` or `none`.| `undefined`  
`autoPlay`| `boolean`| Whether the video will start automatically after loaded(`true`) or not(`false`). Note that if the value is `true`, the muted property will automatically be setted to `true`.| `false`  
`muted`| `boolean`| Whether the video will start with the audio on(`false`) or not(`true`).| `false`  
`loop`| `boolean`| Whether the video will run in a loop(`true`) or not(`false`).| `false`  
`playsInline`| `boolean`| Whether the video will play inline(`true`) or not(`false`).| `false`  
`width`| `number` or `string`| The width of the video exhibition area. It could be as %(`string`) or pixels(`number`).| `undefined`  
`height`| `number` or `string`| The height of the video exhibition area. It could be as %(`string`) or pixels(`number`).| `undefined`  
`PlayIcon`| `string`| Video play icon for `custom-vtex` controls.| `icon-play`  
`PauseIcon`| `string`| Video pause icon for `custom-vtex` controls.| `icon-pause`  
`VolumeOnIcon`| `string`| Video volume on icon for `custom-vtex` controls.| `icon-volume-on`  
`VolumeOffIcon`| `string`| Video volume off icon for `custom-vtex` controls.| `icon-volume-off`  
`FullscreenIcon`| `string`| Video fullscreen icon for `custom-vtex` controls.| `icon-extend`  
`classes`| `CustomCSSClasses`| Used to override default CSS handles. To better understand how this prop works, we recommend reading about it here. Note that this is only useful if you're importing this block as a React component.| `undefined`  
  
Use the **admin's Site Editor** to manage some props declared in the `video` block.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](<https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization>).

CSS Handles  
---  
`controlsContainer`  
`fallbackContainer`  
`fallbackImage`  
`fullscreenButton`  
`playButton`  
`trackBar`  
`trackContainer`  
`trackTimer`  
`videoContainer`  
`videoElement`  
`volumeContainer`  
`volumeButton`  
`volumeSlider`  
  
:warning: _It's required that `controlsType` prop is set as `custom-vtex` in order to have the following CSS Handles properly working: `controlsContainer`, `fullscreenButton`, `playButton`, `trackContainer`, `trackTimer`, `trackBar`, `volumeContainer`, `volumeSlider`, and `volumeButton`.
<!-- SCRAPED:END -->
