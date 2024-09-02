from flask import Blueprint, request, jsonify
from models import db, Customer

bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{"id": c.id, "name": c.name, "email": c.email} for c in customers]), 200

@bp.route('', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"id": new_customer.id, "name": new_customer.name, "email": new_customer.email}), 201

