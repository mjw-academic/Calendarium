# Finance-tracker calendar v0.5

python v3.14.2

# What it is
    A python based CLI personal expense tracker with sqlite database. 
    Based on the assumption that tracking pf made simple can build good habits.

# How it works
    cal-add <amount> <category> <comment(optional)> - Standard input, optimized for minimal friction, 
     and clarity of output.

        example: cal-add 500 Whiskey Redbreast-irishSP-12y

    cal-add -d <date[yyyy-mm-dd]> - adding past or future expenses by date
        example: cal-add -d 2026-02-03 486 delivery sushi-splurge

    cal-view - print full table of added expenses or history.
            
        example: 
        id  date        amount    category       description
    --------------------------------------------------------------------
        23  10.02       100.00    testingdate    datetesting
        19  2026-02-01  5000.00   rent           Husleie januar
        1   2026-02-07  12990.00  rent           Husleie februar
        2   2026-02-07  349.90    subscriptions  Spotify + iCloud

# Installation
    1. Clone the repo
        git clone <repo-url>
        cd Calendar

    2. Create and activate virtual environment
        python -m venv venv
        source venv/bin/activate

    3. Copy the CLI wrappers to somewhere in your PATH
        cp bin/cal-add bin/cal-view ~/.local/bin/
        chmod +x ~/.local/bin/cal-add ~/.local/bin/cal-view

    4. Run it — the database is created automatically on first use
        cal-add 149.90 groceries "Rema 1000"
        cal-view

    Data is stored in ~/.local/share/calendarium/expenses.db
    No pip dependencies required — sqlite3 and argparse are part of Python stdlib.

# Modules/libraries
    argparse - easy python definitions for writing and interpreting bash argument with helpful help text
    sqlite - local small database

# Files
    database.py - initialize and query functions
    main.py - calls to db.py for add and view


