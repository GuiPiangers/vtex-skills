# PRODUCT PRICE GUIDE

> Complete reference for displaying product prices in VTEX IO Store Framework

---

## 🎯 WHAT IS PRODUCT PRICE?

Product Price is VTEX's **official and only app** for rendering product pricing information.

**Critical Information:**
```
✅ vtex.product-price (1.x)     → Current, supported
❌ product-summary-price         → DEPRECATED
❌ store-components ProductPrice → DEPRECATED
```

**Use Product Price for:**
- Product listing prices (shelves, grids)
- Product detail page (PDP) prices
- Cart prices
- Any product pricing display

---

## 📦 AVAILABLE BLOCKS

### Price Display Blocks

| Block | Purpose | When Rendered |
|-------|---------|---------------|
| `product-list-price` | Original/from price | Only if > selling price |
| `product-selling-price` | Current selling price | Always (if available) |
| `product-spot-price` | Cash/PIX price | Only if different from selling price |
| `product-installments` | Best installment option | When installments available |
| `product-installments-list` | All installment options | When you need full list |
| `product-installments-list-item` | Single installment option | Inside installments list |

### Savings Blocks

| Block | Purpose |
|-------|---------|
| `product-price-savings` | Discount from list price |
| `product-spot-price-savings` | Discount for spot price |

### Range Blocks (Multiple SKUs)

| Block | Purpose |
|-------|---------|
| `product-list-price-range` | Price range for list prices |
| `product-selling-price-range` | Price range for selling prices |

### Utility Blocks

| Block | Purpose |
|-------|---------|
| `product-seller-name` | Displays seller name |
| `product-price-suspense` | Loading fallback for async prices |

---

## 🚀 BASIC SETUP

### Step 1: Add Dependency

```json
{
  "dependencies": {
    "vtex.product-price": "1.x"
  }
}
```

### Step 2: Basic Price Structure

```json
{
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-list-price",
      "product-selling-price"
    ]
  }
}
```

**That's it!** This renders both list and selling prices.

---

## 📋 COMMON PATTERNS

### Pattern 1: Simple E-commerce Price

```json
{
  "product-summary.shelf#simple": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "flex-layout.row#price"
    ]
  },
  
  "flex-layout.row#price": {
    "children": [
      "product-list-price",
      "product-selling-price"
    ]
  }
}
```

**Renders:**
```
~~$99.90~~  $79.90
```

---

### Pattern 2: Price with Savings Badge

