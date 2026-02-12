# Product Context Guide

> **Hooks:** `useProduct()` / `useProductDispatch()`  
> **Purpose:** Access and manipulate product data in VTEX IO components  
> **Package:** `vtex.product-context`

---

## 🎯 CORE CONCEPT

Product Context provides two hooks:
- **`useProduct()`** - Read product data (state)
- **`useProductDispatch()`** - Modify product data (dispatch actions)

**Available on:** Product Detail Page (PDP), Product Summary (shelves, search results)

---

## 📦 INSTALLATION

### Add Dependency

**manifest.json:**
```json
{
  "dependencies": {
    "vtex.product-context": "0.x"
  }
}
```

---

## 🔍 useProduct() - Read Product Data

### Basic Usage

```tsx
import { useProduct } from 'vtex.product-context'

const MyComponent = () => {
  const productContext = useProduct()
  
  if (!productContext) {
    return <div>Loading...</div>
  }
  
  const { product, selectedItem, selectedQuantity } = productContext
  
  return (
    <div>
      <h1>{product.productName}</h1>
      <p>Price: ${selectedItem.sellers[0].commertialOffer.Price}</p>
    </div>
  )
}
```

### Return Type

```tsx
{
  product: Product | null
  selectedItem: Item | null
  selectedQuantity: number
  skuSelector: {
    selectedImageVariationSKU: string | null
    isVisible: boolean
    areAllVariationsSelected: boolean
  }
  buyButton: {
    clicked: boolean
  }
  assemblyOptions: {
    items: Record<string, AssemblyOptionItem[]>
    inputValues: Record<string, InputValues>
    areGroupsValid: Record<string, boolean>
  }
}
```

---

## 📊 PRODUCT DATA STRUCTURE

### Product Object

```tsx
product: {
  productId: string
  productName: string
  brand: string
  brandId: number
  description: string
  linkText: string
  productReference: string
  categoryId: string
  categoryTree: Array<{
    id: string
    name: string
    href: string
  }>
  items: Item[]
  properties: Array<{
    name: string
    values: string[]
  }>
  recommendations: {
    buy?: Product[]
    view?: Product[]
  }
  productClusters: Array<{
    id: string
    name: string
  }>
  clusterHighlights: Array<{
    id: string
    name: string
  }>
  priceRange: {
    sellingPrice: {
      highPrice: number
      lowPrice: number
    }
    listPrice: {
      highPrice: number
      lowPrice: number
    }
  }
}
```

### Item (SKU) Object

```tsx
selectedItem: {
  itemId: string
  name: string
  nameComplete: string
  complementName: string
  ean: string
  referenceId: Array<{
    Key: string
    Value: string
  }>
  images: Array<{
    imageId: string
    imageLabel: string
    imageTag: string
    imageUrl: string
    imageText: string
  }>
  sellers: Array<{
    sellerId: string
    sellerName: string
    addToCartLink: string
    sellerDefault: boolean
    commertialOffer: {
      Price: number
      ListPrice: number
      PriceWithoutDiscount: number
      AvailableQuantity: number
      spotPrice: number
      taxPercentage: number
      teasers: Array<{
        name: string
        conditions: {
          minimumQuantity: number
          parameters: Array<{
            name: string
            value: string
          }>
        }
        effects: {
          parameters: Array<{
            name: string
            value: string
          }>
        }
      }>
    }
  }>
  variations: Array<{
    name: string
    values: string[]
  }>
  attachments: Array<{
    id: number
    name: string
    required: boolean
    domainValues: Array<{
      FieldName: string
      MaxCaracters: string
      DomainValues: string[]
    }>
  }>
}
```

---

## ⚡ useProductDispatch() - Modify Product Data

### Basic Usage

```tsx
import { useProductDispatch } from 'vtex.product-context'

const MyComponent = () => {
  const dispatch = useProductDispatch()
  
  const handleSelectSKU = (skuId: string) => {
    dispatch({
      type: 'SET_SELECTED_ITEM',
      args: { item: skuId }
    })
  }
  
  return <button onClick={() => handleSelectSKU('123')}>Select SKU</button>
}
```

---

## 🎬 DISPATCH ACTIONS

### 1. SET_SELECTED_ITEM

Select a specific SKU.

