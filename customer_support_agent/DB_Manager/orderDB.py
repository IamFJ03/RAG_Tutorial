import sqlite3

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

    def fetch_order_by_customer_id(self, customer_id):
        self.cursor.execute("select * from orders where customer_id = ?", (customer_id))
        return self.cursor.fetchall()