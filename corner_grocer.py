import sqlite3

# Define database file
DB_FILE = 'inventory.db'

# Database setup
def setup_database():
    """Initialize the database and create the inventory table if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                name TEXT PRIMARY KEY,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
    print("Database setup complete.")

# Function to display inventory
def display_inventory():
    """Fetch and display all items in the inventory."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM inventory ORDER BY name')
        inventory = cursor.fetchall()

    if not inventory:
        print("Inventory is empty.")
    else:
        print(f"{'Item Name':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for item in inventory:
            print(f"{item[0]:<20} ${item[1]:<10.2f} {item[2]:<10}")
        print("-" * 40)

# Function to add a new item
def add_item():
    """Prompt user to add a new item to the inventory."""
    name = input("Enter item name: ")
    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return
    try:
        quantity = int(input("Enter item quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO inventory (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
            print(f"Item '{name}' added successfully!")
        except sqlite3.IntegrityError:
            print(f"Item '{name}' already exists in the inventory.")

# Function to sort inventory
def sort_inventory(order_by):
    """Display inventory sorted by the given field."""
    valid_fields = {'name', 'price', 'quantity'}
    if order_by not in valid_fields:
        print("Invalid sort field.")
        return

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM inventory ORDER BY {order_by}')
        sorted_inventory = cursor.fetchall()

    print(f"Inventory sorted by {order_by.capitalize()}:")
    display_inventory()

# Function to update an item
def update_item():
    """Prompt user to update an existing item's price or quantity."""
    name = input("Enter the item name to update: ")
    try:
        price = input("Enter new price (leave blank to skip): ")
        quantity = input("Enter new quantity (leave blank to skip): ")

        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            if price:
                cursor.execute('UPDATE inventory SET price = ? WHERE name = ?', (float(price), name))
            if quantity:
                cursor.execute('UPDATE inventory SET quantity = ? WHERE name = ?', (int(quantity), name))
            print(f"Item '{name}' updated successfully!")
    except ValueError:
        print("Invalid input. Update failed.")

# Function to delete an item
def delete_item():
    """Prompt user to delete an item."""
    name = input("Enter the item name to delete: ")
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM inventory WHERE name = ?', (name,))
        print(f"Item '{name}' deleted successfully!")

# Main menu for user interaction
def main_menu():
    setup_database()
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Sort Inventory")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            sort_field = input("Sort by (name, price, quantity): ").lower()
            sort_inventory(sort_field)
        elif choice == '4':
            update_item()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == '__main__':
    main_menu()