```tsx
dispatch({
  type: 'SET_SELECTED_ITEM',
  args: {
    item: Item // Complete Item object, not just ID
  }
})
```

**Example:**
```tsx
const selectSKU = (itemId: string) => {
  const selectedItem = product?.items.find(item => item.itemId === itemId)
  
  if (selectedItem) {
    dispatch({
      type: 'SET_SELECTED_ITEM',
      args: { item: selectedItem }
    })
  }
}

// Or select by variation
const selectByColor = (color: string) => {
  const item = product?.items.find(item => 
    item.variations?.some(v => 
      v.name === 'Color' && v.values.includes(color)
    )
  )
  
  if (item) {
    dispatch({
      type: 'SET_SELECTED_ITEM',
      args: { item }
    })
  }
}
```

---

### 2. SET_QUANTITY

Change selected quantity.

```tsx
dispatch({
  type: 'SET_QUANTITY',
  args: {
    quantity: number
  }
})
```

**Example:**
```tsx
const increaseQuantity = () => {
  const currentQuantity = productContext?.selectedQuantity || 1
  dispatch({
    type: 'SET_QUANTITY',
    args: { quantity: currentQuantity + 1 }
  })
}
```

---

### 3. SKU_SELECTOR_SET_VARIATIONS_SELECTED

Set specific variation values (color, size, etc.).

**Note:** This action sets variation selections but doesn't directly select the item. Use `SET_SELECTED_ITEM` with the complete Item object for direct SKU selection.

```tsx
dispatch({
  type: 'SKU_SELECTOR_SET_VARIATIONS_SELECTED',
  args: {
    variationsSelected: {
      [variationName]: variationValue
    }
  }
})
```

**Example:**
```tsx
const selectColor = (color: string) => {
  dispatch({
    type: 'SKU_SELECTOR_SET_VARIATIONS_SELECTED',
    args: {
      variationsSelected: {
        'Color': color
      }
    }
  })
}

const selectSize = (size: string) => {
  dispatch({
    type: 'SKU_SELECTOR_SET_VARIATIONS_SELECTED',
    args: {
      variationsSelected: {
        'Size': size
      }
    }
  })
}

// Select multiple variations at once
const selectVariations = () => {
  dispatch({
    type: 'SKU_SELECTOR_SET_VARIATIONS_SELECTED',
    args: {
      variationsSelected: {
        'Color': 'Red',
        'Size': 'M'
      }
    }
  })
}
```

**Best Practice:** For direct item selection based on variation, use `SET_SELECTED_ITEM` with the filtered item instead:

```tsx
// More direct approach
const selectByColor = (color: string) => {
  const item = product?.items.find(item => 
    item.variations?.some(v => 
      v.name === 'Color' && v.values.includes(color)
    )
  )
  
  if (item) {
    dispatch({
      type: 'SET_SELECTED_ITEM',
      args: { item }
    })
  }
}
```

---

### 4. SKU_SELECTOR_SET_IS_VISIBLE

Show/hide SKU selector.

```tsx
dispatch({
  type: 'SKU_SELECTOR_SET_IS_VISIBLE',
  args: {
    isVisible: boolean
  }
})
```

**Example:**
```tsx
const toggleSKUSelector = () => {
  const isCurrentlyVisible = productContext?.skuSelector.isVisible
  dispatch({
    type: 'SKU_SELECTOR_SET_IS_VISIBLE',
    args: { isVisible: !isCurrentlyVisible }
  })
}
```

---

### 5. SET_BUY_BUTTON_CLICKED

Mark buy button as clicked.

```tsx
dispatch({
  type: 'SET_BUY_BUTTON_CLICKED',
  args: {
    clicked: boolean
  }
})
```

**Example:**
```tsx
const handleAddToCart = () => {
  dispatch({
    type: 'SET_BUY_BUTTON_CLICKED',
    args: { clicked: true }
  })
  
  // Add to cart logic here
}
```

---

### 6. SET_PRODUCT

Replace entire product data.

```tsx
dispatch({
  type: 'SET_PRODUCT',
  args: {
    product: Product
  }
})
```

**Example:**
```tsx
const loadNewProduct = async (productId: string) => {
  const newProduct = await fetchProduct(productId)
  
  dispatch({
    type: 'SET_PRODUCT',
    args: { product: newProduct }
  })
}
```

---

### 7. SKU_SELECTOR_SET_IMAGE_VARIATION

