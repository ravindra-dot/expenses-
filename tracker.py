from datetime import date
from expense import Expense

# Main function to run the expense tracker
def main():
    print("Expense Tracker is running...\n")

    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            expense = get_user_expense()
            save_user_expense(expense)

        elif choice == "2":
            summarize_expenses()

        elif choice == "3":
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid choice. Try again.")


#user input to get expense details from user        
def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = {
        1: "Food",
        2: "Transport",
        3: "Utilities",
        4: "Entertainment",
        5: "Other"
    }

    print("\nSelect a category:")
    for key, value in expense_categories.items():
        print(f"{key}. {value}")

    while True:
        choice = int(input("Enter category number: "))
        if choice in expense_categories:
            category = expense_categories[choice]
            break
        print("Invalid choice. Try again.")

    return Expense(expense_name, category, expense_amount)

#function to save expense details to a file
def save_user_expense(expense: Expense):
    with open("expenses.csv", "a") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount},{date.today()}\n")

#function to summarize and display expenses
def summarize_expenses():
    total = 0
    category_summary = {}

    try:
        with open("expenses.csv", "r") as file:
            for line in file:
                _, category, amount, _ = line.strip().split(",")
                amount = float(amount)
                total += amount

                category_summary[category] = category_summary.get(category, 0) + amount

        print("\nExpense Summary:")
        for category, amount in category_summary.items():
            print(f"{category}: ₹{amount}")

        print(f"\n Total Expense: ₹{total}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


if __name__ == "__main__":
    main()