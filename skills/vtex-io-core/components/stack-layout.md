<!-- SCRAPED:START -->
# Stack Layout

Use this layout component to show blocks on top of other blocks.

![](https://user-images.githubusercontent.com/27777263/70265324-e55fda00-1778-11ea-8d56-e73e3848b0b3.png)

Each child passed to `stack-layout` will receive an increasingly higher value of `zIndex`.

This means `flex-layout.row#viewone` will appear on the bottom, `flex-layout.row#viewtwo` will appear over it with `zIndex` of value 2, and `flex-layout.row#viewthree` will appear over them both with `zIndex` of value 3. Another thing to notice is that if you pass the `blockClass` prop to any children of the `stack-layout`, it will apply the `blockClass` to the element that wraps the child element.

## Configuration

1. Import the Stack Layout app to your theme's dependencies to the `manifest.json`:

```json
  "dependencies": {
    "vtex.stack-layout": "0.x"
  }
```

2. Add the `stack-layout` block to the desired template. For example:

```json
"stack-layout": {
  "children": ["flex-layout.row#viewone", "flex-layout.row#viewtwo", "flex-layout.row#viewthree]
}
```

| Prop name      | Type     | Description                                                                                                                                                                            | Default value |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass`   | `string` | Allows to pass a custom name to be added to component CSS classes.                                                                                                                      | `null`        |
| `zIndexOffset` | `number` | An offset to be passed to the zIndex of the children of the stack layout. If you pass `3`, the first children will have `zIndex` of 3, and the next layer will have `zIndex` of 4, and so on. | `0`           |
| `arialabel` | `string` | A value to customize the aria-label property | `null`           |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization). 

| CSS Handles       |
| ------------------|
| `stackContainer`  |
| `stackItem`       |
| `stackItem--first`|
<!-- SCRAPED:END -->
