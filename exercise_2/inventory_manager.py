# inventory_manager.py

def format_currency(amount):
    return f"${amount:.2f}"

def display_inventory_value(inventory):
    total_value = sum(item["price"] * item["stock"] for item in inventory.values())
    print(f"\nCurrent Inventory Value: {format_currency(total_value)}\n")

def display_low_stock(inventory):
    low_stock_items = [name for name, data in inventory.items() if data["stock"] <= 5]
    if low_stock_items:
        print("⚠️ LOW STOCK ALERT:")
        for item in low_stock_items:
            print(f"- {item} ({inventory[item]['stock']} units remaining)")
        print()

def add_new_item(inventory):
    name = input("Item name: ").strip()
    if name in inventory:
        print("Item already exists.")
        return
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Invalid price or stock value.")
        return
    category = input("Category: ").strip()
    inventory[name] = {"price": price, "stock": stock, "category": category}
    print(f"{name} added successfully!")

def update_stock(inventory):
    name = input("Item name: ").strip()
    if name not in inventory:
        print("Item not found.")
        return
    try:
        change = int(input("Enter stock to add/remove (use negative number to remove): "))
    except ValueError:
        print("Invalid input.")
        return
    inventory[name]["stock"] += change
    if inventory[name]["stock"] < 0:
        inventory[name]["stock"] = 0
    print(f"{name} stock updated. Current stock: {inventory[name]['stock']}")

def search_by_category(inventory):
    category = input("Category to search: ").strip()
    found = [name for name, data in inventory.items() if data["category"].lower() == category.lower()]
    if not found:
        print("No items found in this category.")
        return
    print(f"Found {len(found)} items in {category}:")
    for name in found:
        item = inventory[name]
        print(f"• {name} - {format_currency(item['price'])} ({item['stock']} in stock)")

def inventory_menu():
    inventory = {
        "Laptop": {"price": 999.99, "stock": 2, "category": "Electronics"},
        "Phone": {"price": 599.99, "stock": 15, "category": "Electronics"},
        "Mouse": {"price": 29.99, "stock": 3, "category": "Electronics"},
        "Chair": {"price": 85.50, "stock": 10, "category": "Furniture"}
    }

    while True:
        print("\n=== SMART INVENTORY MANAGER ===")
        display_inventory_value(inventory)
        display_low_stock(inventory)

        print("Menu:")
        print("1. Add new item")
        print("2. Update stock")
        print("3. Search items by category")
        print("4. Check low stock items")
        print("5. Calculate total inventory value")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_new_item(inventory)
        elif choice == "2":
            update_stock(inventory)
        elif choice == "3":
            search_by_category(inventory)
        elif choice == "4":
            display_low_stock(inventory)
        elif choice == "5":
            display_inventory_value(inventory)
        elif choice == "6":
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    inventory_menu()
