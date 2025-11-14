import sqlite3


 # Connect to a file-based database
conn = sqlite3.connect("./mydatabase.db")
# conn = sqlite3.connect("./sqlitedb/mydatabase.db")

# Connect to an in-memory database
conn_in_memory = sqlite3.connect(":memory:")

def create_tables():
    cursor = conn.cursor()

    create_group_table_query = '''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            created_at DATE
        );
    '''

    # campos type e status serao enum
    create_bill_table_query = '''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            amount REAL,
            type TEXT,
            status TEXT,
            is_indefinite INTEGER DEFAULT 0, -- se '1', conta nunca "acaba"
            payment_date DATE,
            expiration_date DATE,

            group_id INTEGER,
            card_id INTEGER,
            installment_id INTEGER,

            FOREIGN KEY (group_id) REFERENCES groups(id),
            FOREIGN KEY (card_id) REFERENCES cards(id),
            FOREIGN KEY (installment_id) REFERENCES installments(id)
        );
    '''

    # tabela caso a conta for parcelada
    create_installment_query = '''
        CREATE TABLE IF NOT EXISTS installments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            installments_total INTEGER DEFAULT 1,
            installments_paid INTEGER DEFAULT 0,
            installment_value REAL DEFAULT 0,
            monthly_interest REAL DEFAULT 0, -- juros mensais aplicados -> em %

            bill_id INTEGER,

            FOREIGN KEY (bill_id) REFERENCES bills(id)
        );
    '''

    create_monthly_summary_table_query = '''
        CREATE TABLE IF NOT EXISTS monthly_summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month INTEGER,
            year INTEGER,
            total_expanses REAL,
            total_paid REAL,
            total_remaining REAL,
            updated_at DATE
        );
    '''

    create_card_query = '''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_name TEXT NOT NULL UNIQUE,
            bank TEXT,
            limit_amount REAL,
            owner_name TEXT,
            closing_day DATE,
            interest_rate REAL DEFAULT 0, -- juros mensais/rotativos do cartao
            due_day DATE,
            updated_at DATE
        );
    '''

    cursor.execute(create_group_table_query)
    cursor.execute(create_installment_query)
    cursor.execute(create_monthly_summary_table_query)
    cursor.execute(create_card_query)
    cursor.execute(create_bill_table_query)


if __name__ == "__main__":
    pass
