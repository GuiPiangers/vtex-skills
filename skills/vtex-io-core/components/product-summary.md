# PRODUCT SUMMARY GUIDE

> Complete guide for building product displays using VTEX Product Summary blocks

---

## 🎯 WHAT IS PRODUCT SUMMARY?

Product Summary is VTEX's system for displaying product information in **lists and grids** across your store.

**Core concept:**
```
Product Summary ≠ Product Page (PDP)
Product Summary = Product Cards in Shelves/Grids/Search Results
```

**Mental model:**
- Product Page = Full product details with add to cart
- Product Summary = Compact product preview in lists

---

## 🧱 ARCHITECTURE

### Two-Layer System

```
┌─────────────────────────────────────────┐
│  list-context.product-list              │  ← Fetches products (GraphQL)
│  ├── product-summary.shelf              │  ← Structure wrapper
│      ├── product-summary-image          │  ← Individual blocks
│      ├── product-summary-name           │
│      ├── product-summary-price          │
│      └── product-summary-buy-button     │
└─────────────────────────────────────────┘
```

**Layer 1: Data Provider**
- `list-context.product-list` runs GraphQL queries
- Fetches product data from catalog
- Provides context to children

**Layer 2: Display Structure**
- `product-summary.shelf` receives product data
- Distributes data to child blocks
- Each child block renders specific product info

---

## 📦 AVAILABLE BLOCKS

### Core Blocks (Mandatory)

| Block | Purpose |
|-------|---------|
| `list-context.product-list` | 🔴 **MANDATORY** - Fetches and provides product data |
| `product-summary.shelf` | 🔴 **MANDATORY** - Structure wrapper for all child blocks |

### Child Blocks (Composable)

| Block | Renders | Common Use |
|-------|---------|------------|
| `product-summary-image` | Product image with hover support | All product cards |
| `product-summary-name` | Product name/title | All product cards |
| `product-summary-brand` | Brand name | Premium/branded products |
| `product-summary-description` | Short description | Detailed listings |
| `product-summary-sku-selector` | Color/size variations | Configurable products |
| `product-summary-buy-button` | Quick buy button | Minicart v1 only |
| `product-summary-attachment-list` | Product attachments | Customizable products |
| `product-summary-sku-name` | Selected SKU name | After SKU selection |
| `product-specification-badges` | Specification badges | Highlighted features |

### Price Blocks (Use Product Price App)

⚠️ **IMPORTANT:** `product-summary-price` is **DEPRECATED**

**Use instead:**
```json
{
  "dependencies": {
    "vtex.product-price": "1.x"
  }
}
```

**Product Price blocks:**
- `product-list-price` - Original price
- `product-selling-price` - Current selling price
- `product-spot-price` - Spot price (PIX/cash)
- `product-installments` - Installment options
- `product-price-savings` - Savings amount/percentage

---

## 🚀 BASIC SETUP

### Step 1: Add Dependency

```json
{
  "dependencies": {
    "vtex.product-summary": "2.x"
  }
}
```

### Step 2: Basic Structure

```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
  
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-selling-price",
      "add-to-cart-button"
    ]
  }
}
```

**That's it!** This creates a functional product list.

---

## 📋 COMMON PATTERNS

### Pattern 1: Simple Product Card (E-commerce Standard)

```json
{
  "product-summary.shelf#simple": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-list-price",
      "product-selling-price",
      "add-to-cart-button"
    ]
  }
}
```

**Use case:** Most e-commerce stores, clean product grids

---

### Pattern 2: Detailed Product Card (Fashion/Apparel)

```json
{
  "product-summary.shelf#detailed": {
    "children": [
      "stack-layout#prodsum",
      "product-summary-name",
      "product-summary-brand",
      "product-rating-inline",
      "product-summary-sku-selector",
      "product-selling-price",
      "product-installments",
      "add-to-cart-button"
    ]
  },
  
  "stack-layout#prodsum": {
    "children": [
      "product-summary-image",
      "product-specification-badges"
    ]
  }
}
```

**Use case:** Fashion stores with color/size variations, brands matter

