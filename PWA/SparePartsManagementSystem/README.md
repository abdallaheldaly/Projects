# Auto Parts Store Management System

A comprehensive, offline-first inventory management system designed specifically for auto parts stores. Built with pure HTML, CSS, and JavaScript - no backend required, no internet needed after initial load.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Any%20Device-green.svg)
![Offline](https://img.shields.io/badge/offline-ready-success.svg)

---

## 🎯 Live Demo

**Try it now:** [https://abdallaheldaly.github.io/Projects/PWA/SparePartsManagementSystem/%D9%86%D8%B8%D8%A7%D9%85_%D8%A7%D8%AF%D8%A7%D8%B1%D8%A9_%D9%82%D8%B7%D8%B9_%D8%A7%D9%84%D8%BA%D9%8A%D8%A7%D8%B1.html](https://abdallaheldaly.github.io/Projects/PWA/SparePartsManagementSystem/%D9%86%D8%B8%D8%A7%D9%85_%D8%A7%D8%AF%D8%A7%D8%B1%D8%A9_%D9%82%D8%B7%D8%B9_%D8%A7%D9%84%D8%BA%D9%8A%D8%A7%D8%B1.html)

*No installation required - works instantly in your browser!*

---

## ✨ Features

### 📦 Inventory Management
- **Add/Edit/Delete Products** - Full CRUD operations for your inventory
- **Smart Search** - Search by product name, code, company, or car model
- **Stock Status Tracking** - Automatic categorization: Available, Low Stock, Out of Stock
- **Multi-field Product Details**:
- Product code
- Product name
- Quantity in stock
- Manufacturer/Company
- Manufacturing type (Korean, Chinese, Taiwanese, etc.)
- Car model compatibility
- Base price and selling price with service fee calculation

### 📊 Dashboard & Analytics
- **Real-time Statistics**:
- Total products count
- Total items in stock
- Products by status (Available/Low/Out of Stock)
- Inventory value (cost basis)
- Inventory value (selling price)
- Expected profit calculation

### 💰 Pricing System
- **Automatic Price Calculation** - Base price × Service fee = Selling price
- **Customizable Service Fees** - Set different markup rates per product
- **EGP Currency** - Egyptian Pound formatting with Arabic numerals

### 🔍 Advanced Filtering
- **Quick Filters**:
- All products
- In Stock (quantity &gt; 2)
- Low Stock (quantity 1-2)
- Out of Stock (quantity = 0)

### 💾 Data Persistence
- **Local Storage** - All data saved locally in browser
- **Export to JSON** - Backup your entire inventory
- **Import from JSON** - Restore data or migrate between devices
- **Reset to Defaults** - Restore initial sample data
- **Clear All** - Empty entire inventory with confirmation

### 🎨 User Interface
- **RTL Arabic Interface** - Fully right-to-left optimized
- **Responsive Design** - Works on mobile, tablet, and desktop
- **Clean Modern UI** - Professional styling with intuitive navigation
- **Toast Notifications** - Non-intrusive success/error messages

---

## 🚀 Quick Start

### Option 1: Try Online (Instant)
👉 **[Open Live Demo](https://abdallaheldaly.github.io/Projects/PWA/SparePartsManagementSystem/%D9%86%D8%B8%D8%A7%D9%85_%D8%A7%D8%AF%D8%A7%D8%B1%D8%A9_%D9%82%D8%B7%D8%B9_%D8%A7%D9%84%D8%BA%D9%8A%D8%A7%D8%B1.html)**

### Option 2: Direct Open (Offline)
1. Save the HTML file to your computer
2. Double-click to open in any modern browser
3. Start managing your inventory immediately!

### Option 3: Mobile Installation (Recommended)
**Android:**
1. Open the file in Chrome
2. Tap menu (⋮) → **"Add to Home screen"**
3. Launch as standalone app

**iOS:**
1. Open in Safari
2. Tap Share → **"Add to Home Screen"**

---

## 📸 Screenshots

| Dashboard | Product List | Add Product |
|-----------|--------------|-------------|
| ![Dashboard](screenshots/dashboard.png) | ![Products](screenshots/products.png) | ![Add](screenshots/add.png) |

*Screenshots show the system with sample data*

---

## 📖 User Guide

### Adding a New Product
1. Click **"Add Product"** button (top right)
2. Fill in the required fields:
 - Product Name (required)
 - Quantity (required)
 - Base Price (required)
 - Service Fee (default: 1.20 = 20% markup)
3. Selling price calculates automatically
4. Click **Save**

### Editing a Product
1. Find the product in the table
2. Click **Edit** button
3. Modify fields as needed
4. Click **Save**

### Searching Products
- Type in the search box to filter by:
- Product name
- Product code
- Company name
- Car model

### Managing Stock
- **Green badge** = Good stock (&gt; 2 items)
- **Yellow badge** = Low stock (1-2 items)
- **Red badge** = Out of stock (0 items)

### Data Backup
1. Click **Export** to download JSON backup
2. Store file safely
3. To restore: Click **Import** and select your JSON file

---

## 🛠️ Technical Details

### Architecture
- **Single File Application** - Everything in one HTML file
- **No Dependencies** - Pure vanilla JavaScript
- **No Build Process** - Just save and open
- **Client-side Storage** - Uses localStorage API

### Data Structure
```javascript
{
id: "unique-timestamp",
itemCode: "product-code",
name: "Product Name",
quantity: 10,
company: "Manufacturer",
manufactureType: "Korean/Chinese/etc",
basePrice: 100.00,
serviceFee: 1.20,
sellingPrice: 120.00,
carModel: "Compatible Models"
}