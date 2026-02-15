import sqlite3
from datetime import date


def init_db(path):
    """Connect to database and create table if needed. Returns connection."""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            description TEXT
        )
    """)
    conn.commit()
    return conn


def add_expense(conn, expense_date, amount, category, description):
    cursor = conn.cursor()
    amount = float(amount)
    cursor.execute("INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)",
        (expense_date, amount, category, description)
    )
    conn.commit()


def get_expenses_by_date(conn, target_date):
    """Fetch all expenses for a given date."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date = ?", (target_date,))
    return cursor.fetchall()


def get_all_expenses(conn):
    """Fetch all expenses. Returns (column_names, rows)."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date")
    columns = [desc[0] for desc in cursor.description]
    return columns, cursor.fetchall()


# --- Test it directly: python database.py ---
if __name__ == "__main__":
    conn = init_db("test_expenses.db")
    today = date.today().isoformat()

    add_expense(conn, today, 100.49, "beer", "avoided perishing from thirst")

    print("All expenses:")
    columns, rows = get_all_expenses(conn)
    for row in rows:
        print(row)

    conn.close()