---

### Pattern 3: Quick Buy Card (Marketplaces)

```json
{
  "product-summary.shelf#quickbuy": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-selling-price",
      "product-summary-buy-button"
    ]
  },
  
  "product-summary-buy-button": {
    "props": {
      "isOneClickBuy": true
    }
  }
}
```

**Use case:** One-click purchase flows, fast checkout

---

### Pattern 4: Comparison Card (Electronics)

```json
{
  "product-summary.shelf#comparison": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-summary-description",
      "product-specification-badges",
      "product-selling-price",
      "product-installments",
      "add-to-cart-button"
    ]
  }
}
```

**Use case:** Electronics, appliances, technical products

---

## 🎨 IMAGE CONFIGURATION

### Basic Image

```json
{
  "product-summary-image": {
    "props": {
      "showBadge": true,
      "aspectRatio": "1:1",
      "maxHeight": 300
    }
  }
}
```

### Image with Hover Effect

```json
{
  "product-summary-image#hover": {
    "props": {
      "showBadge": true,
      "hoverImage": {
        "criteria": "index",
        "index": 1
      }
    }
  }
}
```

**Result:** Shows second image on hover

### Image by Label

```json
{
  "product-summary-image#label": {
    "props": {
      "mainImageLabel": {
        "label": "front",
        "labelMatchCriteria": "exact"
      },
      "hoverImage": {
        "criteria": "label",
        "label": "back",
        "labelMatchCriteria": "exact"
      }
    }
  }
}
```

**Use case:** Controlled image display based on admin labels

### Responsive Image Sizing

```json
{
  "product-summary-image#responsive": {
    "props": {
      "width": {
        "desktop": 400,
        "mobile": 200
      },
      "aspectRatio": {
        "desktop": "1:1",
        "mobile": "3:4"
      }
    }
  }
}
```

---

## 🏷️ NAME & BRAND

### Product Name

```json
{
  "product-summary-name": {
    "props": {
      "tag": "h2",
      "showFieldsProps": {
        "showProductReference": false,
        "showBrandName": false,
        "showSku": false
      }
    }
  }
}
```

### Product Name with Brand

```json
{
  "product-summary-name#with-brand": {
    "props": {
      "tag": "h3",
      "showFieldsProps": {
        "showBrandName": true,
        "showProductReference": false
      }
    }
  }
}
```

### Separate Brand Block

```json
{
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-brand",
      "product-summary-name",
      "product-selling-price"
    ]
  }
}
```

---

## 💰 PRICE CONFIGURATION

### Modern Price Setup (Recommended)

**Dependencies:**
```json
{
  "dependencies": {
    "vtex.product-summary": "2.x",
    "vtex.product-price": "1.x"
  }
}
```

**Basic Price:**
```json
{
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "flex-layout.row#price-block"
    ]
  },
  
  "flex-layout.row#price-block": {
    "children": [
      "product-list-price",
      "product-selling-price"
    ]
  }
}
```

### Price with Installments

```json
{
  "flex-layout.col#price": {
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-installments"
    ]
  },
  
  "product-installments": {
    "props": {
      "message": "or {installmentsNumber}x of {installmentValue} interest-free"
    }
  }
}
```

### Price with Savings

```json
{
  "flex-layout.row#price-savings": {
    "children": [
      "product-selling-price",
      "product-price-savings"
    ]
  },
  
  "product-price-savings": {
    "props": {
      "message": "Save {savingsPercentage}"
    }
  }
}
```

---

## 🔄 ASYNC PRICES (Performance)

For large product lists, fetch prices asynchronously to improve initial page load.

### Step 1: Configure Search Result

```json
{
  "search-result-layout.desktop": {
    "props": {
      "context": {
        "simulationBehavior": "skip"
      }
    }
  }
}
```

### Step 2: Enable Async on Product Summary

```json
{
  "product-summary.shelf": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-price-suspense"
    ]
  }
}
```

### Step 3: Wrap Prices in Suspense

```json
{
  "product-price-suspense": {
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-installments"
    ]
  }
}
```

