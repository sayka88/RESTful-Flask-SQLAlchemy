from flask import Blueprint, request, jsonify
from models import db, Product

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products]), 200

@bp.route('', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"id": new_product.id, "name": new_product.name, "price": new_product.price}), 201

