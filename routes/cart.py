from flask import Blueprint, request, jsonify
from models import db, CartItem

bp = Blueprint('cart', __name__, url_prefix='/customers/<int:customer_id>/cart')

@bp.route('', methods=['POST'])
def add_to_cart(customer_id):
    data = request.get_json()
    new_item = CartItem(product_id=data['product_id'], customer_id=customer_id, quantity=data['quantity'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"id": new_item.id, "product_id": new_item.product_id, "quantity": new_item.quantity}), 201

@bp.route('', methods=['GET'])
def view_cart(customer_id):
    items = CartItem.query.filter_by(customer_id=customer_id).all()
    return jsonify([{"id": item.id, "product_id": item.product_id, "quantity": item.quantity} for item in items]), 200