**Result:** Products load immediately, prices load progressively

---

## 🎛️ SKU SELECTOR

### Basic SKU Selector

```json
{
  "product-summary-sku-selector": {
    "props": {
      "showVariationsLabels": ["false"]
    }
  }
}
```

### SKU Selector with Options

```json
{
  "product-summary-sku-selector#detailed": {
    "props": {
      "showVariationsLabels": ["true"],
      "visibleVariations": ["Color", "Size"],
      "displayMode": "default",
      "initialSelection": "complete"
    }
  }
}
```

**Props explained:**
- `showVariationsLabels`: Show "Color:", "Size:" labels
- `visibleVariations`: Which variations to show
- `displayMode`: `"default"` (buttons) or `"select"` (dropdown)
- `initialSelection`: Auto-select first SKU

---

## 🛒 BUY BUTTON

### ⚠️ IMPORTANT: Minicart Version

**Minicart v1 → Use `product-summary-buy-button`**
**Minicart v2 → Use `add-to-cart-button`**

### Buy Button (Minicart v1 - Legacy)

```json
{
  "product-summary-buy-button": {
    "props": {
      "isOneClickBuy": false,
      "displayBuyButton": "displayButtonAlways"
    }
  }
}
```

### Add to Cart (Minicart v2 - Recommended)

```json
{
  "dependencies": {
    "vtex.add-to-cart-button": "0.x"
  }
}
```

```json
{
  "add-to-cart-button": {
    "props": {
      "text": "Add to Cart",
      "onClickBehavior": "ensure-sku-selection",
      "customToastUrl": "/checkout/#/cart"
    }
  }
}
```

**`onClickBehavior` options:**
- `"add-to-cart"` - Always add to cart (needs SKU selector)
- `"go-to-product-page"` - Redirect to PDP
- `"ensure-sku-selection"` - Go to PDP if SKU not selected

---

## 📊 LIST CONTEXT CONFIGURATION

### Fetching Products

The `list-context.product-list` accepts props to control what products are fetched:

```json
{
  "list-context.product-list#category": {
    "blocks": ["product-summary.shelf"],
    "props": {
      "category": "1",
      "orderBy": "OrderByTopSaleDESC",
      "hideUnavailableItems": true,
      "maxItems": 10,
      "skusFilter": "FIRST_AVAILABLE",
      "installmentCriteria": "MAX_WITHOUT_INTEREST"
    }
  }
}
```

### Key Props Explained

**Product Selection:**
- `category`: Category ID (use "/" for subcategories: "1/2/3")
- `collection`: Collection ID
- `specificationFilters`: Array of spec filters
- `orderBy`: Sort order (see table below)

**Performance:**
- `skusFilter`: Which SKUs to fetch (see table below)
- `maxItems`: Limit number of products
- `hideUnavailableItems`: Skip out-of-stock

**Pricing:**
- `installmentCriteria`: Which installment to show (see table below)
- `preferredSKU`: Which SKU to prioritize

### Sort Options (`orderBy`)

| Value | Result |
|-------|--------|
| `""` | Relevance (default) |
| `OrderByTopSaleDESC` | Best sellers |
| `OrderByReleaseDateDESC` | Newest first |
| `OrderByBestDiscountDESC` | Biggest discounts |
| `OrderByPriceDESC` | Highest price |
| `OrderByPriceASC` | Lowest price |
| `OrderByNameASC` | A-Z |
| `OrderByNameDESC` | Z-A |

### SKU Filter Options (`skusFilter`)

| Value | Behavior | Performance | Use When |
|-------|----------|-------------|----------|
| `FIRST_AVAILABLE` | Only first available SKU | ⚡ Best | No SKU selector on shelf |
| `ALL_AVAILABLE` | All available SKUs | ⚡⚡ Good | Have SKU selector |
| `ALL` | All SKUs (including unavailable) | ⚠️ Slower | Need full SKU list |

### Installment Options (`installmentCriteria`)

| Value | Shows |
|-------|-------|
| `MAX_WITHOUT_INTEREST` | Max installments with 0% interest |
| `MAX_WITH_INTEREST` | Max installments (any interest) |

