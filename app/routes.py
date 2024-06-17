
from flask import Blueprint, request, jsonify, abort, render_template
from app import db, bcrypt, jwt
from app.models import User, Movie, Booking, FoodItem, Order
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from functools import wraps
from app.utils import send_email

bp = Blueprint('main', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid request'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(name=data['name'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid request'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'token': access_token}), 200

# Admin routes
@bp.route('/admin/movies', methods=['POST'])
@jwt_required()
def add_movie():
    # Add movie logic here
    pass

@bp.route('/admin/food-items', methods=['POST'])
@jwt_required()
def add_food_item():
    # Add food item logic here
    pass

@bp.route('/admin/bookings', methods=['GET'])
@jwt_required()
def get_bookings():
    # Get bookings logic here
    pass

# Movie booking route
@bp.route('/booking', methods=['GET'])
def booking():
    # Render the booking page
    return render_template('booking.html')

# Food ordering route
@bp.route('/food_order', methods=['GET'])
def food_order():
    # Render the food order page
    return render_template('food_order.html')

# Add food item route
@bp.route('/add_food_item', methods=['GET'])
@jwt_required()
def add_food_item_page():
    # Render the page to add a food item
    return render_template('add_food_item.html')

# Define other routes...
@bp.route('/example', methods=['GET'])
def example_route():
    # Example route logic here
    pass

# Index route
@bp.route('/')
def index():
    return jsonify({'message': 'Welcome to your Flask app!'})

# Add more routes here...
