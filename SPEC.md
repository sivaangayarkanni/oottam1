# Oottam - E-commerce Platform Specification

## 1. Project Overview

- **Project Name**: Oottam E-commerce Platform
- **Project Type**: Full-stack e-commerce web application
- **Core Functionality**: E-commerce platform for selling healthy, preservative-free instant foods (multipurpose flour) with 3D forest/food themed visuals
- **Target Users**: Busy professionals, health-conscious families, students, transition users

---

## 2. Technology Stack

### Backend
- **Framework**: Flask 3.x (Python)
- **Database**: SQLite (SQLAlchemy ORM)
- **Session**: Flask sessions with secure cookies
- **Forms**: Flask-WTF for validation

### Frontend
- **HTML5/CSS3**: Custom themed responsive design
- **JavaScript**: Vanilla JS with Three.js for 3D effects
- **3D Library**: Three.js for forest/food 3D visualizations
- **Animations**: CSS animations + GSAP for smooth transitions
- **Icons**: Lucide icons

### Key Libraries
- Flask, Flask-SQLAlchemy, Flask-WTF
- Three.js (3D rendering)
- GSAP (animations)

---

## 3. UI/UX Specification

### Color Palette
| Role | Color | Hex Code |
|------|-------|---------|
| Primary (Forest Green) | Deep Forest | `#1B4332` |
| Secondary (Leaf Green) | Fresh Leaf | `#2D6A4F` |
| Accent (Warm Gold) | Harvest | `#D4A574` |
| Background | Cream | `#FAF7F2` |
| Surface | Warm White | `#FFFFFF` |
| Text Primary | Charcoal | `#1A1A1A` |
| Text Secondary | Warm Gray | `#5C5C5C` |
| Success | Herb Green | `#40916C` |
| Error | Terracotta | `#C8544C` |

### Typography
- **Display Font**: "Playfair Display" (headings - elegant, premium)
- **Body Font**: "DM Sans" (body - clean, modern)
- **Accent Font**: "Caveat" (handwritten touches - warm, human)

### Font Sizes
- H1: 56px / 3.5rem
- H2: 40px / 2.5rem
- H3: 28px / 1.75rem
- Body: 16px / 1rem
- Small: 14px / 0.875rem

### Spacing System
- Base unit: 8px
- Spacing scale: 4, 8, 16, 24, 32, 48, 64, 96px

### Responsive Breakpoints
- Mobile: 0-767px
- Tablet: 768-1023px
- Desktop: 1024px+

---

## 4. Page Specifications

### 4.1 Layout Structure (All Pages)

#### Header (Sticky)
- Logo (left): "Oottam" wordmark with leaf icon
- Navigation (center): Home, Products, About, Contact
- Cart indicator (right): Cart icon with item count badge

#### Footer
- Brand info
- Quick links
- Contact info
- Social links (placeholder)

### 4.2 Homepage

#### Hero Section
- Full-width with 3D animated forest background (Three.js particle trees)
- Main headline: "Fast Food, But Done Right"
- Subheadline: "Clean, preservative-free instant foods inspired by traditional nutrition"
- CTA Button: "Explore Products" → Products page
- Floating 3D flour sack animation

#### Story Section
- Problem statement with illustration
- Solution: Oottam's approach
- Visual: Clean icon grid showing "No Preservatives" | "Traditional Wisdom" | "Modern Convenience"

#### Product Preview
- Featured product cards (3 items)
- "View All Products" link

#### Features Section
- Four feature cards:
  1. "One Flour. Multiple Possibilities." - Multipurpose use
  2. "No Preservatives" - Clean ingredients
  3. "Ready in Minutes" - Quick preparation
  4. "Traditional Wisdom" - Rooted in heritage

#### CTA Section
- "Ready to taste the difference?"
- Newsletter signup (optional)

### 4.3 Products Page

#### Header
- Page title: "Our Products"
- Breadcrumb: Home > Products

#### Filters
- Filter sidebar (collapsible on mobile):
  - Type: All, Multipurpose Flour, Instant Mix
  - Flavor: Original, Multigrain, Ragi, Rice