### Preferred SKU (`preferredSKU`)

| Value | Selects |
|-------|---------|
| `FIRST_AVAILABLE` | First available SKU |
| `LAST_AVAILABLE` | Last available SKU |
| `PRICE_ASC` | Cheapest available |
| `PRICE_DESC` | Most expensive available |

---

## 🎯 REAL-WORLD EXAMPLES

### Example 1: Fashion Store Shelf

```json
{
  "list-context.product-list#fashion": {
    "blocks": ["product-summary.shelf#fashion"],
    "props": {
      "orderBy": "OrderByReleaseDateDESC",
      "maxItems": 12,
      "skusFilter": "ALL_AVAILABLE"
    }
  },
  
  "product-summary.shelf#fashion": {
    "children": [
      "stack-layout#image-badge",
      "product-summary-brand",
      "product-summary-name",
      "product-summary-sku-selector",
      "flex-layout.row#price-fashion",
      "add-to-cart-button"
    ]
  },
  
  "stack-layout#image-badge": {
    "children": [
      "product-summary-image",
      "product-specification-badges"
    ]
  },
  
  "product-summary-image": {
    "props": {
      "aspectRatio": "3:4",
      "hoverImage": {
        "criteria": "index",
        "index": 1
      }
    }
  },
  
  "flex-layout.row#price-fashion": {
    "children": [
      "product-list-price",
      "product-selling-price"
    ]
  }
}
```

---

### Example 2: Electronics Comparison Grid

```json
{
  "list-context.product-list#electronics": {
    "blocks": ["product-summary.shelf#electronics"],
    "props": {
      "category": "3",
      "orderBy": "OrderByPriceDESC",
      "maxItems": 8,
      "skusFilter": "FIRST_AVAILABLE"
    }
  },
  
  "product-summary.shelf#electronics": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-summary-description",
      "product-specification-badges",
      "flex-layout.col#price-installments",
      "add-to-cart-button"
    ]
  },
  
  "product-summary-image": {
    "props": {
      "aspectRatio": "1:1",
      "width": 300
    }
  },
  
  "flex-layout.col#price-installments": {
    "children": [
      "product-selling-price",
      "product-installments"
    ]
  },
  
  "product-installments": {
    "props": {
      "message": "or up to {installmentsNumber}x of {installmentValue}"
    }
  }
}
```

---

### Example 3: Marketplace Quick Buy

```json
{
  "list-context.product-list#quickbuy": {
    "blocks": ["product-summary.shelf#quickbuy"],
    "props": {
      "orderBy": "OrderByTopSaleDESC",
      "maxItems": 20,
      "skusFilter": "FIRST_AVAILABLE",
      "hideUnavailableItems": true
    }
  },
  
  "product-summary.shelf#quickbuy": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-price-suspense"
    ]
  },
  
  "product-price-suspense": {
    "children": [
      "product-selling-price",
      "add-to-cart-button"
    ]
  },
  
  "product-summary-image": {
    "props": {
      "showBadge": true,
      "aspectRatio": "1:1"
    }
  },
  
  "add-to-cart-button": {
    "props": {
      "onClickBehavior": "ensure-sku-selection"
    }
  }
}
```

---

### Example 4: Search Results with Filters

```json
{
  "search-result-layout.desktop": {
    "children": [
      "breadcrumb.search",
      "search-title.v2",
      "total-products.v2",
      "order-by.v2",
      "search-fetch-previous",
      "search-content",
      "filter-navigator.v3",
      "search-fetch-more"
    ],
    "props": {
      "pagination": "show-more",
      "mobileLayout": {
        "mode1": "small",
        "mode2": "normal"
      },
      "context": {
        "skusFilter": "ALL_AVAILABLE",
        "simulationBehavior": "skip"
      }
    }
  },
  
  "search-content": {
    "blocks": ["gallery", "not-found"]
  },
  
  "gallery": {
    "blocks": ["product-summary.shelf#search"]
  },
  
  "product-summary.shelf#search": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-rating-inline",
      "product-price-suspense"
    ]
  },
  
  "product-price-suspense": {
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-installments",
      "add-to-cart-button"
    ]
  }
}
```