Set which variation controls image changes.

```tsx
dispatch({
  type: 'SKU_SELECTOR_SET_IMAGE_VARIATION',
  args: {
    variationName: string | null
  }
})
```

**Example:**
```tsx
const setImageVariation = () => {
  dispatch({
    type: 'SKU_SELECTOR_SET_IMAGE_VARIATION',
    args: { variationName: 'Color' }
  })
}
```

---

### 8. SET_ASSEMBLY_OPTIONS

Update assembly options (customization, attachments).

```tsx
dispatch({
  type: 'SET_ASSEMBLY_OPTIONS',
  args: {
    groupId: string
    groupItems: AssemblyOptionItem[]
  }
})
```

**Example:**
```tsx
const updateAssembly = () => {
  dispatch({
    type: 'SET_ASSEMBLY_OPTIONS',
    args: {
      groupId: 'customization-group-1',
      groupItems: [
        {
          id: 'item-1',
          quantity: 1,
          seller: '1',
          initialQuantity: 0,
          choiceType: 'SINGLE',
          name: 'Extra cheese',
          price: 200,
          children: null
        }
      ]
    }
  })
}
```

---

### 9. SET_ASSEMBLY_OPTIONS_INPUT_VALUES

Set input values for assembly options.

```tsx
dispatch({
  type: 'SET_ASSEMBLY_OPTIONS_INPUT_VALUES',
  args: {
    groupId: string
    inputValues: Record<string, string>
  }
})
```

**Example:**
```tsx
const setCustomMessage = (message: string) => {
  dispatch({
    type: 'SET_ASSEMBLY_OPTIONS_INPUT_VALUES',
    args: {
      groupId: 'message-group',
      inputValues: {
        'customMessage': message
      }
    }
  })
}
```

---

### 10. SET_ASSEMBLY_OPTIONS_GROUP_VALIDITY

Set validity state for assembly option groups.

```tsx
dispatch({
  type: 'SET_ASSEMBLY_OPTIONS_GROUP_VALIDITY',
  args: {
    groupId: string
    validity: boolean
  }
})
```

**Example:**
```tsx
const validateAssemblyGroup = (groupId: string, isValid: boolean) => {
  dispatch({
    type: 'SET_ASSEMBLY_OPTIONS_GROUP_VALIDITY',
    args: {
      groupId,
      validity: isValid
    }
  })
}
```

---

## 💡 PRACTICAL EXAMPLES

### Example 1: Product Info Display

```tsx
import React from 'react'
import { useProduct } from 'vtex.product-context'

const ProductInfo = () => {
  const productContext = useProduct()
  
  if (!productContext?.product) {
    return <div>Product not found</div>
  }
  
  const { product, selectedItem } = productContext
  const offer = selectedItem?.sellers[0]?.commertialOffer
  
  return (
    <div>
      <h1>{product.productName}</h1>
      <p>{product.brand}</p>
      
      {offer && (
        <>
          <p className="price">${offer.Price.toFixed(2)}</p>
          {offer.ListPrice > offer.Price && (
            <p className="old-price">${offer.ListPrice.toFixed(2)}</p>
          )}
          <p>Available: {offer.AvailableQuantity}</p>
        </>
      )}
    </div>
  )
}

export default ProductInfo
```

---

### Example 2: Custom Quantity Selector

```tsx
import React from 'react'
import { useProduct, useProductDispatch } from 'vtex.product-context'

const QuantitySelector = () => {
  const productContext = useProduct()
  const dispatch = useProductDispatch()
  
  const quantity = productContext?.selectedQuantity || 1
  const maxQuantity = productContext?.selectedItem?.sellers[0]?.commertialOffer.AvailableQuantity || 10
  
  const handleIncrease = () => {
    if (quantity < maxQuantity) {
      dispatch({
        type: 'SET_QUANTITY',
        args: { quantity: quantity + 1 }
      })
    }
  }
  
  const handleDecrease = () => {
    if (quantity > 1) {
      dispatch({
        type: 'SET_QUANTITY',
        args: { quantity: quantity - 1 }
      })
    }
  }
  
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value, 10)
    if (value >= 1 && value <= maxQuantity) {
      dispatch({
        type: 'SET_QUANTITY',
        args: { quantity: value }
      })
    }
  }
  
  return (
    <div className="quantity-selector">
      <button onClick={handleDecrease} disabled={quantity <= 1}>
        -
      </button>
      <input 
        type="number" 
        value={quantity} 
        onChange={handleChange}
        min="1"
        max={maxQuantity}
      />
      <button onClick={handleIncrease} disabled={quantity >= maxQuantity}>
        +
      </button>
    </div>
  )
}

export default QuantitySelector
```

