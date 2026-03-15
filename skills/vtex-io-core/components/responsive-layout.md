<!-- Manual content lives outside the SCRAPED markers. -->

<!-- SCRAPED:START -->
# Responsive Layout

[VTEX IO Apps](</docs/vtex-io-apps>)

Store Framework

[Layout and interaction patterns](</docs/guides/layout-and-interacion-patterns>)

Responsive Layout

Official extension

Version: 0.1.4

Latest version: 0.1.4

![{"base64":"  ","img":{"width":110,"height":20,"type":"svg","mime":"image/svg+xml","wUnits":"px","hUnits":"px","url":"https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square"}}](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)

Responsive Layout allows you to declare layout structures that will only be rendered in a specific screen-size breakpoint.

![{"base64":"  ","img":{"width":2840,"height":1428,"type":"gif","mime":"image/gif","wUnits":"px","hUnits":"px","length":1208072,"url":"https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-responsive-layout-0.gif"}}](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-responsive-layout-0.gif)

This app defines and exports four blocks:

  * `responsive-layout.desktop`
  * `responsive-layout.mobile`
  * `responsive-layout.tablet`
  * `responsive-layout.phone`



Each block has `composition: children`, which means that it expects to receive an array of `children` blocks for rendering if the current screen-size is right for its breakpoint.

## Configuration

  1. Import the Responsive Layout app to your theme dependencies in the `manifest.json`. For example:




```
"dependencies": {
    "vtex.responsive-layout": "0.x"
  }
```


  2. Add the `responsive-layout` block to your theme. For example:




```
"store.custom#about-us": {
    "blocks": [
      "responsive-layout.desktop",
      "responsive-layout.tablet",
      "responsive-layout.phone"
    ]
  },
  "responsive-layout.desktop": {
    "children": ["rich-text#desktop"]
  },
  "responsive-layout.tablet": {
    "children": ["rich-text#tablet"]
  },
  "responsive-layout.phone": {
    "children": ["rich-text#phone"]
  },
  "rich-text#desktop": {
    "props": {
      "text": "# This will only show up on desktop.",
      "blockClass": "title"
    }
  },
  "rich-text#tablet": {
    "props": {
      "text": "# This will only show up on tablet.",
      "blockClass": "title"
    }
  },
  "rich-text#phone": {
    "props": {
      "text": "# This will only show up on phone.",
      "blockClass": "title"
    }
  },
```


Note that you could use _any_ array of blocks as `children`, given that they are allowed by the `block` that is directly above `responsive-layout`.
<!-- SCRAPED:END -->

## Mandatory Team Rule: Avoid `responsive-layout.tablet`

Default to only two breakpoint trees:

- `responsive-layout.desktop` for desktop
- `responsive-layout.mobile` for mobile (phone + tablet)

Rationale: maintaining a separate tablet tree increases duplication and Site Editor maintenance cost (you end up editing the same content twice or three times).

## Recommended Structure (Desktop + Mobile)

```json
{
  "store.custom#about": {
    "blocks": ["responsive-layout.desktop#about", "responsive-layout.mobile#about"]
  },
  "responsive-layout.desktop#about": {
    "children": ["flex-layout.row#about-desktop"]
  },
  "responsive-layout.mobile#about": {
    "children": ["flex-layout.row#about-mobile"]
  }
}
```

## When to Split Phone vs Mobile

Only introduce `responsive-layout.phone` if there is a strict UX requirement that cannot be achieved by CSS/responsive-values (for example, completely different interaction models).

## Prefer CSS and Responsive Values When Possible

If the structure is the same and only spacing/typography changes, prefer:

- responsive CSS (media queries / responsive values)
- keeping the same block tree

Use Responsive Layout when you truly need different children blocks per breakpoint.

## Checklist

- Only `desktop` + `mobile` declared by default.
- No `responsive-layout.tablet` unless explicitly justified.
- Mobile tree is intentionally simpler when possible.

