from flask import Blueprint, jsonify
from app.models import Bus

bp = Blueprint("buses", __name__)

@bp.route("/", methods=["GET"])
def list_buses():
    buses = Bus.query.all()
    return jsonify([
        {
            "id": b.id,
            "name": b.name,
            "route": b.route,
            "seats": b.seats,
            "price": b.price, 
            "image_url": b.image_url
        } for b in buses
    ])
