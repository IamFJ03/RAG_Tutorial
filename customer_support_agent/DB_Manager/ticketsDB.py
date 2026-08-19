import sqlite3

class TicketDatabaseManager:
    def __init__(self, db_name="customer_support_database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            customer_id TEXT NOT NULL,
            order_id TEXT,
            item_id TEXT NOT NULL,
            status TEXT NOT NULL CHECK (
                status IN ('open', 'in_progress', 'resolved', 'closed')
            ),
            description TEXT,
            created_at TEXT NOT NULL,
        
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            );
        """)