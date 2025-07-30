# seed_buses.py
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
            "price": 100,
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