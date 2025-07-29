from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Bus(db.Model):
    __tablename__ = "buses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    route = db.Column(db.String(200), nullable=False)
    seats = db.Column(db.Integer, nullable=False)         # stored as "seats" in DB
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "route": self.route,
            "seats": self.seats,  # exposed as availableSeats to frontend
            "price": self.price,
            "image_url": self.image_url
        }


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"), nullable=False)
    seats = db.Column(db.Integer, nullable=False)  # number of seats booked

    user = db.relationship("User", backref="bookings")
    bus = db.relationship("Bus", backref="bookings")
