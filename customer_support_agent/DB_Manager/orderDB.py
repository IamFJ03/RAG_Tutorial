import sqlite3
import random
import string
class OrderDatabaseManager:
    def __init__(self, db_name="customer_support_database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        create table if not exists orders(
            order_id TEXT PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            delivery_date TEXT,
            status TEXT NOT NULL,
            total_amount REAL NOT NULL,
            payment_method TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
""")

        self.connection.commit()

    def add_order(self, customer_id, order_date, delivery_date, status, total_amount, payment_method):
        order_id = "ORD"+''.join(
            random.choices(string.ascii_uppercase + string.digits, k=4)
        )
        self.cursor.execute("""
            Insert into orders(order_id, customer_id, order_date, delivery_date, status, total_amount, payment_method) values(?, ?, ?, ?, ?, ?, ?)
""", (order_id, customer_id, order_date, delivery_date, status, total_amount, payment_method))

        self.connection.commit()
        
    def fetch_order_by_customer_id(self, customer_id):
        self.cursor.execute("select * from orders where customer_id = ?", (customer_id,))
        return self.cursor.fetchall()

    def fetch_order_by_id(self, order_id):
        self.cursor.execute("""
        SELECT
            o.order_id,
            o.customer_id,
            o.order_date,
            o.delivery_date,
            o.status,
            o.total_amount,
            o.payment_method,

            oi.item_id,
            oi.product_name,
            oi.product_category,
            oi.quantity,
            oi.unit_price,
            oi.product_condition

        FROM orders o
        LEFT JOIN orderItems oi
            ON o.order_id = oi.order_id

        WHERE o.order_id = ?
    """, (order_id,))
        return self.cursor.fetchall()

    def update_table(self, id, status):
        self.cursor.execute("""
            Update orders set status = ? where order_id = ?
""", (status, id))

        self.connection.commit()