---

### Example 3: Custom SKU Selector

```tsx
import React from 'react'
import { useProduct, useProductDispatch } from 'vtex.product-context'

const SKUSelector = () => {
  const productContext = useProduct()
  const dispatch = useProductDispatch()
  
  if (!productContext?.product) return null
  
  const { product, selectedItem } = productContext
  
  const handleSelectSKU = (item: Item) => {
    dispatch({
      type: 'SET_SELECTED_ITEM',
      args: { item }
    })
  }
  
  return (
    <div className="sku-selector">
      {product.items.map((item) => (
        <button
          key={item.itemId}
          onClick={() => handleSelectSKU(item)}
          className={selectedItem?.itemId === item.itemId ? 'active' : ''}
        >
          {item.name}
        </button>
      ))}
    </div>
  )
}

export default SKUSelector
```

---

### Example 4: Color Variation Selector

```tsx
import React from 'react'
import { useProduct, useProductDispatch } from 'vtex.product-context'
import type { Item } from 'vtex.product-context'

// Helper function to filter items by variation value
const filterItemsByVariationValue = (
  items: Item[] | undefined,
  variationName: string,
  value: string
): Item[] | undefined => {
  return items?.filter(item =>
    item.variations?.some(v =>
      v.name === variationName && v.values.includes(value)
    )
  )
}

const ColorSelector = () => {
  const productContext = useProduct()
  const dispatch = useProductDispatch()
  
  if (!productContext?.product) return null
  
  const { product } = productContext
  
  // Extract unique color values from all items
  const colorVariation = product.items[0]?.variations?.find(
    v => v.name === 'Color'
  )
  
  if (!colorVariation) return null
  
  const handleColorSelect = (color: string) => {
    // Find first item matching this color
    const matchingItem = filterItemsByVariationValue(
      product.items,
      'Color',
      color
    )?.[0]
    
    if (matchingItem) {
      dispatch({
        type: 'SET_SELECTED_ITEM',
        args: { item: matchingItem }
      })
    }
  }
  
  return (
    <div className="color-selector">
      <h3>Color:</h3>
      <div className="color-options">
        {colorVariation.values.map((color) => (
          <button
            key={color}
            onClick={() => handleColorSelect(color)}
            className="color-option"
            title={color}
          >
            {color}
          </button>
        ))}
      </div>
    </div>
  )
}

export default ColorSelector
```

---

### Example 5: Size Variation Selector

```tsx
import React from 'react'
import { useProduct, useProductDispatch } from 'vtex.product-context'

const SizeSelector = () => {
  const productContext = useProduct()
  const dispatch = useProductDispatch()
  
  if (!productContext?.product) return null
  
  const { product } = productContext
  
  const sizeVariation = product.items[0]?.variations?.find(
    v => v.name === 'Size'
  )
  
  if (!sizeVariation) return null
  
  const handleSizeSelect = (size: string) => {
    dispatch({
      type: 'SKU_SELECTOR_SET_VARIATIONS_SELECTED',
      args: {
        variationsSelected: {
          'Size': size
        }
      }
    })
  }
  
  return (
    <div className="size-selector">
      <h3>Size:</h3>
      <div className="size-options">
        {sizeVariation.values.map((size) => (
          <button
            key={size}
            onClick={() => handleSizeSelect(size)}
            className="size-option"
          >
            {size}
          </button>
        ))}
      </div>
    </div>
  )
}

export default SizeSelector
```

---

### Example 6: Discount Calculator

```tsx
import React from 'react'
import { useProduct } from 'vtex.product-context'

const DiscountBadge = () => {
  const productContext = useProduct()
  
  if (!productContext?.selectedItem) return null
  
  const offer = productContext.selectedItem.sellers[0]?.commertialOffer
  
  if (!offer || offer.ListPrice <= offer.Price) return null
  
  const discountPercentage = Math.round(
    ((offer.ListPrice - offer.Price) / offer.ListPrice) * 100
  )
  
  return (
    <div className="discount-badge">
      <span>-{discountPercentage}%</span>
    </div>
  )
}

export default DiscountBadge
```

