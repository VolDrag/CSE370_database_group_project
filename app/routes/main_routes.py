from flask import Blueprint, render_template

# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "<h1>Welcome to Stuart's Comic Shop!</h1>"











from flask import Blueprint, render_template, request, redirect, url_for
from app.models import create_user, get_user_by_id, create_comiccon_event, get_all_comiccon_events, create_product, get_all_products, create_order, add_product_to_order, create_review, get_product_reviews, register_for_event
from flask_login import login_user, login_required, current_user, logout_user

# Create the Blueprint
main = Blueprint('main', __name__)

# ---------------------------
# User Routes
# ---------------------------

# User Registration Route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        create_user(username, email, password, address)
        return redirect(url_for('main.login'))
    return render_template('register.html')

# User Profile Route
@main.route('/profile')
@login_required  # Ensure user is logged in
def profile():
    user = get_user_by_id(current_user.user_id)
    return render_template('profile.html', user=user)

# ---------------------------
# ComicCon Event Routes
# ---------------------------

# Create ComicCon Event (Admin route)
@main.route('/create_comiccon', methods=['GET', 'POST'])
@login_required  # Ensure user is logged in
def create_comiccon():
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        location = request.form['location']
        points_required = request.form['points_required']
        create_comiccon_event(event_name, event_date, location, points_required)
        return redirect(url_for('main.events'))
    return render_template('create_comiccon.html')

# View all ComicCon Events
@main.route('/events')
def events():
    events = get_all_comiccon_events()
    return render_template('events.html', events=events)

# Register for ComicCon Event
@main.route('/register_event/<int:event_id>', methods=['POST'])
@login_required  # Ensure user is logged in
def register_event(event_id):
    register_for_event(current_user.user_id, event_id)
    return redirect(url_for('main.events'))

# ---------------------------
# Product Routes
# ---------------------------

# View all Products
@main.route('/products')
def products():
    products = get_all_products()
    return render_template('products.html', products=products)

# Add Product (Admin route)
@main.route('/create_product', methods=['GET', 'POST'])
@login_required  # Ensure user is logged in
def create_product_route():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        product_type = request.form['type']
        create_product(title, price, product_type)
        return redirect(url_for('main.products'))
    return render_template('create_product.html')

# ---------------------------
# Order Routes
# ---------------------------

# Create an Order
@main.route('/create_order', methods=['GET', 'POST'])
@login_required  # Ensure user is logged in
def create_order_route():
    if request.method == 'POST':
        total_amount = request.form['total_amount']
        create_order(current_user.user_id, total_amount)
        return redirect(url_for('main.orders'))
    return render_template('create_order.html')

# Add Product to Order
@main.route('/add_to_order/<int:order_id>/<int:product_id>', methods=['POST'])
@login_required  # Ensure user is logged in
def add_to_order(order_id, product_id):
    quantity = request.form['quantity']
    add_product_to_order(order_id, product_id, quantity)
    return redirect(url_for('main.orders'))

# View Orders
@main.route('/orders')
@login_required  # Ensure user is logged in
def orders():
    # Replace this with a function that gets the user's orders
    user_orders = []  # For example, fetch orders related to the current user
    return render_template('orders.html', orders=user_orders)

# ---------------------------
# Review Routes
# ---------------------------

# Create a Product Review
@main.route('/create_review/<int:product_id>', methods=['GET', 'POST'])
@login_required  # Ensure user is logged in
def create_review_route(product_id):
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        create_review(current_user.user_id, product_id, rating, comment)
        return redirect(url_for('main.products'))
    return render_template('create_review.html', product_id=product_id)

# View Product Reviews
@main.route('/product_reviews/<int:product_id>')
def product_reviews(product_id):
    reviews = get_product_reviews(product_id)
    return render_template('product_reviews.html', reviews=reviews)