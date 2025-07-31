# app/__init__.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # ✅ CORRECT CORS CONFIGURATION FOR PRODUCTION
    origins = [
        "https://bus-booking-app-git-main-owens-projects-41f58164.vercel.app",
        "https://bus-booking-app.vercel.app"  # Add clean domain
    ] if os.getenv("FLASK_ENV") == "production" else [
        "http://localhost:3000",
        "http://localhost:3001"
    ]

    CORS(
        app,
        resources={r"/api/*": {"origins": origins}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        expose_headers=["Content-Type", "Authorization"]
    )

    # JWT error handlers
    @jwt.unauthorized_loader
    def unauthorized_loader(reason):
        return jsonify({"message": "Unauthorized: Missing or invalid token"}), 401

    @jwt.invalid_token_loader
    def invalid_token_loader(reason):
        return jsonify({"message": "Invalid token"}), 422

    @jwt.expired_token_loader
    def expired_token_loader(jwt_header, jwt_payload):
        return jsonify({"message": "Token has expired"}), 401

    # Register Blueprints
    from app.routes import auth, buses, bookings, profile
    app.register_blueprint(auth.bp, url_prefix="/api/auth")
    app.register_blueprint(buses.bp, url_prefix="/api/buses")
    app.register_blueprint(bookings.bp, url_prefix="/api/bookings")
    app.register_blueprint(profile.bp, url_prefix="/api/profile")

    @app.route("/")
    def index():
        return jsonify({"message": "Bus Booking API is running"})

    return app