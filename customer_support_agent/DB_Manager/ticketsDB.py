import sqlite3

class TicketDatabaseManager:
    def __init__(self, db_name="customer_support_database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists tickets(
            ticket_id TEXT primary key,
            type TEXT NOT NULL,
            customer_id TEXT,
            order_id TEXT,
            item_id TEXT NOT NULL,
            status TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL
            )
""")