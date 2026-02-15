import argparse
import os
from datetime import date
from database import init_db, add_expense, get_all_expenses

DATA_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "calendarium")
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "expenses.db")

def fmt(val):
    """ text formatting for --view output """
    if val is None:
        return ""
    if isinstance(val, float): 
        return f"{val:.2f}" # string cast float and limit output to two decimals
    return str(val)

def main():
    parser = argparse.ArgumentParser(description="Calendarium — expense tracker")
    parser.add_argument("--add", metavar="CATEGORY", help="add expense under this category")
    parser.add_argument("--amount", type=float, help="cost in kroner")
    parser.add_argument("--comment", help="description of the expense")
    parser.add_argument("--date", help="override date (YYYY-MM-DD), defaults to today")
    parser.add_argument("--view", action="store_true", help="show all entries")
    args = parser.parse_args()

    conn = init_db(DB_PATH)

    if args.view:
        columns, rows = get_all_expenses(conn)
        if not rows:
            print("no recorded expenses")
            conn.close()
            return
        str_rows = [[fmt(val) for val in row] for row in rows]

        widths = []

        for col_index in range(len(columns)):
            header_width = len(columns[col_index])
            data_width = max(len(row[col_index]) for row in str_rows)
            widths.append(max(header_width, data_width) + 2)

        header = "".join(col.ljust(w) for col, w in zip(columns, widths))

        print(header)
        print("-" * len(header))
        
        for row in str_rows:
            line = "".join(val.ljust(w) for val,w in zip(row, widths))

            print(line)

    elif args.add:
        if args.amount is None: #originally if not args.amount, this also catches 0.
            print("--amount required, that is kind of the whole point")
        else:
            expense_date = args.date if args.date else date.today().isoformat()
            add_expense(conn, expense_date, args.amount, args.add, args.comment)

    else:
        parser.print_help()

    conn.close()


if __name__ == "__main__":
    main()
