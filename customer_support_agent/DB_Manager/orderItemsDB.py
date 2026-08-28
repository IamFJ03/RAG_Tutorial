import sqlite3
import os
class OrderItemDatabaseManager:
    def __init__(self, db_name=None):
        if db_name is None:
            db_name = os.getenv(
                "DB_PATH",
                "customer_support_database.db"
                )
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists orderItems(
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT NOT NULL,
            product_name TEXT NOT NULL,
            product_category TEXT,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            product_condition TEXT DEFAULT 'Good',
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
            )
""")

        self.connection.commit()

    def add_order_items(self, order_id, product_name, product_category, quantity, unit_price):
        self.cursor.execute("""
            Insert into orderItems( order_id, product_name, product_category, quantity, unit_price) values( ?, ?, ?, ?, ?)
""", ( order_id, product_name, product_category, quantity, unit_price))
        self.connection.commit()
    
    def fetch_order_items_by_id(self, order_id):
        self.cursor.execute("select * from orderItems where order_id = ?", (order_id,))
        return self.cursor.fetchall()

    def fetch_item_by_id(self, id):
        self.cursor.execute("""
        SELECT
            oi.item_id,
            oi.order_id,
            oi.product_name,
            oi.product_category,
            oi.quantity,
            oi.unit_price,
            oi.product_condition,

            o.customer_id,
            o.order_date,
            o.delivery_date,
            o.status,
            o.total_amount,
            o.payment_method

        FROM orderItems oi
        JOIN orders o
            ON oi.order_id = o.order_id

        WHERE oi.item_id = ?
    """, (id,))
        return self.cursor.fetchone()