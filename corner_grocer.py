import json

# Define file path for inventory storage
inventory_file = 'inventory.json'

# Function to load inventory from the JSON file
def load_inventory():
    try:
        with open(inventory_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

# Function to save the current inventory to the JSON file
def save_inventory(inventory):
    with open(inventory_file, 'w') as file:
        json.dump(inventory, file, indent=4)

# Function to display inventory
def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print(f"{'Item Name':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for item in inventory:
            print(f"{item['name']:<20} ${item['price']:<10} {item['quantity']:<10}")
        print("-" * 40)

# Function to add a new item to the inventory
def add_item(inventory):
    name = input("Enter item name: ")
    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return
    try:
        quantity = int(input("Enter item quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a valid integer.")
        return
    
    item = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(item)
    save_inventory(inventory)
    print("Item added successfully!")

# Function to sort inventory by specified field
def sort_inventory(inventory, field):
    if field not in ['name', 'price', 'quantity']:
        print("Invalid sort field.")
        return
    inventory.sort(key=lambda x: x[field])
    print(f"Inventory sorted by {field.capitalize()}.")
    display_inventory(inventory)

# Main menu for user interaction
def main_menu():
    inventory = load_inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Sort Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            display_inventory(inventory)
        elif choice == '3':
            sort_field = input("Sort by (name, price, quantity): ").lower()
            sort_inventory(inventory, sort_field)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == '__main__':
    main_menu()
