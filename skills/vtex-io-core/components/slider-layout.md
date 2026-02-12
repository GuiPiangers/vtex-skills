# SLIDER LAYOUT GUIDE

> Complete reference for building carousels and sliders in VTEX IO Store Framework

---

## 🎯 WHAT IS SLIDER LAYOUT?

Slider Layout is VTEX's **flexible carousel/slider solution** for displaying sliding content.

**Core concept:**
```
Slider Layout = Universal Carousel Builder
Can slide ANY block → Products, images, text, custom components
```

**Common Use Cases:**
- Product carousels (shelves)
- Banner rotators
- Category showcases
- Testimonial sliders
- Image galleries
- Multi-section synced sliders

---

## 🧱 AVAILABLE BLOCKS

### Core Blocks

| Block | Purpose | Required |
|-------|---------|----------|
| `slider-layout` | 🔴 **MANDATORY** - Main slider component | Yes |
| `slider-layout-group` | Syncs multiple sliders together | Optional |

**That's it!** Just two blocks, but incredibly flexible.

---

## 🚀 BASIC SETUP

### Step 1: Add Dependency

```json
{
  "dependencies": {
    "vtex.slider-layout": "0.x"
  }
}
```

### Step 2: Basic Slider

```json
{
  "slider-layout#basic": {
    "children": [
      "rich-text#slide1",
      "rich-text#slide2",
      "rich-text#slide3"
    ]
  },
  
  "rich-text#slide1": {
    "props": {
      "text": "Slide 1"
    }
  },
  "rich-text#slide2": {
    "props": {
      "text": "Slide 2"
    }
  },
  "rich-text#slide3": {
    "props": {
      "text": "Slide 3"
    }
  }
}
```

**That's it!** This creates a working slider.

---

## 📋 COMMON PATTERNS

### Pattern 1: Simple Product Carousel

```json
{
  "slider-layout#products": {
    "props": {
      "itemsPerPage": {
        "desktop": 4,
        "tablet": 3,
        "phone": 1
      },
      "infinite": true,
      "showNavigationArrows": "desktopOnly",
      "showPaginationDots": "never"
    },
    "children": ["product-summary.shelf"]
  }
}
```

**Use case:** Standard product shelf carousel

---

### Pattern 2: Banner Rotator

```json
{
  "slider-layout#banners": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "autoplay": {
        "timeout": 5000,
        "stopOnHover": true
      },
      "showNavigationArrows": "always",
      "showPaginationDots": "always"
    },
    "children": [
      "image#banner1",
      "image#banner2",
      "image#banner3"
    ]
  }
}
```

**Use case:** Auto-rotating homepage banners

---

### Pattern 3: Center Mode Gallery

```json
{
  "slider-layout#gallery": {
    "props": {
      "itemsPerPage": {
        "desktop": 3,
        "tablet": 2,
        "phone": 1
      },
      "centerMode": "center",
      "centerModeSlidesGap": 20,
      "infinite": true,
      "showNavigationArrows": "always"
    },
    "children": [
      "image#1",
      "image#2",
      "image#3",
      "image#4"
    ]
  }
}
```

**Use case:** Image galleries with peek preview

---

### Pattern 4: Text Testimonials

```json
{
  "slider-layout#testimonials": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "autoplay": {
        "timeout": 7000,
        "stopOnHover": true
      },
      "slideTransition": {
        "speed": 800,
        "delay": 0,
        "timing": "ease-in-out"
      }
    },
    "children": [
      "rich-text#testimonial1",
      "rich-text#testimonial2",
      "rich-text#testimonial3"
    ]
  }
}
```

**Use case:** Customer testimonials slider

---

## 🎛️ PROPS REFERENCE

### Navigation Props

| Prop | Type | Options | Default | Description |
|------|------|---------|---------|-------------|
| `showNavigationArrows` | `enum` | `always`, `never`, `mobileOnly`, `desktopOnly` | `always` | When to show arrows |
| `showPaginationDots` | `enum` | `always`, `never`, `mobileOnly`, `desktopOnly` | `always` | When to show dots |
| `navigationStep` | `number` or `"page"` | Any number or `"page"` | `"page"` | Items to scroll per arrow click |

**Examples:**

```json
// Hide arrows on mobile
{
  "showNavigationArrows": "desktopOnly"
}

// Hide dots everywhere
{
  "showPaginationDots": "never"
}

// Scroll 2 items per click
{
  "navigationStep": 2
}

// Scroll full page per click
{
  "navigationStep": "page"
}
```

