from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Booking, Bus
from app import db
from flask_cors import cross_origin

bp = Blueprint("bookings", __name__, url_prefix="/api/bookings")


@bp.route("", methods=["POST", "OPTIONS"]) 
@bp.route("/", methods=["POST", "OPTIONS"])
@cross_origin()  
@jwt_required()
def book_bus():
    if request.method == "OPTIONS":
        
        return '', 200

    user_id = get_jwt_identity()
    data = request.json
    bus_id = data.get("bus_id")
    seats_requested = data.get("seats", 1)

    if not bus_id or seats_requested <= 0:
        return jsonify({"message": "Invalid bus ID or number of seats"}), 400

    bus = Bus.query.get(bus_id)
    if not bus:
        return jsonify({"message": "Bus not found"}), 404

    if bus.seats < seats_requested:
        return jsonify({"message": "Not enough seats available"}), 400

    # Deduct seats
    bus.seats -= seats_requested

    # Record booking
    booking = Booking(user_id=user_id, bus_id=bus.id, seats=seats_requested)
    db.session.add(booking)
    db.session.commit()

    return jsonify({
        "message": "Booking successful",
        "bus": bus.name,
        "seats_booked": seats_requested,
        "remaining_seats": bus.seats
    }), 201


@bp.route("/", methods=["GET", "OPTIONS"])
@cross_origin()
@jwt_required()
def get_my_bookings():
    if request.method == "OPTIONS":
        return '', 200

    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()

    results = []
    for b in bookings:
        results.append({
            
            "bus_name": b.bus.name,
            "route": b.bus.route,
            "seats_booked": b.seats,
            "total_price": b.seats * b.bus.price,
            "image_url": b.bus.image_url
        })

    return jsonify(results), 200