---

## 🎨 CUSTOMIZATION (CSS Handles)

### Product Summary Container

```css
/* Main container */
.container { }
.containerNormal { }  /* Default size */
.containerSmall { }   /* Compact mode */
.containerInline { }  /* Inline layout */

/* Structural */
.element { }
.column { }
.information { }
```

### Image Handles

```css
.imageContainer { }
.image { }
.imagePlaceholder { }
.aspectRatio { }
.hoverImage { }
.hoverEffect { }
.mainImageHovered { }
```

### Name & Brand Handles

```css
.nameContainer { }
.nameWrapper { }
.brandName { }
.skuName { }
.productReference { }
```

### Price Handles

```css
.priceContainer { }
```

### Button Handles

```css
.buyButtonContainer { }
.buyButton { }
.isHidden { }
```

### Example Customization

```css
/* Custom product card styling */
.container {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  transition: transform 0.2s;
}

.container:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.imageContainer {
  position: relative;
  overflow: hidden;
  border-radius: 4px;
}

.nameContainer {
  margin: 12px 0;
  min-height: 48px;
}

.buyButton {
  width: 100%;
  background: #000;
  color: #fff;
  border-radius: 4px;
  padding: 12px;
}
```

---

## ⚠️ COMMON MISTAKES & SOLUTIONS

### Mistake 1: Forgetting Data Provider

❌ **Wrong:**
```json
{
  "product-summary.shelf": {
    "children": ["product-summary-image"]
  }
}
```

✅ **Correct:**
```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
  "product-summary.shelf": {
    "children": ["product-summary-image"]
  }
}
```

---

### Mistake 2: Using Deprecated Price Block

❌ **Wrong:**
```json
{
  "children": [
    "product-summary-price"  // Deprecated!
  ]
}
```

✅ **Correct:**
```json
{
  "dependencies": {
    "vtex.product-price": "1.x"
  }
}
```
```json
{
  "children": [
    "product-selling-price"
  ]
}
```

---

### Mistake 3: Wrong Buy Button for Minicart v2

❌ **Wrong:**
```json
{
  "children": [
    "product-summary-buy-button"  // Only for Minicart v1!
  ]
}
```

✅ **Correct:**
```json
{
  "dependencies": {
    "vtex.add-to-cart-button": "0.x"
  }
}
```
```json
{
  "children": [
    "add-to-cart-button"
  ]
}
```

---

### Mistake 4: Not Optimizing for Performance

❌ **Wrong:**
```json
{
  "list-context.product-list": {
    "props": {
      "skusFilter": "ALL",  // Fetches ALL SKUs including unavailable
      "maxItems": 100       // Too many items
    }
  }
}
```

✅ **Correct:**
```json
{
  "list-context.product-list": {
    "props": {
      "skusFilter": "FIRST_AVAILABLE",  // Only first SKU
      "maxItems": 12,                   // Reasonable limit
      "hideUnavailableItems": true
    }
  },
  "product-summary.shelf": {
    "props": {
      "priceBehavior": "async"  // Async prices
    }
  }
}
```

---

### Mistake 5: Missing SKU Selector with "Always Add to Cart"

❌ **Wrong:**
```json
{
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "add-to-cart-button"  // No SKU selector!
    ]
  },
  "add-to-cart-button": {
    "props": {
      "onClickBehavior": "add-to-cart"  // Will fail without SKU!
    }
  }
}
```

✅ **Correct - Option 1 (Add SKU Selector):**
```json
{
  "children": [
    "product-summary-image",
    "product-summary-name",
    "product-summary-sku-selector",  // ← Add this
    "add-to-cart-button"
  ]
}
```

✅ **Correct - Option 2 (Redirect to PDP):**
```json
{
  "add-to-cart-button": {
    "props": {
      "onClickBehavior": "ensure-sku-selection"  // ← Safe behavior
    }
  }
}
```

---