#### Product Grid
- Responsive grid: 1 col mobile, 2 col tablet, 3 col desktop
- Product card:
  - Product image (placeholder with 3D effect)
  - Product name
  - Short description
  - Price
  - "Add to Cart" button

### 4.4 Product Detail Page

#### Product Hero
- Large product image with 3D floating effect
- Product name, price
- Quick add to cart section
- Quantity selector

#### Details Section
- "What You Can Make" - Use cases (Roti, Dosa, Porridge, Snacks, Quick Meals)
- "Ingredients" - Full list with benefits explanation
- "How to Use" - Simple instructions

#### Related Products
- 3 related product cards

### 4.5 Cart Page

#### Cart Items
- Product thumbnail
- Product name
- Quantity selector (+/-)
- Item price
- Remove button
- Running total

#### Cart Summary
- Subtotal
- Shipping estimate
- Total
- "Proceed to Checkout" button

### 4.6 Checkout Page

#### Form Sections
- Contact Information
- Shipping Address
- Payment (placeholder - mock only)

#### Order Summary
- Items list
- Total

#### Trust Elements
- "Secure checkout" badge
- "30-day guarantee" text

### 4.7 About Page

#### Brand Story
- "Our Story" section
- The problem Oottam solves
- The solution
- Mission statement
- Vision statement

#### Team/Values
- Brand values grid:
  - Transparency
  - Quality
  - Tradition
  - Innovation

### 4.8 Contact Page

#### Form
- Name field
- Email field
- Subject field
- Message field
- Submit button

#### Contact Info
- Email: hello@oottam.in (placeholder)
- Phone: (placeholder)

---

## 5. Functionality Specification

### Core Features
1. **Product Catalog**: View all products with filtering
2. **Product Details**: View individual product information
3. **Shopping Cart**: Add/remove items, update quantities
4. **Checkout**: Mock checkout form (no real payments)
5. **Session Persistence**: Cart persists across pages

### User Interactions
- Smooth scroll navigation
- Add to cart with feedback animation
- Filter products by type and flavor
- Quantity +/- controls
- Form validation with error messages

### Data Handling
- Products stored in SQLite database
- Cart stored in session
- Checkout form - mock only (no real submission)

---

## 6. 3D/Animation Specification

### Three.js Scenes

#### Hero Forest (Homepage)
- Procedural trees using cones/cylinders
- Particle system for floating leaves/seeds
- Ambient color: forest greens
- Subtle camera animation

#### Product Display
- Floating flour sack/packet
- Gentle rotation animation
- Soft shadows

### CSS Animations
- Button hover: subtle scale + color shift
- Card hover: lift effect with shadow
- Page transitions: fade in
- Cart update: bounce animation on badge

---

## 7. Folder Structure

```
oottam/
├── app.py                 # Main Flask application
├── config.py             # Configuration
├── models.py             # Database models
├── forms.py              # WTForms
├── requirements.txt      # Dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   ├── main.js       # Main JavaScript
│   │   ├── three-scene.js # Three.js scene
│   │   └── cart.js      # Cart functionality
│   └── images/           # (placeholder folder)
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Homepage
    ├── products.html    # Products page
    ├── product.html     # Product detail
    ├── cart.html        # Cart page
    ├── checkout.html    # Checkout page
    ├── about.html       # About page
    └── contact.html     # Contact page
```

---

## 8. Acceptance Criteria

### Visual
- [ ] Forest-themed color palette applied consistently
- [ ] 3D effects visible on homepage hero
- [ ] Product cards display properly with hover effects
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Typography matches spec (Playfair Display, DM Sans)

### Functionality
- [ ] All 6 pages navigate correctly
- [ ] Product filtering works
- [ ] Add to cart updates badge count
- [ ] Quantity +/- works in cart
- [ ] Remove from cart works
- [ ] Cart persists during session

### Performance
- [ ] Pages load without errors
- [ ] 3D animations run smoothly
- [ ] No console errors

### Content
- [ ] Brand copy matches Oottam's voice
- [ ] Product descriptions are unique (not placeholder lorem)
- [ ] All sections have appropriate content