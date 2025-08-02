# Function to format currency into $XX.XX style
def format_currency(amount):
    return f"${amount:.2f}"

# Add a new item to inventory
def add_item(inventory):
    name = input("Item name: ").strip()
    if name in inventory:
        print("Item already exists.")
        return
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        category = input("Category: ").strip()
        inventory[name] = {"price": price, "stock": stock, "category": category}
        print(f"{name} added successfully.")
    except ValueError:
        print("Invalid input.")

# Update stock by adding/removing quantities
def update_stock(inventory):
    name = input("Item name: ").strip()
    if name not in inventory:
        print("Item not found.")
        return
    try:
        qty = int(input("Add (+) or Remove (-) stock: "))
        inventory[name]["stock"] += qty  # Update stock count
        print(f"Updated stock for {name}: {inventory[name]['stock']} units.")
    except ValueError:
        print("Invalid input.")

# Search for items by category
def search_by_category(inventory):
    category = input("Category to search: ").strip()
    found = [name for name, details in inventory.items() if details["category"] == category]
    if not found:
        print("No items found in this category.")
    else:
        print(f"Found {len(found)} items in {category}:")
        for item in found:
            price = format_currency(inventory[item]["price"])
            stock = inventory[item]["stock"]
            print(f"• {item} - {price} ({stock} in stock)")

# Show low stock items (stock <= 5)
def check_low_stock(inventory):
    low_stock_items = [name for name, details in inventory.items() if details["stock"] <= 5]
    if not low_stock_items:
        print("No low stock items.")
    else:
        print("⚠️ LOW STOCK ALERT:")
        for item in low_stock_items:
            print(f"- {item} ({inventory[item]['stock']} units remaining)")

# Calculate total inventory value
def total_inventory_value(inventory):
    total = sum(details["price"] * details["stock"] for details in inventory.values())
    print(f"Current Inventory Value: {format_currency(total)}")

# Main interactive menu loop
def inventory_menu():
    inventory = {}  # Nested dictionary to hold inventory data

    while True:
        print("\n=== SMART INVENTORY MANAGER ===")
        total_inventory_value(inventory)
        check_low_stock(inventory)
        print("\n1. Add Item\n2. Update Stock\n3. Search by Category\n4. Exit")

        choice = input("Choose option: ").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_stock(inventory)
        elif choice == "3":
            search_by_category(inventory)
        elif choice == "4":
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    inventory_menu()
