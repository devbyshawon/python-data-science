from datetime import datetime
import math

categories = ("Food", "Transport", "Education",
              "Shopping", "Healthcare", "Entertainment")

expenses = []  # list of dicts: {"id","date","category","description","amount"}

budgets = {}  # key: (year, month) tuple, value: budget amount


# Helper Functions
def find_expense(expense_id):
    expense_id = expense_id.strip().upper()
    for expense in expenses:
        if expense['id'] == expense_id:
            return expense
    return None


def read_date():
    while True:
        text = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            return datetime.strptime(text, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, e.g. 2026-11-01.")


def read_category():
    while True:
        print("Categories:", ", ".join(categories))
        choice = input("Enter category: ").strip().capitalize()
        if choice in categories:
            return choice
        print("Invalid category. Choose one from the list.")


def read_amount():
    while True:
        try:
            amount = float(input("Enter amount (৳): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if not math.isfinite(amount):
            print("Amount must be a finite number.")
            continue

        amount = round(amount, 2)
        if amount > 10_000_000:
            print("Amount is too large.")
            continue
        if amount > 0:
            return amount
        print("Amount must be greater than zero.")


# Feature 1
def add_expense():
    expense_id = input("Enter Expense ID: ").strip().upper()
    if not expense_id:
        print("Expense ID cannot be empty.")
        return

    if find_expense(expense_id) is not None:
        print(f"An expense with ID {expense_id} already exists.")
        return

    date = read_date()
    category = read_category()

    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    amount = read_amount()

    expense = {
        "id": expense_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    print(f"Expense {expense_id} added: {category}, ৳{amount:.2f}.")


# Feature 2
def shorten(text, width):
    if len(text) <= width:
        return text
    return text[:width - 3] + "..."


def print_expense_table(expense_list):
    print(f"{'ID':<8} {'Date':<12} {'Category':<14} "
          f"{'Description':<20} {'Amount':>10}")
    print("-" * 68)

    for expense in expense_list:
        print(
            f"{shorten(expense['id'], 8):<8} "
            f"{str(expense['date']):<12} "
            f"{expense['category']:<14} "
            f"{shorten(expense['description'], 20):<20} "
            f"{expense['amount']:>10.2f}"
        )


def display_all_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    print_expense_table(expenses)


# Feature 3
def show_results(results, empty_message):
    if not results:
        print(empty_message)
        return

    print(f"\nFound {len(results)} expense(s):")
    print_expense_table(results)


def search_by_id():
    expense_id = input("Enter Expense ID: ").strip()
    if not expense_id:
        print("Expense ID cannot be empty.")
        return
    expense = find_expense(expense_id)

    if expense is None:
        print(f"No expense found with ID {expense_id.upper()}.")
        return

    show_results([expense], "")


def search_by_category():
    category = read_category()
    results = []

    for expense in expenses:
        if expense['category'] == category:
            results.append(expense)

    show_results(results, f"No expenses found in category {category}.")


def search_by_date():
    target = read_date()
    results = []

    for expense in expenses:
        if expense['date'] == target:
            results.append(expense)
    show_results(results, f"No expenses found on {target}.")


def search_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nSearch / Filter")
    print("1. Search by ID")
    print("2. Filter by category")
    print("3. Filter by date")
    print("4. Back")

    choice = input("Enter your choice (1-4): ").strip()
    if choice == "1":
        search_by_id()
    elif choice == "2":
        search_by_category()
    elif choice == "3":
        search_by_date()
    elif choice == "4":
        return
    else:
        print("Invalid choice. Enter a number from 1 to 4.")
        return


# Feature 4
def update_expense():
    if not expenses:
        print("No expenses recorded yet.")
        return

    expense_id = input("Enter Expense ID to update: ").strip()
    if not expense_id:
        print("Expense ID cannot be empty.")
        return
    expense = find_expense(expense_id)

    if expense is None:
        print(f"No expense found with ID {expense_id.upper()}.")
        return

    print("\nCurrent record:")
    print_expense_table([expense])

    print("\nWhat do you want to change?")
    print("1. Date")
    print("2. Category")
    print("3. Description")
    print("4. Amount")
    print("5. Cancel")

    choice = input("Enter your choice (1-5): ").strip()
    if choice == "1":
        expense['date'] = read_date()
    elif choice == "2":
        expense['category'] = read_category()
    elif choice == "3":
        description = input("Enter new description: ").strip()
        if not description:
            print("Description cannot be empty.")
            return
        expense['description'] = description
    elif choice == "4":
        expense['amount'] = read_amount()
    elif choice == "5":
        print("Update cancelled.")
        return
    else:
        print("Invalid choice. Enter a number from 1 to 5.")
        return

    print("\nExpense updated.")
    print_expense_table([expense])


# Feature 5
def delete_expense():
    if not expenses:
        print("No expenses recorded yet.")
        return

    expense_id = input("Enter Expense ID to delete: ").strip()
    if not expense_id:
        print("Expense ID cannot be empty.")
        return
    expense = find_expense(expense_id)

    if expense is None:
        print(f"No expense found with ID {expense_id.upper()}.")
        return

    print_expense_table([expense])
    confirm = input("Delete this expense? (y/n): ").strip().lower()

    if confirm == "y":
        expenses.remove(expense)
        print("Expense deleted.")
    else:
        print("Deletion cancelled.")


# Feature 6
def calculate_total(expense_list):
    total = 0
    for expense in expense_list:
        total += expense['amount']
    return round(total, 2)


def calculate_average_daily(expense_list):
    if not expense_list:
        return 0

    days = set()
    for expense in expense_list:
        days.add(expense['date'])

    return calculate_total(expense_list) / len(days)


def find_highest(expense_list):
    if not expense_list:
        return None

    highest = expense_list[0]
    for expense in expense_list:
        if expense['amount'] > highest['amount']:
            highest = expense
    return highest


def find_lowest(expense_list):
    if not expense_list:
        return None

    lowest = expense_list[0]
    for expense in expense_list:
        if expense['amount'] < lowest['amount']:
            lowest = expense
    return lowest


def calculate_category_totals(expense_list):
    totals = {}
    for category in categories:
        totals[category] = 0

    for expense in expense_list:
        totals[expense['category']] += expense['amount']

    for category in totals:
        totals[category] = round(totals[category], 2)

    return totals


def show_statistics():
    if not expenses:
        print("No expenses recorded yet.")
        return

    highest = find_highest(expenses)
    lowest = find_lowest(expenses)
    totals = calculate_category_totals(expenses)

    print("\nExpense Statistics")
    print(f"Total expenses: ৳{calculate_total(expenses):.2f}")
    print(f"Average daily: ৳{calculate_average_daily(expenses):.2f}")
    print(f"Highest expense: ৳{highest['amount']:.2f} "
          f"({highest['description']}, {highest['category']}, "
          f"{highest['date']})")
    print(f"Lowest expense: ৳{lowest['amount']:.2f} "
          f"({lowest['description']}, {lowest['category']}, "
          f"{lowest['date']})")

    print("\nSpending by category:")
    for category, amount in totals.items():
        print(f"  {category:<14} ৳{amount:>10.2f}")


# Feature 7
def read_month():
    while True:
        text = input("Enter month (YYYY-MM): ").strip()
        try:
            parsed = datetime.strptime(text, "%Y-%m")
            return parsed.year, parsed.month
        except ValueError:
            print("Invalid month. Use YYYY-MM, e.g. 2026-11.")


def get_expenses_for_month(year, month):
    month_expense = []
    for expense in expenses:
        if expense['date'].year == year and expense['date'].month == month:
            month_expense.append(expense)
    return month_expense


def show_monthly_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    year, month = read_month()
    month_expenses = get_expenses_for_month(year, month)
    label = f"{year}-{month:02d}"

    if not month_expenses:
        print(f"No expenses recorded for {label}.")
        return

    highest = find_highest(month_expenses)
    totals = calculate_category_totals(month_expenses)

    print(f"\nMonthly Summary: {label}")
    print(f"Total expenses: ৳{calculate_total(month_expenses):.2f}")
    print(f"Transactions: {len(month_expenses)}")
    print(f"Average daily: ৳{calculate_average_daily(month_expenses):.2f}")
    print(f"Highest expense: ৳{highest['amount']:.2f} "
          f"({highest['description']}, {highest['category']}, "
          f"{highest['date']})")

    print("\nSpending by category:")
    for category, amount in totals.items():
        print(f"  {category:<14} ৳{amount:>10.2f}")


# Feature 8
def set_monthly_budget():
    year, month = read_month()
    amount = read_amount()

    budgets[(year, month)] = amount
    print(f"Budget for {year}-{month:02d} set to ৳{amount:.2f}.")


def show_budget_status():
    year, month = read_month()
    label = f"{year}-{month:02d}"

    if (year, month) not in budgets:
        print(f"No budget set for {label}.")
        return

    budget = budgets[(year, month)]
    spent = round(calculate_total(get_expenses_for_month(year, month)), 2)
    remaining = round(budget - spent, 2)

    print(f"\nBudget Status: {label}")
    print(f"Monthly budget: ৳{budget:.2f}")
    print(f"Current spending: ৳{spent:.2f}")
    print(f"Remaining: ৳{remaining:.2f}")

    if remaining < 0:
        print(f"WARNING: You have exceeded your budget by ৳{-remaining:.2f}!")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print("You are within your budget.")


# Menu
def show_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add expense")
    print("2. Display all expenses")
    print("3. Search / filter expenses")
    print("4. Update expense")
    print("5. Delete expense")
    print("6. Expense statistics")
    print("7. Monthly summary")
    print("8. Set monthly budget")
    print("9. Check budget status")
    print("10. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_all_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            show_monthly_summary()
        elif choice == "8":
            set_monthly_budget()
        elif choice == "9":
            show_budget_status()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 10.")


main()
