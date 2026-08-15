import sqlite3

class OrderItemDatabaseManager:
    def __init__(self, db_name="customer_support_database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

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