---

### Layout Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `itemsPerPage` | `object` | `{desktop: 5, tablet: 3, phone: 1}` | Items shown per device |
| `fullWidth` | `boolean` | `true` | Slides occupy full width |
| `infinite` | `boolean` | `false` | Enable infinite loop |
| `usePagination` | `boolean` | `true` | Use pagination vs smooth scroll |

**itemsPerPage Object:**

```json
{
  "itemsPerPage": {
    "desktop": 4,  // Desktop screens
    "tablet": 2,   // Tablet screens
    "phone": 1     // Mobile screens
  }
}
```

**Important:** All three breakpoints must be defined!

---

### Center Mode Props

| Prop | Type | Options | Default | Description |
|------|------|---------|---------|-------------|
| `centerMode` | `enum` or `object` | `center`, `to-the-left`, `disabled` | `disabled` | Slide positioning |
| `centerModeSlidesGap` | `number` | Any number | `undefined` | Gap between slides (px) |

**Center Mode Options:**

| Value | Behavior |
|-------|----------|
| `disabled` | Normal slider (no peek) |
| `center` | Center slide, show peek of prev/next |
| `to-the-left` | Left align, show peek of next only |

**Responsive Center Mode:**

```json
{
  "centerMode": {
    "desktop": "center",
    "tablet": "to-the-left",
    "phone": "disabled"
  }
}
```

**With Gap:**

```json
{
  "centerMode": "center",
  "centerModeSlidesGap": 20  // 20px gap between slides
}
```

---

### Autoplay Props

| Prop | Type | Description |
|------|------|-------------|
| `autoplay` | `object` | Autoplay configuration |

**Autoplay Object:**

```json
{
  "autoplay": {
    "timeout": 5000,        // 5 seconds between slides
    "stopOnHover": true     // Pause on mouse hover
  }
}
```

**Disable Autoplay:**

```json
{
  "autoplay": undefined  // Or simply omit the prop
}
```

---

### Transition Props

| Prop | Type | Description |
|------|------|-------------|
| `slideTransition` | `object` | CSS transition settings |

**slideTransition Object:**

```json
{
  "slideTransition": {
    "speed": 400,              // Transition duration (ms)
    "delay": 0,                // Delay before transition (ms)
    "timing": "ease-in-out"    // CSS timing function
  }
}
```

**Timing Function Examples:**

```json
// Fast start, slow end
"timing": "ease-in"

// Slow start, fast end
"timing": "ease-out"

// Smooth both ends
"timing": "ease-in-out"

// Linear (constant speed)
"timing": "linear"

// Custom cubic-bezier
"timing": "cubic-bezier(0.4, 0, 0.2, 1)"
```

---

### Arrow Props

| Prop | Type | Description |
|------|------|-------------|
| `arrowSize` | `number` or `object` | Arrow dimensions (px) |

**Fixed Size:**

```json
{
  "arrowSize": 30  // 30x30 pixels on all devices
}
```

**Responsive Size:**

```json
{
  "arrowSize": {
    "desktop": 40,
    "tablet": 30,
    "phone": 25
  }
}
```

---

### Accessibility Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `string` | `"slider"` | aria-label for screen readers |

**Example:**

```json
{
  "label": "Featured Products Carousel"
}
```

---

## 🎯 REAL-WORLD EXAMPLES

### Example 1: Homepage Product Shelf

```json
{
  "slider-layout#home-shelf": {
    "props": {
      "itemsPerPage": {
        "desktop": 5,
        "tablet": 3,
        "phone": 2
      },
      "infinite": true,
      "showNavigationArrows": "always",
      "showPaginationDots": "never",
      "navigationStep": "page",
      "blockClass": "home-shelf"
    },
    "children": ["list-context.product-list#home"]
  },
  
  "list-context.product-list#home": {
    "blocks": ["product-summary.shelf#home"],
    "props": {
      "orderBy": "OrderByTopSaleDESC",
      "maxItems": 20
    }
  },
  
  "product-summary.shelf#home": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-selling-price",
      "add-to-cart-button"
    ]
  }
}
```

---

### Example 2: Auto-Rotating Hero Banners

