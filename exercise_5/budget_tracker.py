import json   # For saving/loading data persistently
import os     # For file existence checks
from datetime import datetime  # To validate date inputs

DATA_FILE = "budget_data.json"  # File to store budget data

# Load data from JSON file or create a new one if not exists
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save current data back into JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Validate user date input in format YYYY-MM
def get_valid_month():
    while True:
        user_input = input("Enter month (YYYY-MM): ").strip()
        try:
            datetime.strptime(user_input, "%Y-%m")  # Validate format
            return user_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM.")

# Add income or expense entry into the budget data
def add_entry(data, month, entry_type):
    category = input(f"Enter {entry_type} category: ").strip()
    try:
        amount = float(input(f"Enter amount for {category}: "))
        if amount < 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    # Initialize structures if month or entry type is new
    if month not in data:
        data[month] = {"income": {}, "expenses": {}, "limits": {}}
    if category not in data[month][entry_type]:
        data[month][entry_type][category] = 0

    data[month][entry_type][category] += amount  # Add amount to category
    print(f"{entry_type.capitalize()} added: {category} - ${amount:.2f}")

# Set budget limit for specific expense categories
def set_budget_limit(data, month):
    category = input("Enter expense category to set limit: ").strip()
    try:
        limit = float(input(f"Set budget limit for {category}: "))
        if limit < 0:
            print("Limit must be positive.")
            return
    except ValueError:
        print("Invalid limit.")
        return

    if month not in data:
        data[month] = {"income": {}, "expenses": {}, "limits": {}}

    data[month]["limits"][category] = limit  # Store limit in the data structure
    print(f"Budget limit set: {category} - ${limit:.2f}")

# Display detailed monthly financial summary
def show_summary(data, month):
    if month not in data:
        print("No data found for this month.")
        return

    month_data = data[month]
    income_total = sum(month_data.get("income", {}).values())
    expense_total = sum(month_data.get("expenses", {}).values())
    net_savings = income_total - expense_total
    savings_percent = (net_savings / income_total * 100) if income_total else 0

    print("\n💰 FINANCIAL SUMMARY")
    print(f"Total Income: ${income_total:.2f}")
    print(f"Total Expenses: ${expense_total:.2f}")
    print(f"Net Savings: ${net_savings:.2f} ({savings_percent:.1f}%)")

    print("\n📊 EXPENSE BREAKDOWN")
    for category, amount in month_data.get("expenses", {}).items():
        percent = (amount / expense_total * 100) if expense_total else 0
        bars = '█' * int(percent // 5) + '░' * (20 - int(percent // 5))  # Text-based bar visualization
        print(f"{category:<12} {bars} ${amount:.0f} ({percent:.1f}%)")

    print("\n⚠️ BUDGET ALERTS:")
    alerts = False
    for category, limit in month_data.get("limits", {}).items():
        spent = month_data["expenses"].get(category, 0)
        if spent > limit:
            alerts = True
            over_budget = spent - limit
            percent_spent = (spent / limit) * 100
            print(f"{category}: ${over_budget:.0f} over budget ({percent_spent:.1f}% of limit)")
    if not alerts:
        print("No budget overruns.")

# Compare two months to see spending trends in categories
def analyze_trends(data):
    month1 = get_valid_month()
    month2 = get_valid_month()

    if month1 not in data or month2 not in data:
        print("One or both months not found.")
        return

    print(f"\n📈 SPENDING TREND: {month1} ➔ {month2}")
    categories = set(data[month1].get("expenses", {}).keys()) | set(data[month2].get("expenses", {}).keys())

    for category in categories:
        spent1 = data[month1].get("expenses", {}).get(category, 0)
        spent2 = data[month2].get("expenses", {}).get(category, 0)
        trend = "Increased" if spent2 > spent1 else "Decreased" if spent2 < spent1 else "No Change"
        diff = abs(spent2 - spent1)
        print(f"{category}: {trend} by ${diff:.2f}")

# Export monthly summary into a text file
def export_summary(data, month):
    if month not in data:
        print("No data found for this month.")
        return

    filename = f"{month}_summary.txt"
    with open(filename, 'w') as f:
        income_total = sum(data[month].get("income", {}).values())
        expense_total = sum(data[month].get("expenses", {}).values())
        net_savings = income_total - expense_total
        savings_percent = (net_savings / income_total * 100) if income_total else 0

        f.write(f"=== BUDGET SUMMARY: {month} ===\n")
        f.write(f"Total Income: ${income_total:.2f}\n")
        f.write(f"Total Expenses: ${expense_total:.2f}\n")
        f.write(f"Net Savings: ${net_savings:.2f} ({savings_percent:.1f}%)\n\n")

        f.write("Expense Breakdown:\n")
        for category, amount in data[month].get("expenses", {}).items():
            percent = (amount / expense_total * 100) if expense_total else 0
            f.write(f"{category}: ${amount:.2f} ({percent:.1f}%)\n")

        f.write("\nBudget Alerts:\n")
        for category, limit in data[month].get("limits", {}).items():
            spent = data[month]["expenses"].get(category, 0)
            if spent > limit:
                over_budget = spent - limit
                percent_spent = (spent / limit) * 100
                f.write(f"{category}: ${over_budget:.0f} over budget ({percent_spent:.1f}% of limit)\n")
    print(f"Summary exported to {filename}")

# Main menu loop to navigate through budget functionalities
def main():
    data = load_data()
    while True:
        print("\n=== PERSONAL BUDGET TRACKER ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget Limit")
        print("4. View Monthly Summary")
        print("5. Analyze Spending Trends")
        print("6. Export Monthly Summary")
        print("7. Exit")

        choice = input("Select an option: ").strip()

        if choice in ["1", "2", "3", "4", "6"]:
            month = get_valid_month()

        if choice == "1":
            add_entry(data, month, "income")
        elif choice == "2":
            add_entry(data, month, "expenses")
        elif choice == "3":
            set_budget_limit(data, month)
        elif choice == "4":
            show_summary(data, month)
        elif choice == "5":
            analyze_trends(data)
        elif choice == "6":
            export_summary(data, month)
        elif choice == "7":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
