from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Booking, Bus

bp = Blueprint("profile", __name__)

@bp.route("/", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    bookings = Booking.query.filter_by(user_id=user.id).all()
    booking_data = []
    for b in bookings:
        bus = Bus.query.get(b.bus_id)
        booking_data.append({
            "bus": bus.name,
            "route": bus.route,
            "image_url": bus.image_url
        })

    return jsonify({
        "id": user.id,
        "email": user.email,
        "username": user.username,  # New
        "profile_picture": user.profile_picture,  # New
        "bookings": booking_data
    })
