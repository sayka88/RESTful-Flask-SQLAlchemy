from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
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

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)

# Создание таблиц
def create_tables():
    db.create_all()
    print("Database tables created.")

# Роуты для продуктов
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'id': new_product.id, 'name': new_product.name, 'price': new_product.price}), 201

# Роуты для клиентов
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in customers])

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    new_customer = Customer(name=data['name'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'id': new_customer.id, 'name': new_customer.name}), 201

# Роуты для корзины клиента
@app.route('/customers/<int:customer_id>/cart', methods=['POST'])
def add_to_cart(customer_id):
    data = request.json
    new_cart_item = Cart(customer_id=customer_id, product_id=data['product_id'])
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify({'message': 'Product added to cart'}), 201

@app.route('/customers/<int:customer_id>/cart', methods=['GET'])
def view_cart(customer_id):
    cart_items = Cart.query.filter_by(customer_id=customer_id).all()
    products = [{'product_id': ci.product_id} for ci in cart_items]
    return jsonify({'products': products})

# Роуты для оформления заказа
@app.route('/customers/<int:customer_id>/checkout', methods=['POST'])
def checkout(customer_id):
    new_order = Order(customer_id=customer_id)
    db.session.add(new_order)
    db.session.commit()

    cart_items = Cart.query.filter_by(customer_id=customer_id).all()
    for item in cart_items:
        order_product = OrderProduct(order_id=new_order.id, product_id=item.product_id)
        db.session.add(order_product)
        db.session.delete(item)  # Удаление каждого элемента корзины

    db.session.commit()
    
    return jsonify({'message': 'Order created'}), 201

# Роуты для заказов
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': o.id, 'customer_id': o.customer_id} for o in orders])

# Главная функция
if __name__ == '__main__':
    with app.app_context():
        create_tables()  # Создание таблиц перед запуском приложения
    app.run(debug=True, port=5001)
