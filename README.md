# E-Commerce System with RESTful API

## Description

This project is an e-commerce system with a RESTful API implemented using Flask and SQLAlchemy. The system allows you to manage products, customers, and orders through API endpoints.

## Features

- **Product Management:**
  - `GET /products` - Retrieve a list of all products.
  - `POST /products` - Add a new product.

- **Customer Management:**
  - `GET /customers` - Retrieve a list of all customers.
  - `POST /customers` - Add a new customer.

- **Customer Cart:**
  - `POST /customers/<customer_id>/cart` - Add a product to the customer's cart.
  - `GET /customers/<customer_id>/cart` - View the customer's cart.
  - `POST /customers/<customer_id>/checkout` - Checkout the customer's cart and create an order.

- **Order Management:**
  - `GET /orders` - Retrieve a list of all orders.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sayka88/RESTful-Flask-SQLAlchemy.git
   cd RESTful-Flask-SQLAlchemy
2. Create and activate a virtual environment:

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install dependencies:
   ```bash
     pip install -r requirements.txt
4. Set up the database:
     In a Python shell, run:
     ```bash
       from app import app, db
       with app.app_context():
       db.create_all()

## Running

Start the Flask server:

      ```bash
          flask run
The server will be available at http://127.0.0.1:5000.

## Example Requests
Add a Product:

      ```bash
          curl -X POST http://127.0.0.1:5000/products \
          -H "Content-Type: application/json" \
          -d '{"name": "product1", "price": 100.0}'

Add a Customer:

      ```bash
          curl -X POST http://127.0.0.1:5000/customers \
          -H "Content-Type: application/json" \
          -d '{"name": "customer1"}'



Add a Product to Customer's Cart:

      ```bash
          curl -X POST http://127.0.0.1:5000/customers/1/cart \
          -H "Content-Type: application/json" \
          -d '{"product_id": 1}'
          
Checkout an Order:

      ```bash
          curl -X POST http://127.0.0.1:5000/customers/1/checkout
          View Customer's Cart:

bash
Копировать код
curl -X GET http://127.0.0.1:5000/customers/1/cart
Retrieve List of Orders:

bash
Копировать код
curl -X GET http://127.0.0.1:5000/orders
Project Structure
app.py - Main Flask application file.
models.py - Data model definitions.
requirements.txt - Project dependencies.
config.py - Flask application configuration.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contacts
If you have any questions, you can contact [your name] at [your email].



