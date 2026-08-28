import sqlite3
from datetime import datetime
import os

class CustomerDatabaseManager:
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
            create table if not exists customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            created_at TEXT
            )
""")
        self.connection.commit()

    def add_customer(self, name, email, phone, address):
        created_at = datetime.now().isoformat()
        self.cursor.execute("""
            Insert into customers(name, email, phone, address, created_at) values(?, ?, ?, ?, ?)
""", (name, email, phone, address, created_at))

        self.connection.commit()