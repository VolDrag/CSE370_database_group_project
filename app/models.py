
from mysql.connector import connect, Error

# Database connection function
def get_db_connection():
    return connect(
        host='localhost',
        user='Sheldon_C',
        password='Hofstader',
        database='stuarts_comic_shop'
    )

# -------------------------------
# User Model Functions
# -------------------------------

# Create a new user
def create_user(username, email, password, address, role='customer', loyalty_points=0):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO user (username, email, password, address, role, loyalty_points)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (username, email, password, address, role, loyalty_points))
    connection.commit()
    cursor.close()
    connection.close()

# Get user by user_id
def get_user_by_id(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM user WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()  # Fetch one user
    cursor.close()
    connection.close()

    return user  # Returns a tuple with user data

# -------------------------------
# ComicCon Event Model Functions
# -------------------------------

# Create a new ComicCon event
def create_comiccon_event(event_name, event_date, location, points_required):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO comiccon (event_name, event_date, location, points_required)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (event_name, event_date, location, points_required))
    connection.commit()
    cursor.close()
    connection.close()

# Get all ComicCon events
def get_all_comiccon_events():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM comiccon"
    cursor.execute(query)
    events = cursor.fetchall()  # Fetch all events
    cursor.close()
    connection.close()

    return events  # Returns a list of tuples

# -------------------------------
# Registration (User-ComicCon) Model Functions
# -------------------------------

# Register a user for a ComicCon event
def register_for_event(user_id, event_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO registration (user_id, event_id)
    VALUES (%s, %s)
    """
    cursor.execute(query, (user_id, event_id))
    connection.commit()
    cursor.close()
    connection.close()

# Get registrations for a specific ComicCon event
def get_event_registrations(event_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    SELECT u.username, u.email
    FROM user u
    JOIN registration r ON u.user_id = r.user_id
    WHERE r.event_id = %s
    """
    cursor.execute(query, (event_id,))
    registrations = cursor.fetchall()  # Fetch all registrations for the event
    cursor.close()
    connection.close()

    return registrations  # Returns a list of tuples

# -------------------------------
# Product Model Functions
# -------------------------------

# Create a new product (comic or collectible)
def create_product(title, price, product_type):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO product (title, price, type)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (title, price, product_type))
    connection.commit()
    cursor.close()
    connection.close()

# Get all products
def get_all_products():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM product"
    cursor.execute(query)
    products = cursor.fetchall()  # Fetch all products
    cursor.close()
    connection.close()

    return products  # Returns a list of tuples

# -------------------------------
# Order Model Functions
# -------------------------------

# Create a new order
def create_order(user_id, total_amount):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO orders (user_id, total_amount)
    VALUES (%s, %s)
    """
    cursor.execute(query, (user_id, total_amount))
    connection.commit()
    cursor.close()
    connection.close()

# -------------------------------
# OrderItem Model Functions (Includes relationship between Order and Product)
# -------------------------------

# Add a product to an order (includes relationship)
def add_product_to_order(order_id, product_id, quantity):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO order_item (order_id, product_id, quantity)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (order_id, product_id, quantity))
    connection.commit()
    cursor.close()
    connection.close()

# -------------------------------
# Review Model Functions
# -------------------------------

# Create a new review for a product
def create_review(user_id, product_id, rating, comment):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO review (user_id, product_id, rating, comment)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, product_id, rating, comment))
    connection.commit()
    cursor.close()
    connection.close()

# Get all reviews for a product
def get_product_reviews(product_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    SELECT r.rating, r.comment, u.username
    FROM review r
    JOIN user u ON r.user_id = u.user_id
    WHERE r.product_id = %s
    """
    cursor.execute(query, (product_id,))
    reviews = cursor.fetchall()  # Fetch all reviews for the product
    cursor.close()
    connection.close()

    return reviews  # Returns a list of tuples