```json
{
  "flex-layout.col#price-savings": {
    "children": [
      "product-list-price",
      "flex-layout.row#selling-and-savings"
    ]
  },
  
  "flex-layout.row#selling-and-savings": {
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

**Renders:**
```
From: $99.90
$79.90  Save 20%
```

---

### Pattern 3: Price with Installments

```json
{
  "flex-layout.col#price-installments": {
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

**Renders:**
```
From: $599.90
$499.90
or 10x of $49.99 interest-free
```

---

### Pattern 4: Spot Price (PIX/Cash)

```json
{
  "flex-layout.col#price-pix": {
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-spot-price",
      "product-installments"
    ]
  },
  
  "product-spot-price": {
    "props": {
      "message": "{spotPriceValue} with PIX"
    }
  }
}
```

**Renders:**
```
From: $599.90
$499.90
$474.91 with PIX
or 10x of $49.99
```

---

### Pattern 5: Complete Price Block

```json
{
  "flex-layout.col#complete-price": {
    "props": {
      "blockClass": "price-block"
    },
    "children": [
      "product-list-price#complete",
      "flex-layout.row#selling-savings",
      "product-spot-price#pix",
      "product-installments#complete"
    ]
  },
  
  "product-list-price#complete": {
    "props": {
      "message": "From: {listPriceValue}"
    }
  },
  
  "flex-layout.row#selling-savings": {
    "children": [
      "product-selling-price#complete",
      "product-price-savings#badge"
    ]
  },
  
  "product-selling-price#complete": {
    "props": {
      "message": "{sellingPriceValue}"
    }
  },
  
  "product-price-savings#badge": {
    "props": {
      "message": "-{savingsPercentage}"
    }
  },
  
  "product-spot-price#pix": {
    "props": {
      "message": "{spotPriceValue} à vista no PIX"
    }
  },
  
  "product-installments#complete": {
    "props": {
      "message": "ou até {installmentsNumber}x de {installmentValue} sem juros"
    }
  }
}
```

---

## 💰 PRICE BLOCKS DETAILED

### `product-list-price`

**Purpose:** Display original/from price (crossed out)

**Behavior:** Only renders if list price > selling price

**Common Props:**
```json
{
  "product-list-price": {
    "props": {
      "message": "From: {listPriceValue}",
      "alwaysShow": false,
      "markers": ["discount"],
      "blockClass": "list-price"
    }
  }
}
```

**Message Variables:**
- `listPriceValue` - The list price (e.g., "$99.90")
- `listPriceWithTax` - List price with tax
- `listPriceWithUnitMultiplier` - List price × unit multiplier
- `taxPercentage` - Tax percentage
- `taxValue` - Tax value
- `measurementUnit` - Unit of measure (e.g., "kg", "lb")
- `unitMultiplier` - Unit multiplier value
- `hasMeasurementUnit` - Boolean: has unit of measure
- `hasUnitMultiplier` - Boolean: has unit multiplier

**Example with Unit:**
```json
{
  "product-list-price": {
    "props": {
      "message": "{listPriceValue} / {unitMultiplier} {measurementUnit}"
    }
  }
}
```
**Renders:** `$24.00 / 2 oz`

---

### `product-selling-price`

**Purpose:** Display current selling price

**Behavior:** Always renders (if product is available)

**Common Props:**
```json
{
  "product-selling-price": {
    "props": {
      "message": "{sellingPriceValue}",
      "alwaysShow": false,
      "markers": ["highlight"],
      "blockClass": "selling-price"
    }
  }
}
```

**Message Variables:**
- `sellingPriceValue` - Current selling price
- `sellingPriceWithTax` - Selling price with tax
- `sellingPriceWithUnitMultiplier` - Selling price × multiplier
- `sellingPriceWithUnitMultiplierAndTax` - Price × multiplier + tax
- `sellingPriceWithTaxWithoutUnitMultiplier` - Price + tax (no multiplier)
- `taxPercentage` - Tax percentage
- `taxValue` - Tax value
- `hasListPrice` - Boolean: has list price
- `measurementUnit` - Unit of measure
- `unitMultiplier` - Unit multiplier
- `hasMeasurementUnit` - Boolean
- `hasUnitMultiplier` - Boolean

**Advanced Unit of Measure Example:**
```json
{
  "product-selling-price": {
    "props": {
      "message": "{sellingPriceWithUnitMultiplier}{hasMeasurementUnit, select, true { / {hasUnitMultiplier, select, true {{unitMultiplier}} false {}} {measurementUnit}} false {}}"
    }
  }
}
```

**Products with unit:** `$24.00 / 2 oz`  
**Products without:** `$24.00`

---

### `product-spot-price`

**Purpose:** Display cash/PIX price (lowest payment option)

**Behavior:** Only renders if spot price ≠ selling price

**Common Props:**
```json
{
  "product-spot-price": {
    "props": {
      "message": "{spotPriceValue} no PIX",
      "alwaysShow": false,
      "blockClass": "spot-price"
    }
  }
}
```

**Message Variables:**
- `spotPriceValue` - Lowest price available

**When It Appears:**
- Cash discount configured
- PIX payment with discount
- Specific payment method promotion

---

### `product-installments`

**Purpose:** Display best installment option

**Behavior:** Shows highest installment count by default

**Common Props:**
```json
{
  "product-installments": {
    "props": {
      "message": "ou {installmentsNumber}x de {installmentValue} sem juros",
      "markers": ["installments"],
      "blockClass": "installments",
      "installmentsCriteria": "max-quantity-without-interest",
      "installmentOptionsFilter": {
        "paymentSystemName": "Visa",
        "installmentsQuantity": 12
      }
    }
  }
}
```

**Message Variables:**
- `spotPriceValue` - Spot price
- `installmentsNumber` - Number of installments
- `installmentValue` - Value per installment
- `installmentsTotalValue` - Total installment value
- `interestRate` - Interest rate
- `paymentSystemName` - Payment system name
- `hasInterest` - Boolean: has interest
- `hasMoreThanOne` - Boolean: more than 1 installment

**installmentsCriteria Options:**

| Value | Behavior |
|-------|----------|
| `max-quantity` | Most installments (default) |
| `max-quantity-without-interest` | Most installments with 0% interest |

**installmentOptionsFilter:**
```json
{
  "installmentOptionsFilter": {
    "paymentSystemName": "Visa",      // Filter by payment system
    "installmentsQuantity": 10        // Filter by quantity
  }
}
```

**Examples:**

```json
// Always show interest-free option
{
  "product-installments#no-interest": {
    "props": {
      "installmentsCriteria": "max-quantity-without-interest",
      "message": "or {installmentsNumber}x of {installmentValue}"
    }
  }
}
```

```json
// Show specific payment system
{
  "product-installments#visa": {
    "props": {
      "installmentOptionsFilter": {
        "paymentSystemName": "Visa"
      },
      "message": "{installmentsNumber}x of {installmentValue} on Visa"
    }
  }
}
```

---

### `product-installments-list`

**Purpose:** Display ALL installment options

**Behavior:** Lists all payment plans

**Common Props:**
```json
{
  "product-installments-list": {
    "props": {
      "paymentSystemName": "Visa",
      "installmentsToShow": [1, 3, 6, 10, 12],
      "blockClass": "installments-list"
    },
    "children": [
      "product-installments-list-item"
    ]
  }
}
```

**Props:**
- `paymentSystemName` - Filter by payment system
- `installmentsToShow` - Array of installment counts to show

**Example - Custom List:**
```json
{
  "product-installments-list#custom": {
    "props": {
      "installmentsToShow": [1, 6, 12]
    },
    "children": [
      "product-installments-list-item#custom"
    ]
  },
  
  "product-installments-list-item#custom": {
    "props": {
      "message": "{installmentsNumber}x of {installmentValue} {hasInterest, select, true {with interest} false {interest-free}}"
    }
  }
}
```

---

### `product-price-savings`

**Purpose:** Display savings amount/percentage

**Behavior:** Only renders if list price > selling price

**Common Props:**
```json
{
  "product-price-savings": {
    "props": {
      "message": "Save {savingsPercentage}",
      "markers": ["savings"],
      "blockClass": "savings",
      "percentageStyle": "compact",
      "minimumPercentage": 10
    }
  }
}
```

**Message Variables:**
- `previousPriceValue` - List price
- `newPriceValue` - Selling price
- `savingsValue` - Absolute savings
- `savingsWithTax` - Savings with tax
- `savingsPercentage` - Percentage savings

**Percentage Style:**

| Value | Result |
|-------|--------|
| `locale` (default) | `20 %` (with space) |
| `compact` | `20%` (no space) |

**Minimum Percentage:**
```json
{
  "product-price-savings": {
    "props": {
      "minimumPercentage": 15  // Only show if ≥ 15% off
    }
  }
}
```

**Common Message Formats:**

```json
// Percentage only
"message": "Save {savingsPercentage}"
// Result: Save 20%

// Amount only
"message": "Save {savingsValue}"
// Result: Save $20.00

// Both
"message": "Save {savingsValue} ({savingsPercentage})"
// Result: Save $20.00 (20%)

// Custom badge
"message": "-{savingsPercentage}"
// Result: -20%
```

---

### `product-spot-price-savings`

**Purpose:** Display savings for spot price

**Behavior:** Renders if spot price < list price

**Common Props:**
```json
{
  "product-spot-price-savings": {
    "props": {
      "message": "Economy of {spotPriceSavingsValue} with PIX",
      "percentageStyle": "compact"
    }
  }
}
```

**Message Variables:**
- `previousPriceValue` - List price
- `newSpotPriceValue` - Spot price
- `spotPriceSavingsValue` - Absolute savings
- `spotPriceSavingsWithTax` - Savings with tax
- `spotPriceSavingsPercentage` - Percentage savings

---

## 📊 PRICE RANGE BLOCKS

### When to Use Price Ranges

Use price range blocks when:
- Product has multiple SKUs with different prices
- Showing "From $X to $Y" format
- Before user selects a SKU

### `product-selling-price-range`

```json
{
  "product-selling-price-range": {
    "props": {
      "message": "From {minPriceValue} to {maxPriceValue}"
    }
  }
}
```

**Message Variables:**
- `minPriceValue` - Cheapest SKU price
- `maxPriceValue` - Most expensive SKU price
- `minPriceWithTax` - Cheapest with tax
- `maxPriceWithTax` - Most expensive with tax
- `sellingPriceValue` - Single SKU price (if only 1 SKU)
- `sellingPriceWithTax` - Single SKU with tax

**Smart Behavior:**
```
Multiple SKUs → "From $99 to $199"
Single SKU   → "$149"
```

### `product-list-price-range`

```json
{
  "product-list-price-range": {
    "props": {
      "message": "Was {minPriceValue} to {maxPriceValue}"
    }
  }
}
```

**Message Variables:** Same as selling price range but for list prices

---

## ⚡ ASYNC PRICES (Performance Optimization)

### What Are Async Prices?

**Traditional Flow:**
1. Load page
2. Wait for ALL product data (including prices)
3. Render page
4. **User waits longer** ⏱️

**Async Flow:**
1. Load page
2. Render products WITHOUT prices (show skeleton/loading)
3. Fetch prices in background
4. Update prices progressively
5. **User sees content faster** ⚡

### When to Use Async Prices

✅ **Use async when:**
- Large product lists (20+ items)
- Search result pages
- Category pages with many products
- Performance is critical

❌ **Skip async when:**
- Single product (PDP)
- Few products (< 10 items)
- Prices are critical to see immediately

### Implementation

**Step 1: Configure Search Result**

Tell search result to skip price simulation:

```json
{
  "search-result-layout.desktop": {
    "children": ["search-content"],
    "props": {
      "context": {
        "simulationBehavior": "skip"
      }
    }
  }
}
```

**Step 2: Enable Async on Product Summary**

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

**Step 3: Wrap Prices in Suspense**

```json
{
  "product-price-suspense": {
    "props": {
      "Fallback": "rich-text#price-loading"
    },
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-installments",
      "add-to-cart-button"
    ]
  },
  
  "rich-text#price-loading": {
    "props": {
      "text": "Loading price..."
    }
  }
}
```

**Complete Example:**

```json
{
  "search-result-layout.desktop": {
    "children": ["search-content"],
    "props": {
      "context": {
        "simulationBehavior": "skip"
      }
    }
  },
  
  "search-content": {
    "blocks": ["gallery"]
  },
  
  "gallery": {
    "blocks": ["product-summary.shelf#async"]
  },
  
  "product-summary.shelf#async": {
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
    "props": {
      "Fallback": "flex-layout.row#skeleton"
    },
    "children": [
      "flex-layout.col#price-async"
    ]
  },
  
  "flex-layout.row#skeleton": {
    "props": {
      "blockClass": "price-skeleton"
    },
    "children": [
      "rich-text#loading"
    ]
  },
  
  "rich-text#loading": {
    "props": {
      "text": "⏳ Loading..."
    }
  },
  
  "flex-layout.col#price-async": {
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-spot-price",
      "product-installments"
    ]
  }
}
```

### Custom Loading Skeleton

```json
{
  "product-price-suspense": {
    "props": {
      "Fallback": "flex-layout.col#skeleton"
    },
    "children": ["flex-layout.col#actual-price"]
  },
  
  "flex-layout.col#skeleton": {
    "props": {
      "blockClass": "price-skeleton"
    },
    "children": [
      "rich-text#skeleton-line1",
      "rich-text#skeleton-line2"
    ]
  },
  
  "rich-text#skeleton-line1": {
    "props": {
      "blockClass": "skeleton-line",
      "text": "████████"
    }
  },
  
  "rich-text#skeleton-line2": {
    "props": {
      "blockClass": "skeleton-line",
      "text": "████████████"
    }
  }
}
```

**CSS for Skeleton:**
```css
.skeleton-line {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  color: transparent;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

---

## 🎨 MESSAGE CUSTOMIZATION

### Using the `message` Prop

Every price block accepts a `message` prop using ICU Message Format.

**Basic Example:**
```json
{
  "product-selling-price": {
    "props": {
      "message": "Only {sellingPriceValue}!"
    }
  }
}
```

**Renders:** `Only $79.90!`

### Conditional Messages

Use ICU selects for conditional rendering:

```json
{
  "product-selling-price": {
    "props": {
      "message": "{hasListPrice, select, true {Now: {sellingPriceValue}} false {{sellingPriceValue}}}"
    }
  }
}
```

**Result:**
- Has list price: `Now: $79.90`
- No list price: `$79.90`

### Complex Conditional Example

```json
{
  "product-installments": {
    "props": {
      "message": "{hasMoreThanOne, select, true {{installmentsNumber}x of {installmentValue} {hasInterest, select, true {with interest} false {interest-free}}} false {Cash: {spotPriceValue}}}"
    }
  }
}
```

**Result:**
- Multiple installments with interest: `10x of $49.99 with interest`
- Multiple installments without: `10x of $49.99 interest-free`
- Single payment: `Cash: $499.00`

---

## 🏷️ USING MARKERS

Markers allow Site Editor customization without code changes.

### Setup

```json
{
  "product-selling-price": {
    "props": {
      "markers": ["highlight", "primary"],
      "message": "Special Price: {sellingPriceValue}"
    }
  }
}
```

### Site Editor Customization

1. Go to Site Editor
2. Select the price block
3. Edit message per marker
4. Changes apply without deployment

**Use Case:** Marketing can change "Special Price" to "Limited Offer" during campaigns.

---

## 🎨 CSS CUSTOMIZATION

### Main CSS Handles

```css
/* List Price */
.listPrice { }
.listPriceValue { }
.listPriceWithTax { }
.listPrice--isUnavailable { }

/* Selling Price */
.sellingPrice { }
.sellingPriceValue { }
.sellingPriceWithTax { }
.sellingPrice--hasListPrice { }
.sellingPrice--isUnavailable { }

/* Spot Price */
.spotPrice { }
.spotPriceValue { }
.spotPrice--isUnavailable { }

/* Installments */
.installments { }
.installmentsNumber { }
.installmentValue { }
.installmentsTotalValue { }
.interestRate { }
.paymentSystemName { }
.installmentsListContainer { }

/* Savings */
.savings { }
.savingsValue { }
.savingsWithTax { }
.savingsPercentage { }
.savings--isUnavailable { }

.spotPriceSavings { }
.spotPriceSavingsValue { }
.spotPriceSavingsPercentage { }

/* Price Range */
.listPriceRange { }
.listPriceRangeMinValue { }
.listPriceRangeMaxValue { }
.listPriceRangeUniqueValue { }

.sellingPriceRange { }
.sellingPriceRangeMinValue { }
.sellingPriceRangeMaxValue { }
.sellingPriceRangeUniqueValue { }

/* Seller */
.sellerNameContainer { }
.sellerName { }
.sellerNameContainer--isDefaultSeller { }

/* Tax */
.taxPercentage { }
```

### Example Customization

```css
/* Strikethrough list price */
.listPriceValue {
  text-decoration: line-through;
  color: #999;
  font-size: 14px;
}

/* Bold selling price */
.sellingPriceValue {
  font-size: 24px;
  font-weight: bold;
  color: #000;
}

/* Highlight spot price */
.spotPriceValue {
  font-size: 20px;
  color: #00a650;
  font-weight: 600;
}

/* Savings badge */
.savingsPercentage {
  background: #ff6b6b;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: bold;
}

/* Installments text */
.installments {
  color: #666;
  font-size: 14px;
}
```

---

## 🎯 REAL-WORLD EXAMPLES

### Example 1: Fashion E-commerce

```json
{
  "product-summary.shelf#fashion": {
    "children": [
      "product-summary-image",
      "product-summary-brand",
      "product-summary-name",
      "flex-layout.col#price-fashion"
    ]
  },
  
  "flex-layout.col#price-fashion": {
    "props": {
      "blockClass": "price-fashion"
    },
    "children": [
      "product-list-price#fashion",
      "flex-layout.row#selling-savings-fashion",
      "product-installments#fashion"
    ]
  },
  
  "product-list-price#fashion": {
    "props": {
      "message": "De {listPriceValue}",
      "blockClass": "list-price-fashion"
    }
  },
  
  "flex-layout.row#selling-savings-fashion": {
    "props": {
      "blockClass": "selling-row"
    },
    "children": [
      "product-selling-price#fashion",
      "product-price-savings#fashion"
    ]
  },
  
  "product-selling-price#fashion": {
    "props": {
      "message": "Por {sellingPriceValue}",
      "blockClass": "selling-price-fashion"
    }
  },
  
  "product-price-savings#fashion": {
    "props": {
      "message": "-{savingsPercentage}",
      "percentageStyle": "compact",
      "minimumPercentage": 5,
      "blockClass": "savings-badge"
    }
  },
  
  "product-installments#fashion": {
    "props": {
      "message": "ou {installmentsNumber}x de {installmentValue}",
      "installmentsCriteria": "max-quantity-without-interest",
      "blockClass": "installments-fashion"
    }
  }
}
```

---

### Example 2: Electronics with PIX

```json
{
  "product-summary.shelf#electronics": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-rating-inline",
      "flex-layout.col#price-electronics"
    ]
  },
  
  "flex-layout.col#price-electronics": {
    "children": [
      "product-list-price#electronics",
      "product-selling-price#electronics",
      "product-spot-price#pix",
      "product-spot-price-savings#pix",
      "product-installments#electronics"
    ]
  },
  
  "product-list-price#electronics": {
    "props": {
      "message": "De: {listPriceValue}"
    }
  },
  
  "product-selling-price#electronics": {
    "props": {
      "message": "Por: {sellingPriceValue}"
    }
  },
  
  "product-spot-price#pix": {
    "props": {
      "message": "💰 {spotPriceValue} no PIX",
      "blockClass": "pix-price"
    }
  },
  
  "product-spot-price-savings#pix": {
    "props": {
      "message": "Economize {spotPriceSavingsValue} no PIX",
      "blockClass": "pix-savings"
    }
  },
  
  "product-installments#electronics": {
    "props": {
      "message": "ou em até {installmentsNumber}x de {installmentValue} sem juros no cartão",
      "installmentsCriteria": "max-quantity-without-interest"
    }
  }
}
```

---

### Example 3: Marketplace with Seller

```json
{
  "flex-layout.col#price-marketplace": {
    "children": [
      "product-seller-name",
      "product-list-price",
      "product-selling-price",
      "product-installments"
    ]
  },
  
  "product-seller-name": {
    "props": {
      "message": "Vendido por: {sellerName}"
    }
  }
}
```

---

### Example 4: Async Search Results

```json
{
  "search-result-layout.desktop": {
    "children": [
      "breadcrumb.search",
      "search-title.v2",
      "search-content"
    ],
    "props": {
      "context": {
        "simulationBehavior": "skip",
        "skusFilter": "FIRST_AVAILABLE"
      }
    }
  },
  
  "search-content": {
    "blocks": ["gallery"]
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
      "product-price-suspense#search"
    ]
  },
  
  "product-price-suspense#search": {
    "props": {
      "Fallback": "rich-text#price-skeleton"
    },
    "children": [
      "flex-layout.col#price-complete"
    ]
  },
  
  "rich-text#price-skeleton": {
    "props": {
      "text": "⏳",
      "blockClass": "loading-skeleton"
    }
  },
  
  "flex-layout.col#price-complete": {
    "children": [
      "product-list-price",
      "product-selling-price",
      "product-spot-price",
      "product-installments"
    ]
  }
}
```

---

### Example 5: Unit of Measure Products

```json
{
  "product-selling-price#weight": {
    "props": {
      "message": "{sellingPriceWithUnitMultiplier}{hasMeasurementUnit, select, true { / {hasUnitMultiplier, select, true {{unitMultiplier}} false {}} {measurementUnit}} false {}}"
    }
  }
}
```

**Products with measurement:**
- `$15.99 / 500 g`
- `$8.50 / 2 kg`
- `$24.00 / 12 oz`

**Products without:**
- `$15.99`

---

## ⚠️ COMMON MISTAKES & SOLUTIONS

### Mistake 1: Using Deprecated Blocks

❌ **Wrong:**
```json
{
  "dependencies": {
    "vtex.product-summary": "2.x"
  }
}
```
```json
{
  "children": [
    "product-summary-price"  // DEPRECATED!
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

### Mistake 2: Not Using Async on Large Lists

❌ **Wrong:**
```json
{
  "search-result-layout": {
    "children": ["gallery"]
  },
  "gallery": {
    "blocks": ["product-summary.shelf"]
  },
  "product-summary.shelf": {
    // No async configuration
    "children": [
      "product-selling-price"
    ]
  }
}
```

✅ **Correct:**
```json
{
  "search-result-layout": {
    "props": {
      "context": {
        "simulationBehavior": "skip"
      }
    }
  },
  "product-summary.shelf": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-price-suspense"
    ]
  }
}
```

---

### Mistake 3: Missing Suspense with Async

❌ **Wrong:**
```json
{
  "product-summary.shelf": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
      "product-selling-price"  // Not wrapped in suspense!
    ]
  }
}
```

✅ **Correct:**
```json
{
  "product-summary.shelf": {
    "props": {
      "priceBehavior": "async"
    },
    "children": [
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

### Mistake 4: Wrong Installment Criteria

❌ **Wrong:**
```json
{
  "product-installments": {
    "props": {
      // Shows 24x with 5% interest instead of 10x interest-free
      "installmentsCriteria": "max-quantity"
    }
  }
}
```

✅ **Correct:**
```json
{
  "product-installments": {
    "props": {
      // Shows 10x interest-free
      "installmentsCriteria": "max-quantity-without-interest"
    }
  }
}
```

---

### Mistake 5: Hardcoding Price Text

❌ **Wrong:**
```json
{
  "product-selling-price": {
    "props": {
      "message": "Price: $79.90"  // Hardcoded!
    }
  }
}
```

✅ **Correct:**
```json
{
  "product-selling-price": {
    "props": {
      "message": "Price: {sellingPriceValue}"  // Dynamic!
    }
  }
}
```

---

## 📋 DECISION TREE

```
NEED TO DISPLAY PRODUCT PRICE?
│
├─ What type of price?
│  ├─ Original/From price → product-list-price
│  ├─ Current price → product-selling-price
│  ├─ Cash/PIX price → product-spot-price
│  ├─ Installments → product-installments
│  └─ Price range → product-selling-price-range
│
├─ Show savings?
│  ├─ Regular discount → product-price-savings
│  └─ PIX discount → product-spot-price-savings
│
├─ Performance concerns?
│  └─ Large lists → Use async prices
│     ├─ Set simulationBehavior: "skip"
│     ├─ Set priceBehavior: "async"
│     └─ Wrap in product-price-suspense
│
└─ Need customization?
   ├─ Custom text → Use message prop
   ├─ Site Editor → Use markers prop
   └─ Styling → Use CSS handles + blockClass
```

---

## ✅ CHECKLIST

**Before deploying prices:**

### Critical:
- [ ] Using `vtex.product-price` (NOT deprecated blocks)
- [ ] Price blocks have proper `message` props
- [ ] Async prices configured for large lists
- [ ] `product-price-suspense` used with async

### Performance:
- [ ] `simulationBehavior: "skip"` on search results
- [ ] `priceBehavior: "async"` on product summary
- [ ] Loading fallback configured
- [ ] Price range used for multi-SKU products

### User Experience:
- [ ] List price only shows when > selling price
- [ ] Installments show interest-free when available
- [ ] Spot price only shows when different
- [ ] Savings display threshold configured
- [ ] Messages are clear and localized

### Styling:
- [ ] CSS handles applied
- [ ] `blockClass` used for specific customization
- [ ] Prices visually distinct (list crossed, selling bold)
- [ ] Mobile responsive

---

## 🎓 KEY TAKEAWAYS

1. **Product Price is the only official price app** - Don't use deprecated blocks

2. **Async prices improve performance** - Essential for large product lists

3. **Every block has message variables** - Fully customizable with ICU format

4. **Conditional rendering is smart** - Blocks only render when relevant

5. **Three price types**:
   - List price (original)
   - Selling price (current)
   - Spot price (cash/PIX)

6. **Installment criteria matters**:
   - `max-quantity` - Most installments
   - `max-quantity-without-interest` - Most interest-free

7. **Use suspense with async** - Always wrap async prices in `product-price-suspense`

8. **Price ranges for multi-SKU** - Show "From X to Y" before SKU selection

---

## 🔗 RELATED GUIDES

- **Product Summary** - How to structure product cards
- **Search Result** - Search page configuration
- **Add to Cart Button** - Cart integration

---

**Official Documentation:**
- https://developers.vtex.com/docs/apps/vtex.product-price