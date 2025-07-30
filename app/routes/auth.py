import os
from flask import Blueprint, request, jsonify, current_app
from app.models import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bp = Blueprint("auth", __name__)

# ✅ Register route
@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return {"message": "User already exists"}, 400

    user = User(
        email=data["email"],
        username=data.get("username"),
        profile_picture=data.get("profile_picture")
    )
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully"}, 201

# ✅ Login route
@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        return {"message": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)
    return {
        "token": token,
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "profile_picture": user.profile_picture
        }
    }

# ✅ Get or update profile
@bp.route("/profile", methods=["GET", "PUT"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return {"message": "User not found"}, 404

    if request.method == "GET":
        return jsonify({
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "profile_picture": user.profile_picture
        })

    elif request.method == "PUT":
        if request.content_type.startswith("multipart/form-data"):
            # Handle file upload
            if "profile_picture" in request.files:
                image = request.files["profile_picture"]
                filename = f"profile_{user_id}_{image.filename}"
                upload_dir = os.path.join(current_app.root_path, "static", "uploads")
                os.makedirs(upload_dir, exist_ok=True)
                filepath = os.path.join(upload_dir, filename)
                image.save(filepath)
                user.profile_picture = f"/static/uploads/{filename}"
        else:
            # Handle JSON update
            data = request.json or {}
            if "username" in data:
                user.username = data["username"]
            if "profile_picture" in data:
                user.profile_picture = data["profile_picture"]

        db.session.commit()

        return {
            "message": "Profile updated",
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "profile_picture": user.profile_picture
            }
        }
