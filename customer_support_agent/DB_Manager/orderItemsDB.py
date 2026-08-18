import sqlite3

class OrderItemDatabaseManager:
    def __init__(self, db_name="customer_support_database.db"):
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
        self.cursor.execute("select orders.delivery_date, orders.status, orderItems.item_id, orderItems.product_name, orderItems.product_category, orderItems.unit_price from orderItems Join orders on orderItems.order_id = orders.order_id WHERE orderItems.item_id = ?", (id,))
        return self.cursor.fetchone()