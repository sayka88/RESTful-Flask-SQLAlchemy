from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Определение моделей
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('carts', lazy=True))
    product = db.relationship('Product', backref=db.backref('carts', lazy=True))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    items = db.relationship('OrderProduct', backref='order', lazy=True)

class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    product = db.relationship('Product', backref=db.backref('order_products', lazy=True))

# Функция создания таблиц
def create_tables():
    with app.app_context():
        db.create_all()
        print("Database tables created.")

# Импортируем и регистрируем маршруты
from routes import products, customers, cart, orders

app.register_blueprint(products.bp)
app.register_blueprint(customers.bp)
app.register_blueprint(cart.bp)
app.register_blueprint(orders.bp)

if __name__ == "__main__":
    with app.app_context():
        create_tables()
    app.run(port=5500, debug=True)