```json
{
  "slider-layout#hero": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "autoplay": {
        "timeout": 6000,
        "stopOnHover": true
      },
      "slideTransition": {
        "speed": 600,
        "delay": 0,
        "timing": "ease-in-out"
      },
      "showNavigationArrows": "always",
      "showPaginationDots": "always",
      "fullWidth": true,
      "blockClass": "hero-slider"
    },
    "children": [
      "flex-layout.row#banner1",
      "flex-layout.row#banner2",
      "flex-layout.row#banner3"
    ]
  },
  
  "flex-layout.row#banner1": {
    "props": {
      "fullWidth": true
    },
    "children": ["image#hero1"]
  },
  
  "image#hero1": {
    "props": {
      "src": "assets/banner-1.jpg",
      "alt": "Summer Sale",
      "link": {
        "url": "/sale"
      }
    }
  }
}
```

---

### Example 3: Category Carousel with Peek

```json
{
  "slider-layout#categories": {
    "props": {
      "itemsPerPage": {
        "desktop": 4,
        "tablet": 2,
        "phone": 1
      },
      "centerMode": {
        "desktop": "center",
        "tablet": "to-the-left",
        "phone": "disabled"
      },
      "centerModeSlidesGap": 16,
      "infinite": true,
      "showNavigationArrows": "desktopOnly",
      "showPaginationDots": "mobileOnly",
      "blockClass": "category-slider"
    },
    "children": [
      "flex-layout.col#cat1",
      "flex-layout.col#cat2",
      "flex-layout.col#cat3",
      "flex-layout.col#cat4",
      "flex-layout.col#cat5"
    ]
  },
  
  "flex-layout.col#cat1": {
    "children": [
      "image#category1",
      "rich-text#category1"
    ]
  },
  
  "image#category1": {
    "props": {
      "src": "assets/category-electronics.jpg",
      "width": 300,
      "height": 300
    }
  },
  
  "rich-text#category1": {
    "props": {
      "text": "**Electronics**",
      "textAlignment": "CENTER"
    }
  }
}
```

---

### Example 4: Testimonials Slider

```json
{
  "slider-layout#testimonials": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "autoplay": {
        "timeout": 8000,
        "stopOnHover": true
      },
      "slideTransition": {
        "speed": 1000,
        "timing": "ease-in-out"
      },
      "showNavigationArrows": "never",
      "showPaginationDots": "always",
      "blockClass": "testimonials"
    },
    "children": [
      "flex-layout.col#testimonial1",
      "flex-layout.col#testimonial2",
      "flex-layout.col#testimonial3"
    ]
  },
  
  "flex-layout.col#testimonial1": {
    "props": {
      "blockClass": "testimonial-card"
    },
    "children": [
      "rich-text#quote1",
      "rich-text#author1"
    ]
  },
  
  "rich-text#quote1": {
    "props": {
      "text": "\"Amazing products and customer service!\"",
      "blockClass": "testimonial-quote"
    }
  },
  
  "rich-text#author1": {
    "props": {
      "text": "— John Doe, Verified Customer",
      "blockClass": "testimonial-author"
    }
  }
}
```

---

### Example 5: Image Gallery with Thumbnails (Synced)

```json
{
  "slider-layout-group#gallery": {
    "children": [
      "slider-layout#main-images",
      "slider-layout#thumbnails"
    ]
  },
  
  "slider-layout#main-images": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "showNavigationArrows": "always",
      "showPaginationDots": "never",
      "blockClass": "main-gallery"
    },
    "children": [
      "image#gallery1",
      "image#gallery2",
      "image#gallery3",
      "image#gallery4"
    ]
  },
  
  "slider-layout#thumbnails": {
    "props": {
      "itemsPerPage": {
        "desktop": 4,
        "tablet": 4,
        "phone": 3
      },
      "showNavigationArrows": "never",
      "showPaginationDots": "never",
      "blockClass": "thumbnail-gallery"
    },
    "children": [
      "image#thumb1",
      "image#thumb2",
      "image#thumb3",
      "image#thumb4"
    ]
  }
}
```

---

## 🔄 SLIDER LAYOUT GROUP (Advanced)

### What is Slider Layout Group?

`slider-layout-group` synchronizes multiple sliders to move together.

**Mental model:**
```
Main Gallery Slider    [Image 1] [Image 2] [Image 3]
                              ↕ SYNCED ↕
Thumbnail Slider      [Thumb 1] [Thumb 2] [Thumb 3]
```

