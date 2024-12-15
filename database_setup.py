import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create the inventory table
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    quantity REAL NOT NULL,
    price REAL NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database setup complete.")
