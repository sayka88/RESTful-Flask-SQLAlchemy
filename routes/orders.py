from flask import Blueprint, request, jsonify
from models import db, CartItem, Order

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{"id": o.id, "customer_id": o.customer_id} for o in orders]), 200

@bp.route('/<int:customer_id>/checkout', methods=['POST'])
def checkout(customer_id):
    items = CartItem.query.filter_by(customer_id=customer_id).all()
    if not items:
        return jsonify({"error": "Корзина пуста"}), 400
    
    order = Order(customer_id=customer_id)
    db.session.add(order)
    db.session.commit()

    for item in items:
        item.order = order
        db.session.commit()

    CartItem.query.filter_by(customer_id=customer_id).delete()
    db.session.commit()

    return jsonify({"order_id": order.id, "items": [{"product_id": item.product_id, "quantity": item.quantity} for item in items]}), 201

