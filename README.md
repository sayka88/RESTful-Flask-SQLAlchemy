# E-Commerce System with RESTful API

## Description

This project is an e-commerce system with a RESTful API implemented using Flask and SQLAlchemy. The system allows managing products, customers, and orders through API endpoints.

## Functionality

- **Product Management:**
  - `GET /products` - Get a list of all products.
  - `POST /products` - Add a new product.

- **Customer Management:**
  - `GET /customers` - Get a list of all customers.
  - `POST /customers` - Add a new customer.

- **Customer Cart:**
  - `POST /customers/<customer_id>/cart` - Add a product to the customer's cart.
  - `GET /customers/<customer_id>/cart` - View the customer's cart.
  - `POST /customers/<customer_id>/checkout` - Place an order for the customer.

- **Order Management:**
  - `GET /orders` - Get a list of all orders.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sayka88/RESTful-Flask-SQLAlchemy.git
   cd your-repository
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Set up the database:

In the Python command line, run:


from app import app, db
with app.app_context():
    db.create_all()
Running
Run the Flask server:


flask run
The server will be available at http://127.0.0.1:5000.

Example Requests
Adding a product:


curl -X POST http://127.0.0.1:5000/products \
-H "Content-Type: application/json" \
-d '{"name": "product1", "price": 100.0}'
Adding a customer:


curl -X POST http://127.0.0.1:5000/customers \
-H "Content-Type: application/json" \
-d '{"name": "customer1"}'
Adding a product to the customer's cart:


curl -X POST http://127.0.0.1:5000/customers/1/cart \
-H "Content-Type: application/json" \
-d '{"product_id": 1}'
Placing an order:


curl -X POST http://127.0.0.1:5000/customers/1/checkout
Viewing the customer's cart:


curl -X GET http://127.0.0.1:5000/customers/1/cart
Getting a list of orders:


curl -X GET http://127.0.0.1:5000/orders
Project Structure
app.py - Main Flask application file.
models.py - Data model definitions.
requirements.txt - Project dependencies.
config.py - Flask application configuration.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions, you can contact [Sayyara] at [sayka.alekperova@gmail.com].


### Note

- Replace `https://github.com/sayka88/RESTful-Flask-SQLAlchemy.git` with the URL of your repository.
- Add or modify sections according to the specifics of your project.
- Ensure that the files `app.py`, `models.py`, and `requirements.txt` are present in your project and configured correctly.

If you need to make any changes or additions, let me know!
