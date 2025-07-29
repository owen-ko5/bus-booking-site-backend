from app import create_app, db
from app.models import Bus

app = create_app()

with app.app_context():
    print("🧹 Resetting the database...")
    db.drop_all()
    db.create_all()


    buses = [
        {
            "name": "JOHN WICK",
            "route": "Nairobi → Rongai",
            "seats": 30,
            "price": 150,
            "image_url": "/static/images/Baba_yaga.jpg"
        },
        {
            "name": "Mood",
            "route": "Nairobi → Embakasi",
            "seats": 25,
            "price": 100,
            "image_url": "/static/images/Mood.jpg"
        },
        {
            "name": "Detroit 313",
            "route": "Nairobi → Rongai",
            "seats": 30,
            "price": 150,
            "image_url": "/static/images/Detroit 313.jpg"
        },
        {
            "name": "Bionic",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price":100,
            "image_url": "/static/images/Bionic.jpg"
        },
        {
            "name": "Brawlout",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Brawlout.jpg"
        },
        {
            "name": "Dethrone",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 80,
            "image_url": "/static/images/Dethrone.jpg"
        },
        {
            "name": "Ferrari",
            "route": "Nairobi → Rongai",
            "seats": 30,
            "price": 150,
            "image_url": "/static/images/Ferrari.jpg"
        },
        {
            "name": "Fortune",
            "route": "Nairobi → Rongai",
            "seats": 30,
            "price": 150,
            "image_url": "/static/images/Fortune.jpg"
        },
        {
            "name": "MoneyFest",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Moneyfest.jpg"
        },
        {
            "name": "Moxie Illz",
            "route": "Nairobi → Rongai",
            "seats": 30,
            "price": 150,
            "image_url": "/static/images/Moxillz.jpg"
        },
        {
            "name": "Opposite",
            "route": "Nairobi → Umoja",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Opposite.jpg"
        },
        {
            "name": "Plank",
            "route": "Nairobi → Umoja",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/plank.jpg"
        },
        {
            "name": "Restoration",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Restoration.jpg"
        },
        {
            "name": "Urban_Legends",
            "route": "Nairobi → Kitengela",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/urban_legends.jpg"
        },
        {
            "name": "X-trail",
            "route": "Nairobi → Kayole junction",
            "seats": 30,
            "price": 50,
            "image_url": "/static/images/X-trail.jpg"
        },
        {
            "name": "Xplicit",
            "route": "Nairobi → Ngong",
            "seats": 30,
            "price": 80,
            "image_url": "/static/images/Xplicit.jpg"
        },
        {
            "name": "Xtreme",
            "route": "Nairobi → Kitengela",
            "seats": 30,
            "price": 80,
            "image_url": "/static/images/Xtreme.jpg"
        },
        {
            "name": "X-trail",
            "route": "Nairobi → Kayole junction",
            "seats": 30,
            "price": 50,
            "image_url": "/static/images/X-trail.jpg"
        },
        {
            "name": "Phenomenal",
            "route": "Nairobi → Ngong",
            "seats": 30,
            "price": 80,
            "image_url": "/static/images/Phenomenal.jpg"
        },
        {
            "name": "Dice",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Dice.jpg"
        },
        {
            "name": "Jinx",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Jinx.jpg"
        },
        {
            "name": "Heartless",
            "route": "Nairobi → Embakasi",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Heartless.jpg"
        },
        {
            "name": "Detox",
            "route": "Nairobi → Umoja",
            "seats": 30,
            "price": 100,
            "image_url": "/static/images/Detox.jpg"
        },
        {
            "name": "Harukaze 1",
            "route": "Nairobi → Ngong",
            "seats": 30,
            "price": 80,
            "image_url": "/static/images/Harukaze 1.jpg"
        }
    ]

    for b in buses:
        bus = Bus(**b)
        db.session.add(bus)

    db.session.commit()
    print("✅ Buses seeded!")
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