## 📋 DECISION TREE

```
BUILDING PRODUCT SUMMARY?
│
├─ Need product list/grid?
│  → Use list-context.product-list + product-summary.shelf
│
├─ Which blocks to include?
│  ├─ Image? → product-summary-image
│  ├─ Name? → product-summary-name
│  ├─ Brand? → product-summary-brand
│  ├─ Price? → product-selling-price (NOT product-summary-price!)
│  ├─ Variations? → product-summary-sku-selector
│  └─ Buy? → add-to-cart-button (v2) OR product-summary-buy-button (v1)
│
├─ Performance concerns?
│  ├─ Large lists? → priceBehavior: "async"
│  ├─ Many SKUs? → skusFilter: "FIRST_AVAILABLE"
│  └─ Search results? → simulationBehavior: "skip"
│
└─ Advanced features?
   ├─ Hover image? → hoverImage prop
   ├─ Badges? → product-specification-badges
   └─ Installments? → product-installments
```

---

## 🔗 RELATED GUIDES

- **Product Price** - `/mnt/skills/public/product-price/SKILL.md` (price blocks)
- **Search Result** - `/mnt/skills/public/search-result/SKILL.md` (search pages)
- **Flex Layout** - `/mnt/skills/public/flex-layout/SKILL.md` (layout structure)
- **Add to Cart Button** - Minicart v2 integration

---

## 📚 QUICK REFERENCE

### Essential Dependencies

```json
{
  "dependencies": {
    "vtex.product-summary": "2.x",
    "vtex.product-price": "1.x",
    "vtex.add-to-cart-button": "0.x"
  }
}
```

### Minimal Working Example

```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-selling-price",
      "add-to-cart-button"
    ]
  }
}
```

### Performance Optimized Example

```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"],
    "props": {
      "skusFilter": "FIRST_AVAILABLE",
      "maxItems": 12,
      "hideUnavailableItems": true
    }
  },
  "product-summary.shelf": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-price-suspense"
    ]
  },
  "product-price-suspense": {
    "children": [
      "product-selling-price"
    ]
  }
}
```

---

## ✅ CHECKLIST

**Before deploying Product Summary:**

### Critical:
- [ ] Used `list-context.product-list` to fetch products
- [ ] Used `product-summary.shelf` as structure wrapper
- [ ] Used `product-selling-price` (NOT deprecated `product-summary-price`)
- [ ] Used correct buy button (`add-to-cart-button` for v2 OR `product-summary-buy-button` for v1)
- [ ] If using "add-to-cart" behavior, included SKU selector OR used "ensure-sku-selection"

### Performance:
- [ ] Set appropriate `skusFilter` for use case
- [ ] Limited `maxItems` to reasonable number
- [ ] Considered `priceBehavior: "async"` for large lists
- [ ] Set `hideUnavailableItems: true` if applicable

### User Experience:
- [ ] Image has proper `aspectRatio` for consistency
- [ ] Added hover image for visual feedback (optional)
- [ ] Included installments for high-ticket items (optional)
- [ ] Added SKU selector for configurable products (optional)
- [ ] Tested on mobile and desktop

### SEO & Accessibility:
- [ ] Product name uses semantic HTML tag (`h2`, `h3`)
- [ ] Images have proper dimensions
- [ ] Links are accessible

---

## 🎓 KEY TAKEAWAYS

1. **Two-layer architecture**: `list-context.product-list` (data) + `product-summary.shelf` (display)

2. **Price blocks are separate**: Use `vtex.product-price` app, NOT `product-summary-price`

3. **Buy button depends on Minicart version**:
   - Minicart v2 → `add-to-cart-button`
   - Minicart v1 → `product-summary-buy-button`

4. **Performance matters**: Use `async` prices and optimize `skusFilter`

5. **Composable blocks**: Mix and match child blocks based on needs

6. **Context is key**: Product Summary works anywhere with product context (shelves, search, related products)

---

**Official Documentation:**
- https://developers.vtex.com/docs/apps/vtex.product-summary
- https://developers.vtex.com/docs/apps/vtex.product-price