When user clicks arrow on one slider, **both** sliders move.

### Basic Group Structure

```json
{
  "slider-layout-group#name": {
    "children": [
      "slider-layout#first",
      "slider-layout#second"
    ]
  }
}
```

### ⚠️ CRITICAL RULES

**All sliders in a group MUST have:**
- ✅ Same `itemsPerPage` configuration
- ✅ Same `infinite` setting
- ✅ Same `navigationStep`
- ✅ Same number of children
- ❌ Can differ in: `children` content, `blockClass`, visual props

**Example - CORRECT:**

```json
{
  "slider-layout-group#sync": {
    "children": ["slider-layout#A", "slider-layout#B"]
  },
  
  "slider-layout#A": {
    "props": {
      "itemsPerPage": {"desktop": 1, "tablet": 1, "phone": 1},
      "infinite": true
    },
    "children": ["image#1", "image#2", "image#3"]
  },
  
  "slider-layout#B": {
    "props": {
      "itemsPerPage": {"desktop": 1, "tablet": 1, "phone": 1},
      "infinite": true
    },
    "children": ["rich-text#1", "rich-text#2", "rich-text#3"]
  }
}
```

**Example - WRONG:**

```json
{
  "slider-layout#A": {
    "props": {
      "itemsPerPage": {"desktop": 1, "tablet": 1, "phone": 1}  // Different!
    }
  },
  
  "slider-layout#B": {
    "props": {
      "itemsPerPage": {"desktop": 2, "tablet": 2, "phone": 1}  // Different!
    }
  }
}
```

### Practical Use Cases

**1. Product Images + Thumbnails**

```json
{
  "slider-layout-group#product": {
    "children": [
      "slider-layout#images",
      "slider-layout#thumbs"
    ]
  }
}
```

**2. Multi-Language Content**

```json
{
  "slider-layout-group#multilang": {
    "children": [
      "slider-layout#english",
      "slider-layout#spanish"
    ]
  }
}
```

**3. Split Content Views**

```json
{
  "slider-layout-group#split": {
    "children": [
      "slider-layout#left-content",
      "slider-layout#right-content"
    ]
  }
}
```

---

## 🎨 CSS CUSTOMIZATION

### CSS Handles

```css
/* Container */
.sliderLayoutContainer { }
.sliderTrackContainer { }
.sliderTrack { }

/* Slides */
.slide { }
.slide--visible { }
.slide--hidden { }
.slide--firstVisible { }
.slide--lastVisible { }
.slideChildrenContainer { }

/* Navigation */
.sliderArrows { }
.sliderLeftArrow { }
.sliderRightArrow { }

/* Pagination */
.paginationDotsContainer { }
.paginationDot { }
.paginationDot--isActive { }
```

### Example Customizations

**Custom Arrow Styling:**

```css
.sliderLeftArrow,
.sliderRightArrow {
  background: rgba(0, 0, 0, 0.7);
  border-radius: 50%;
  padding: 12px;
  transition: all 0.3s;
}

.sliderLeftArrow:hover,
.sliderRightArrow:hover {
  background: rgba(0, 0, 0, 0.9);
  transform: scale(1.1);
}
```

**Custom Dots:**

```css
.paginationDotsContainer {
  margin-top: 20px;
}

.paginationDot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #ddd;
  margin: 0 6px;
  transition: all 0.3s;
}

.paginationDot--isActive {
  background: #000;
  width: 30px;
  border-radius: 6px;
}
```

**Slide Transitions:**

```css
.slide {
  opacity: 0.5;
  transition: opacity 0.3s;
}

.slide--visible {
  opacity: 1;
}

.slide--firstVisible {
  border-left: 3px solid #000;
}
```

**Center Mode Styling:**

```css
.sliderLayoutContainer[data-center-mode="center"] .slide--visible {
  transform: scale(1);
}

.sliderLayoutContainer[data-center-mode="center"] .slide:not(.slide--visible) {
  transform: scale(0.9);
  opacity: 0.6;
}
```

---

## 🔧 CONFIGURATION RECIPES

### Recipe 1: Smooth Auto-Carousel

```json
{
  "slider-layout#smooth": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "autoplay": {
        "timeout": 4000,
        "stopOnHover": false
      },
      "slideTransition": {
        "speed": 1200,
        "timing": "cubic-bezier(0.4, 0, 0.2, 1)"
      },
      "usePagination": true,
      "showNavigationArrows": "never",
      "showPaginationDots": "always"
    }
  }
}
```

