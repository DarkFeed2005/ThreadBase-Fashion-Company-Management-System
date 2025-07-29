import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        port=3306,
        user="sql12792490",
        password="b8dbuseU3e",
        database="sql12792490"
    )

# User Operations
def verify_user(username, password):
    try:
        with connect_db() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                (username, password)
            )
            return cursor.fetchone()
    except Exception as e:
        print(f"Database error: {e}")
        return None

def add_user(user_data):
    try:
        with connect_db() as db:
            cursor = db.cursor()
            cursor.execute(
                """INSERT INTO users 
                (username, password, first_name, last_name, email, 
                 contact, address, nic, role)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    user_data["username"],
                    user_data["password"],  # No hashing here
                    user_data["first_name"],
                    user_data["last_name"],
                    user_data["email"],
                    user_data["contact"],
                    user_data["address"],
                    user_data["nic"],
                    user_data["role"]
                )
            )
            db.commit()
            return True
    except Exception as e:
        print(f"Database error: {e}")
        return False

def get_all_users():
    try:
        with connect_db() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    except Exception as e:
        print(f"Database error: {e}")
        return []

def delete_user(user_id):
    try:
        with connect_db() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            db.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Database error: {e}")
        return False

# Design Operations
def add_design(design_data):
    try:
        with connect_db() as db:
            cursor = db.cursor()
            cursor.execute(
                """INSERT INTO designs 
                (name, materials, price, designer)
                VALUES (%s, %s, %s, %s)""",
                (
                    design_data["name"],
                    design_data["materials"],
                    design_data["price"],
                    design_data["designer"]
                )
            )
            db.commit()
            return True
    except Exception as e:
        print(f"Database error: {e}")
        return False

def get_designs_by_designer(designer):
    try:
        with connect_db() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM designs WHERE designer = %s", (designer,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Database error: {e}")
        return []

# Sales Operations
def add_sale(sale_data):
    try:
        with connect_db() as db:
            cursor = db.cursor()
            cursor.execute(
                """INSERT INTO sales 
                (design_id, quantity, total, customer_info, sales_person)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    sale_data["design_id"],
                    sale_data["quantity"],
                    sale_data["total"],
                    sale_data["customer_info"],
                    sale_data["sales_person"]
                )
            )
            db.commit()
            return True
    except Exception as e:
        print(f"Database error: {e}")
        return False

def get_all_sales():
    try:
        with connect_db() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM sales")
            return cursor.fetchall()
    except Exception as e:
        print(f"Database error: {e}")
        return []