---

### Example 7: Stock Availability

```tsx
import React from 'react'
import { useProduct } from 'vtex.product-context'

const StockStatus = () => {
  const productContext = useProduct()
  
  if (!productContext?.selectedItem) return null
  
  const stock = productContext.selectedItem.sellers[0]?.commertialOffer.AvailableQuantity
  
  const getStockStatus = () => {
    if (stock === 0) return { text: 'Out of stock', className: 'out-of-stock' }
    if (stock < 5) return { text: `Only ${stock} left!`, className: 'low-stock' }
    return { text: 'In stock', className: 'in-stock' }
  }
  
  const status = getStockStatus()
  
  return (
    <div className={`stock-status ${status.className}`}>
      {status.text}
    </div>
  )
}

export default StockStatus
```

---

### Example 8: Combined Variation Selector

```tsx
import React from 'react'
import { useProduct, useProductDispatch } from 'vtex.product-context'

const VariationSelector = () => {
  const productContext = useProduct()
  const dispatch = useProductDispatch()
  
  if (!productContext?.product) return null
  
  const { product } = productContext
  const firstItem = product.items[0]
  
  if (!firstItem?.variations) return null
  
  const handleVariationChange = (variationName: string, value: string) => {
    dispatch({
      type: 'SKU_SELECTOR_SET_VARIATIONS_SELECTED',
      args: {
        variationsSelected: {
          [variationName]: value
        }
      }
    })
  }
  
  return (
    <div className="variation-selector">
      {firstItem.variations.map((variation) => (
        <div key={variation.name} className="variation-group">
          <h3>{variation.name}:</h3>
          <div className="variation-options">
            {variation.values.map((value) => (
              <button
                key={value}
                onClick={() => handleVariationChange(variation.name, value)}
                className="variation-option"
              >
                {value}
              </button>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

export default VariationSelector
```

---

## 🚦 BEST PRACTICES

```
✓ Always check if productContext exists before use
✓ Handle null/undefined cases for product and selectedItem
✓ Use TypeScript for type safety
✓ Dispatch actions in response to user interactions
✓ Keep components focused (single responsibility)
✓ Use selectedItem for current SKU data
✓ Access price from selectedItem.sellers[0].commertialOffer
✓ Validate quantity against AvailableQuantity
```

---

## 🚫 ANTI-PATTERNS

```
❌ Don't assume productContext always exists
❌ Don't mutate productContext directly
❌ Don't dispatch actions without user interaction
❌ Don't access nested properties without null checks
❌ Don't use product.items[0] when selectedItem exists
❌ Don't forget to add vtex.product-context dependency
```

---

## 📋 COMMON USE CASES

| Use Case | Hook | Action/Property |
|----------|------|--------|
| Display product name | `useProduct()` | `product.productName` |
| Display price | `useProduct()` | `selectedItem.sellers[0].commertialOffer.Price` |
| Show discount | `useProduct()` | Calculate from ListPrice vs Price |
| Change quantity | `useProductDispatch()` | `SET_QUANTITY` with quantity number |
| Select SKU directly | `useProductDispatch()` | `SET_SELECTED_ITEM` with complete Item object |
| Select by color/size | `useProductDispatch()` | Find Item by variation, then `SET_SELECTED_ITEM` |
| Set variation state | `useProductDispatch()` | `SKU_SELECTOR_SET_VARIATIONS_SELECTED` |
| Check availability | `useProduct()` | `selectedItem.sellers[0].commertialOffer.AvailableQuantity` |
| Get images | `useProduct()` | `selectedItem.images` |

---

## 🔗 TYPE DEFINITIONS

```tsx
import type { ProductContextState } from 'vtex.product-context'

// Use in component props
interface MyComponentProps {
  productContext?: ProductContextState
}

// Or destructure with types
const MyComponent = () => {
  const productContext = useProduct()
  
  const product: Product | null = productContext?.product ?? null
  const selectedItem: Item | null = productContext?.selectedItem ?? null
  const quantity: number = productContext?.selectedQuantity ?? 1
}
```

---

## 📚 OFFICIAL REFERENCES

- https://github.com/vtex-apps/product-context

---