# Runtime Context Guide

> **Hook:** `useRuntime()`  
> **Purpose:** Access route, query params, navigation, account/workspace context and device info  
> **Package:** `vtex.render-runtime`

---

## Setup

Run the following to add typings to your app (enables IDE autocomplete):

```bash
vtex setup --typings
```

---

## `useRuntime()` — Full Return Type

```tsx
import { useRuntime } from 'vtex.render-runtime'

interface RenderContext {
  account: string
  binding: BindingInfo
  culture: Culture
  deviceInfo: DeviceInfo
  getSettings: (appId: string) => Record<string, any>
  hints: Hints
  history: History                // from the `history` package v4
  navigate: (options: NavigateOptions) => void
  page: string
  pages: Record<string, PageInfo>
  production: boolean
  query: Record<string, string>
  renderMajor: number
  rootPath: string | undefined
  route: Route
  setQuery: (params: Record<string, string>) => void
  workspace: string
}
```

---

## Fields Reference

### `account` — `string`
The VTEX account name.

```tsx
const { account } = useRuntime()
// e.g. "storecomponents"
```

---

### `binding` — `BindingInfo`
Store binding data — useful in multi-binding (multi-store/multi-language) setups.

```tsx
interface BindingInfo {
  id: string
  canonicalBaseAddress: string
}

const { binding } = useRuntime()
// { id: "aacb06b3-a8fa-4bab-b5bd-2d654d20dcd8", canonicalBaseAddress: "storetheme.vtex.com/" }
```

---

### `culture` — `Culture`
Current locale, currency and country info. Use for formatting prices, dates and translations.

```tsx
interface Culture {
  availableLocales: string[]
  country: string
  currency: string
  language: string
  locale: string
  customCurrencyDecimalDigits: number | null
  customCurrencySymbol: string | null
}

const { culture } = useRuntime()
// { country: "USA", currency: "USD", language: "en", locale: "en-US", ... }
```

---

### `deviceInfo` — `DeviceInfo`
⚡ **Dynamic** — updates when the user resizes the window. Use for responsive rendering logic.

```tsx
interface DeviceInfo {
  isMobile: boolean
  type: 'phone' | 'tablet' | 'desktop' | 'unknown'
}

const { deviceInfo } = useRuntime()
// { isMobile: false, type: "desktop" }
```

---

### `hints` — `Hints`
📦 **Static** — based on CDN/server-side detection. Does **not** update on window resize.  
Use for SSR-safe device detection (e.g. serving different HTML on mobile vs desktop).

```tsx
interface Hints {
  desktop: boolean
  mobile: boolean
  tablet: boolean
  phone: boolean
  unknown: boolean
}

const { hints } = useRuntime()
// { desktop: true, mobile: false, tablet: false, phone: false, unknown: false }
```

> **`deviceInfo` vs `hints`:** Use `deviceInfo` for client-side responsive logic (updates on resize). Use `hints` for SSR-safe rendering decisions (static, set by CDN).

---

### `getSettings` — `(appId: string) => Record<string, any>`
Returns the public settings of any installed app. Useful for reading app-level configurations.

```tsx
const { getSettings } = useRuntime()
const storeSettings = getSettings('vtex.store')
// e.g. { storeName: "My Store", titleTag: "My Store", ... }
```

---

### `navigate` — `(options: NavigateOptions) => void`
Client-side programmatic navigation. Use when you need to navigate based on logic (e.g. form submission, conditional redirect).

```tsx
interface NavigateOptions {
  to?: string                  // Full URL path (e.g. '/product/p')
  page?: string                // Block page id (e.g. 'store.product')
  params?: Record<string, any> // Route params
  query?: Record<string, any>  // Query string params
  replace?: boolean            // Replace history entry instead of push
  hash?: string                // URL hash
  rootPath?: string
  scrollOptions?: false | {
    baseElementId: string
    behavior: 'auto' | 'smooth'
    left: number
    top: number
  }
  fallbackToWindowLocation?: boolean
  skipSetPath?: boolean
}

const { navigate } = useRuntime()

// Navigate to a path
navigate({ to: '/other-page' })

// Navigate to a page with params
navigate({ page: 'store.product', params: { slug: 'my-product' } })

// Replace current history entry (no back button entry)
navigate({ to: '/checkout', replace: true })
```

> **Prefer `<Link>` over `navigate`** for anchor-like navigation — it handles SSR correctly and supports standard browser behavior. Use `navigate` only when navigation depends on logic.

---

### `history` — `History` (from `history` v4)
Direct access to the browser history object. Use for advanced navigation (e.g. `goBack()`).

```tsx
const { history } = useRuntime()

history.goBack()
history.push('/other-page')
```

---

### `setQuery` — `(params: Record<string, string>) => void`
Updates the current URL query string without full navigation. Useful for filters, pagination, and tab state.

```tsx
const { setQuery } = useRuntime()

// Adds/updates ?tab=reviews in the URL
setQuery({ tab: 'reviews' })
```

---

### `page` — `string`
The current page block id.

```tsx
const { page } = useRuntime()
// e.g. "store.home", "store.product", "store.search"
```

---

### `pages` — `Record<string, PageInfo>`
Map of all registered pages. Keys are page ids.

