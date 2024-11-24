# CornerGrocer
Inventory Management System

This project is an Inventory Management System with a web interface that allows users to add, view, and remove products from the inventory. The goal is to modernize and improve a previous C++ console application by creating a more interactive and user-friendly web application.

Features

Add Products: Users can add new products to the inventory by entering the product name, quantity, and price.
View Inventory: A table displays all products currently in the inventory, showing the product name, quantity, price, and an option to remove items.
Remove Products: Users can remove products from the inventory by clicking a "Remove" button next to each product.
Tech Stack
HTML: The structure and layout of the web pages.
CSS: Styling for the web pages, including the layout and design of forms and tables.
JavaScript: Provides interactivity, including adding and removing products from the inventory.
Local Storage (in later steps): For saving inventory data across page reloads (when adding a backend).

Getting Started

Prerequisites
To run this project locally, you will need:

A web browser to view and interact with the application.
Code editor (e.g., Visual Studio Code, Sublime Text, etc.) to edit the code.

Installation
Clone the repository to your local machine 

Usage

Add New Product: Fill in the fields for product name, quantity, and price, then click "Add Product" to add it to the inventory.
View Inventory: The inventory will be displayed in a table with product names, quantities, and prices. Each product will have a "Remove" button that allows you to remove the product from the list.
Remove Product: Click the "Remove" button next to a product to delete it from the inventory list.

Example of Inventory

Product Name	Quantity	Price	Actions
Apple	10	$1.00	Remove
Banana	15	$0.50	Remove

Future Enhancements

Database Integration: In later phases, we will integrate a backend (Node.js) and connect to a database (SQLite or MongoDB) to persist the data across sessions.
Stock Alerts: Introduce visual indicators for low stock levels to alert users when items are running low.
Search and Filter: Implement search functionality to filter the inventory by product name, quantity, or price.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.