---

### Recipe 2: Fast Product Showcase

```json
{
  "slider-layout#fast-products": {
    "props": {
      "itemsPerPage": {
        "desktop": 6,
        "tablet": 4,
        "phone": 2
      },
      "infinite": false,
      "navigationStep": 3,
      "slideTransition": {
        "speed": 300,
        "timing": "ease-out"
      },
      "showNavigationArrows": "desktopOnly",
      "showPaginationDots": "never"
    }
  }
}
```

---

### Recipe 3: Mobile-First Gallery

```json
{
  "slider-layout#mobile-gallery": {
    "props": {
      "itemsPerPage": {
        "desktop": 3,
        "tablet": 2,
        "phone": 1
      },
      "showNavigationArrows": {
        "desktop": "always",
        "tablet": "always",
        "phone": "never"
      },
      "showPaginationDots": {
        "desktop": "never",
        "tablet": "never",
        "phone": "always"
      },
      "infinite": true,
      "fullWidth": true
    }
  }
}
```

---

### Recipe 4: Peek-a-Boo Carousel

```json
{
  "slider-layout#peek": {
    "props": {
      "itemsPerPage": {
        "desktop": 3,
        "tablet": 2,
        "phone": 1
      },
      "centerMode": "center",
      "centerModeSlidesGap": 24,
      "infinite": true,
      "showNavigationArrows": "always",
      "fullWidth": false
    }
  }
}
```

---

## ⚠️ COMMON MISTAKES & SOLUTIONS

### Mistake 1: Forgetting Responsive Values

❌ **Wrong:**

```json
{
  "itemsPerPage": {
    "desktop": 4
    // Missing tablet and phone!
  }
}
```

✅ **Correct:**

```json
{
  "itemsPerPage": {
    "desktop": 4,
    "tablet": 3,
    "phone": 1
  }
}
```

---

### Mistake 2: Mismatched Group Configurations

❌ **Wrong:**

```json
{
  "slider-layout-group#bad": {
    "children": ["slider-layout#A", "slider-layout#B"]
  },
  "slider-layout#A": {
    "props": {
      "itemsPerPage": {"desktop": 1, "tablet": 1, "phone": 1}
    }
  },
  "slider-layout#B": {
    "props": {
      "itemsPerPage": {"desktop": 2, "tablet": 1, "phone": 1}  // Different!
    }
  }
}
```

✅ **Correct:**

```json
{
  "slider-layout#A": {
    "props": {
      "itemsPerPage": {"desktop": 1, "tablet": 1, "phone": 1}
    }
  },
  "slider-layout#B": {
    "props": {
      "itemsPerPage": {"desktop": 1, "tablet": 1, "phone": 1}  // Same!
    }
  }
}
```

---

### Mistake 3: Wrong Arrow Display Logic

❌ **Wrong:**

```json
{
  "showNavigationArrows": "mobile"  // Invalid value!
}
```

✅ **Correct:**

```json
{
  "showNavigationArrows": "mobileOnly"  // Valid values: always, never, mobileOnly, desktopOnly
}
```

---

### Mistake 4: Autoplay Without Timeout

❌ **Wrong:**

```json
{
  "autoplay": {
    "stopOnHover": true
    // Missing timeout!
  }
}
```

✅ **Correct:**

```json
{
  "autoplay": {
    "timeout": 5000,
    "stopOnHover": true
  }
}
```

---

### Mistake 5: Using Smooth Scroll with Pages

❌ **Wrong:**

```json
{
  "usePagination": false,  // Smooth scroll enabled
  "navigationStep": "page" // But trying to navigate by page!
}
```

✅ **Correct - Option 1 (Pagination):**

```json
{
  "usePagination": true,
  "navigationStep": "page"
}
```

✅ **Correct - Option 2 (Smooth Scroll):**

```json
{
  "usePagination": false,
  "navigationStep": 1  // Use number, not "page"
}
```

---

## 📋 DECISION TREE