```tsx
interface PageInfo {
  allowConditions: boolean
  context: string | null
  declarer: string
  path: string
  routeId: string
  blockId: string
  map: string[]
}

const { pages, page } = useRuntime()
const currentPageInfo = pages[page]
// { declarer: "vtex.store@2.x", path: "/", routeId: "store.home", ... }
```

---

### `route` — `Route`
Full data about the current route including path, params, query and stylesheet info.

```tsx
const { route } = useRuntime()

// Commonly used fields:
route.id           // "store.home"
route.path         // "/search?q=shoes"
route.params       // { slug: "my-product" }  — for dynamic routes
route.queryString  // { q: "shoes", map: "ft" }
route.pageContext  // { id: "store.home", type: "route" }
route.canonicalPath // "/"
route.ssr          // true
```

---

### `production` — `boolean`
`true` if running in the production workspace (`master`), `false` otherwise. Use to gate debug info or dev-only features.

```tsx
const { production } = useRuntime()

if (!production) {
  console.debug('Debug info:', someData)
}
```

---

### `workspace` — `string`
Current workspace name. `"master"` in production.

```tsx
const { workspace } = useRuntime()
// "master" | "myworkspace"
```

---

### `rootPath` — `string | undefined`
The store root path, set when the store runs under a subpath (e.g. `/ar` for Arabic binding). `undefined` if not configured.

```tsx
const { rootPath } = useRuntime()
// "/ar" | undefined
```

---

### `renderMajor` — `number`
The major version of `vtex.render-runtime` currently running.

```tsx
const { renderMajor } = useRuntime()
// 8
```

---

## Other Exports

### `canUseDOM` — `boolean`
`true` in browser, `false` in SSR/Node. Use to safely access `window` and `document`.

```tsx
import { canUseDOM } from 'vtex.render-runtime'

const value = canUseDOM
  ? window.localStorage.getItem('foo')
  : ''
```

> **Prefer `canUseDOM` over `typeof window !== 'undefined'`** — it's the VTEX-idiomatic check and works correctly with SSR hydration.

---

### `<Link>` Component
Renders an `<a>` tag with VTEX IO-aware navigation. Preferred over `navigate` for standard links.

```tsx
import { Link } from 'vtex.render-runtime'

// Navigate by path
<Link to="/other-page" className="c-on-base">Go</Link>

// Navigate by page id with params
<Link page="store.product" params={{ slug: 'my-product' }}>Product</Link>
```

| Prop | Type | Description |
|---|---|---|
| `to` | `string` | Full URL path |
| `page` | `string` | Block page id (alternative to `to`) |
| `params` | `object` | Route params. Keys starting with `__` are ignored in path transformations |
| `query` | `string` | Query string (e.g. `"skuId=231"`) |
| `replace` | `boolean` | Replace history entry instead of push |
| `onClick` | `function` | Click callback |

---

### `<ExtensionPoint>` / `<Block>` Component
Injects a block by id. Use in custom components with `blocks` composition.

```tsx
import { ExtensionPoint } from 'vtex.render-runtime'
// or: import { Block } from 'vtex.render-runtime'

const MyComponent = () => (
  <div>
    <ExtensionPoint id="my-other-block" />
  </div>
)
```

> Prefer `Slot` composition over `ExtensionPoint` when possible — it's simpler and doesn't require `allowed` in `interfaces.json`.

---

### `<NoSSR>` Component
Prevents its children from rendering during SSR. Use when a component depends on `window` or `document`.

```tsx
import { NoSSR } from 'vtex.render-runtime'

const MyComponent = () => (
  <NoSSR onSSR={<div>Loading...</div>}>
    <DomRelatedComponent />
  </NoSSR>
)
```

> **Prefer `canUseDOM`** for simple checks. Use `<NoSSR>` only when the entire subtree must be excluded from SSR.

---

### `<Helmet>` Component
Injects tags into the `<head>` of the page. Re-export of `react-helmet`.

```tsx
import { Helmet } from 'vtex.render-runtime'

const MyComponent = () => (
  <Helmet>
    <meta property="og:type" content="article" />
    <title>My Page</title>
  </Helmet>
)
```

---

### `withRuntimeContext` HOC
For **class components** that need runtime context. Use `useRuntime()` in function components instead.

```tsx
import { withRuntimeContext, RenderContext } from 'vtex.render-runtime'

class MyComponent extends React.Component<{ runtime: RenderContext }> {
  render() {
    return <div>{this.props.runtime.page}</div>
  }
}

export default withRuntimeContext(MyComponent)
```

---

## `manifest.json` Dependency

```json
{
  "dependencies": {
    "vtex.render-runtime": "8.x"
  }
}
```

---

## Practical Rules

```
✓ Use canUseDOM before accessing window/document
✓ Use deviceInfo for client-side responsive logic (updates on resize)
✓ Use hints for SSR-safe device detection (static, set by CDN)
✓ Use <Link> for standard anchor navigation
✓ Use navigate() only when navigation depends on runtime logic
✓ Use setQuery() for filter/pagination state in the URL
✓ Use production flag to gate debug-only code
✗ Never access window/document directly without canUseDOM guard
✗ Don't use withRuntimeContext in function components — use useRuntime()
✗ Don't use <NoSSR> when canUseDOM check is sufficient
```