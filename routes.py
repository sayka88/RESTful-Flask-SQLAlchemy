from flask import Flask, request, jsonify
from models import db, Product, Customer, Order, Cart, OrderProduct

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

    @app.route('/products', methods=['POST'])
    def add_product():
        data = request.get_json()
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'id': product.id}), 201

    @app.route('/customers', methods=['GET'])
    def get_customers():
        customers = Customer.query.all()
        return jsonify([{'id': c.id, 'name': c.name} for c in customers])

    @app.route('/customers', methods=['POST'])
    def add_customer():
        data = request.get_json()
        customer = Customer(name=data['name'])
        db.session.add(customer)
        db.session.commit()
        return jsonify({'id': customer.id}), 201

    @app.route('/customers/<int:customer_id>/cart', methods=['POST'])
    def add_to_cart(customer_id):
        data = request.get_json()
        product = Product.query.get(data['product_id'])
        customer = Customer.query.get(customer_id)
        customer.cart.append(product)
        db.session.commit()
        return '', 204

    @app.route('/customers/<int:customer_id>/cart', methods=['GET'])
    def view_cart(customer_id):
        customer = Customer.query.get(customer_id)
        cart = customer.cart
        return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in cart])

    @app.route('/customers/<int:customer_id>/checkout', methods=['POST'])
    def checkout(customer_id):
        customer = Customer.query.get(customer_id)
        order = Order(customer_id=customer_id)
        for product in customer.cart:
            order.products.append(product)
        customer.cart = []
        db.session.add(order)
        db.session.commit()
        return jsonify({'order_id': order.id}), 201

    @app.route('/orders', methods=['GET'])
    def get_orders():
        orders = Order.query.all()
        return jsonify([{'id': o.id, 'customer_id': o.customer_id} for o in orders])

    return app
