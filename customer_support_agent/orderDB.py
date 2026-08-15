import sqlite3

class OrderDatabaseManager:
    def __init__(self, db_name="customer_support_database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
        create table if not exists orders(
            order_id TEXT PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            product_category TEXT,
            order_date TEXT NOT NULL,
            delivery_date TEXT,
            status TEXT NOT NULL,
            amount REAL NOT NULL,
            payment_method TEXT,
            product_condition TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
""")

        self.connection.commit()