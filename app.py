from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Импортируем и регистрируем маршруты
from routes import products, customers, cart, orders

app.register_blueprint(products.bp)
app.register_blueprint(customers.bp)
app.register_blueprint(cart.bp)
app.register_blueprint(orders.bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