```
BUILDING A SLIDER?
│
├─ What are you sliding?
│  ├─ Products → Use with list-context.product-list
│  ├─ Images → Use with image blocks
│  ├─ Text → Use with rich-text
│  └─ Mixed → Use with flex-layout blocks
│
├─ How many items visible?
│  └─ Configure itemsPerPage for each breakpoint
│
├─ Should it auto-rotate?
│  ├─ Yes → Set autoplay with timeout
│  └─ No → Omit autoplay prop
│
├─ Infinite loop?
│  ├─ Yes → infinite: true
│  └─ No → infinite: false
│
├─ Show peek of adjacent slides?
│  ├─ Yes → centerMode: "center" or "to-the-left"
│  └─ No → centerMode: "disabled"
│
├─ Navigation style?
│  ├─ Arrows only → showPaginationDots: "never"
│  ├─ Dots only → showNavigationArrows: "never"
│  └─ Both → showNavigationArrows: "always", showPaginationDots: "always"
│
└─ Need synced sliders?
   └─ Yes → Use slider-layout-group
```

---

## 🎓 PERFORMANCE TIPS

### 1. Limit Items Per Load

```json
{
  "itemsPerPage": {
    "desktop": 5  // Don't show 20+ items at once
  }
}
```

### 2. Use Lazy Loading for Images

```json
{
  "image#slide": {
    "props": {
      "loading": "lazy"
    }
  }
}
```

### 3. Optimize Autoplay Timeout

```json
{
  "autoplay": {
    "timeout": 5000  // Not too fast (causes jarring UX)
  }
}
```

### 4. Minimize Transition Speed

```json
{
  "slideTransition": {
    "speed": 400  // 300-500ms is optimal
  }
}
```

---

## ✅ CHECKLIST

**Before deploying slider:**

### Critical:
- [ ] `itemsPerPage` has all three breakpoints (desktop, tablet, phone)
- [ ] Slider has children blocks
- [ ] If using group, all sliders have matching configurations
- [ ] Navigation arrows/dots visibility configured
- [ ] Autoplay timeout set if using autoplay

### User Experience:
- [ ] Infinite loop enabled for product carousels
- [ ] stopOnHover enabled for autoplay sliders
- [ ] Appropriate transition speed (300-600ms)
- [ ] Arrow size appropriate for touch targets (min 30px)
- [ ] Accessible label provided

### Performance:
- [ ] Images use lazy loading
- [ ] Reasonable items per page count
- [ ] Transition timing optimized
- [ ] No excessive slides in DOM

### Styling:
- [ ] Custom CSS handles applied
- [ ] blockClass used for specific styling
- [ ] Arrows and dots styled appropriately
- [ ] Mobile responsive tested

---

## 🎓 KEY TAKEAWAYS

1. **Universal carousel builder** - Can slide ANY block type

2. **Responsive by default** - Must configure all breakpoints

3. **Two core blocks**:
   - `slider-layout` - The slider itself
   - `slider-layout-group` - Syncs multiple sliders

4. **Four navigation options**:
   - `always`, `never`, `mobileOnly`, `desktopOnly`

5. **Three center modes**:
   - `disabled`, `center`, `to-the-left`

6. **Autoplay is optional** - Configure timeout and stopOnHover

7. **Groups require matching configs** - Same props across all sliders

8. **Performance matters** - Limit items, optimize transitions

---

## 🔗 RELATED GUIDES

- **Product Summary** - `/mnt/skills/public/product-summary/SKILL.md` (for product carousels)
- **Flex Layout** - `/mnt/skills/public/flex-layout/SKILL.md` (for slide structure)
- **Responsive Layout** - Device-specific configurations

---

## 📚 QUICK REFERENCE

### Minimal Example

```json
{
  "slider-layout#basic": {
    "children": ["block1", "block2", "block3"]
  }
}
```

### Complete Example

```json
{
  "slider-layout#complete": {
    "props": {
      "label": "Product Carousel",
      "itemsPerPage": {
        "desktop": 4,
        "tablet": 3,
        "phone": 1
      },
      "infinite": true,
      "showNavigationArrows": "desktopOnly",
      "showPaginationDots": "mobileOnly",
      "navigationStep": "page",
      "autoplay": {
        "timeout": 5000,
        "stopOnHover": true
      },
      "slideTransition": {
        "speed": 400,
        "delay": 0,
        "timing": "ease-in-out"
      },
      "centerMode": "disabled",
      "fullWidth": true,
      "arrowSize": 30,
      "blockClass": "my-slider"
    },
    "children": ["slide1", "slide2", "slide3"]
  }
}
```

---

**Official Documentation:**
- https://developers.vtex.com/docs/apps/vtex.slider-layout