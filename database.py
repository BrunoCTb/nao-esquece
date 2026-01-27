# database.py
import sqlite3

class Database:
    def __init__(self, db_path="./mydatabase.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row


    def get_connection(self):
        return self.conn


    def create_tables(conn):
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                created_at DATE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                amount REAL,
                type TEXT,
                status TEXT,
                is_indefinite INTEGER DEFAULT 0,
                payment_date DATE,
                expiration_date DATE,
                group_id INTEGER,
                card_id INTEGER,
                installment_id INTEGER,
                FOREIGN KEY (group_id) REFERENCES groups(id),
                FOREIGN KEY (card_id) REFERENCES cards(id),
                FOREIGN KEY (installment_id) REFERENCES installments(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS installments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                installments_total INTEGER DEFAULT 1,
                installments_paid INTEGER DEFAULT 0,
                installment_value REAL DEFAULT 0,
                monthly_interest REAL DEFAULT 0,
                bill_id INTEGER,
                FOREIGN KEY (bill_id) REFERENCES bills(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS monthly_summaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                month INTEGER,
                year INTEGER,
                total_expanses REAL,
                total_paid REAL,
                total_remaining REAL,
                updated_at DATE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_name TEXT NOT NULL UNIQUE,
                bank TEXT,
                limit_amount REAL,
                owner_name TEXT,
                closing_day DATE,
                interest_rate REAL DEFAULT 0,
                due_day DATE,
                updated_at DATE
            );
        """)

        conn.commit()

