from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)
api = Api(app)

# Модели
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cart = db.relationship('Cart', backref='customer', lazy=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    products = db.relationship('Product', secondary='order_product')

class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)

# Ресурсы API
class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])
    
    def post(self):
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'id': new_product.id, 'name': new_product.name, 'price': new_product.price})

class CustomerResource(Resource):
    def get(self):
        customers = Customer.query.all()
        return jsonify([{'id': c.id, 'name': c.name} for c in customers])
    
    def post(self):
        data = request.get_json()
        new_customer = Customer(name=data['name'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'id': new_customer.id, 'name': new_customer.name})

class CartResource(Resource):
    def post(self, customer_id):
        data = request.get_json()
        new_cart_item = Cart(customer_id=customer_id, product_id=data['product_id'])
        db.session.add(new_cart_item)
        db.session.commit()
        return {'message': 'Product added to cart'}, 201
    
    def get(self, customer_id):
        cart_items = Cart.query.filter_by(customer_id=customer_id).all()
        products = [item.product_id for item in cart_items]
        return jsonify({'products': products})

class CheckoutResource(Resource):
    def post(self, customer_id):
        cart_items = Cart.query.filter_by(customer_id=customer_id).all()
        order = Order(customer_id=customer_id)
        for item in cart_items:
            order.products.append(Product.query.get(item.product_id))
            db.session.delete(item)
        db.session.add(order)
        db.session.commit()
        return {'message': 'Order created'}, 201

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return jsonify([{'id': o.id, 'customer_id': o.customer_id} for o in orders])

# Маршруты API
api.add_resource(ProductResource, '/products')
api.add_resource(CustomerResource, '/customers')
api.add_resource(CartResource, '/customers/<int:customer_id>/cart')
api.add_resource(CheckoutResource, '/customers/<int:customer_id>/checkout')
api.add_resource(OrderResource, '/orders')

if __name__ == '__main__':
    db.create_all()  # Создаем таблицы базы данных
    app.run(debug=True, port=5001)

