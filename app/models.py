from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(80), nullable=True)  # Add this
    profile_picture = db.Column(db.String(255), nullable=True)  # Add this
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
    seats = db.Column(db.Integer, nullable=False)  # total seats
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)

    bookings = db.relationship("Booking", backref="bus", lazy=True)

    def to_dict(self):
        # Sum up all seats booked for this bus
        booked_seats = sum(booking.seats for booking in self.bookings)
        seats_available = self.seats - booked_seats

        return {
            "id": self.id,
            "name": self.name,
            "route": self.route,
            "seats": self.seats,
            "seats_available": seats_available,
            "price": self.price,
            "image_url": self.image_url
        }


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"), nullable=False)
    seats = db.Column(db.Integer, nullable=False)  # seats booked

    user = db.relationship("User", backref="bookings")
