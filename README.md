# Boutique Management System

A complete HTML/CSS/JavaScript based boutique management system with Selenium testing framework for managing dresses, orders, cart, and customer interactions.

## Tech Stack

- HTML5, CSS3, JavaScript
- jQuery & jQuery UI
- Selenium (Python for testing)
- Google Fonts

## Features

- **Home Page** - Product image slider with play/pause controls
- **Login System** - Form validation with jQuery dialog
- **Product Management** - Add new products with validation
- **Order Management** - Place customer orders
- **Shopping Cart** - Update quantity, remove items, checkout
- **About Us** - Boutique story, services, achievements
- **Contact Us** - Contact form with validation
- **Profile Page** - Complete boutique information
- **Responsive Design** - Mobile, tablet, desktop support

## Testing Framework

Python Selenium test cases for all pages:
- `Test_.py` - Login page (10 test cases)
- `home.py` - Home page slider testing
- `addproduct.py` - Add product form testing
- `order.py` - Order placement testing
- `cart.py` - Shopping cart functionality
- `contactUs.py` - Contact form testing
- `about.py` - About page testing
- `profile.py` - Profile page testing

## File Structure

```
boutique_management_system/
│
├── css/
│   └── style.css
│
├── images/
│   ├── b.jpg
│   └── bg.jpg
│
├── Home.html
├── Login.html
├── AddProduct.html
├── Orders.html
├── Cart.html
├── About.html
├── ContactUS.html
├── Profile.html
│
└── Test Files/
    ├── Test_.py
    ├── home.py
    ├── addproduct.py
    ├── order.py
    ├── cart.py
    ├── contactUs.py
    ├── about.py
    └── profile.py
```

## Pages Overview

| Page | Features |
|------|----------|
| Home.html | Auto image slider, play/pause buttons |
| Login.html | Username, email, password validation |
| AddProduct.html | Product name, price, quantity, category |
| Orders.html | Customer details, order placement |
| Cart.html | Quantity buttons, remove item, checkout |
| About.html | Story, services, achievements, gallery |
| ContactUS.html | Name, email, subject, message |
| Profile.html | Complete boutique profile |

## How to Run

1. Open any HTML file in a web browser
2. Start from `Home.html` or `Profile.html`

## Run Tests

```bash
python Test_.py
python home.py
python addproduct.py
# and so on...
```

---

*Boutique Management System - Front-end project with Selenium testing*
