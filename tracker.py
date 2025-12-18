def main():
    print("Expense Tracker is running...")
    #getting user inputs
    get_user_expense()

    #write there expense to a file
    save_user_expense()

    #reading expenses from a- file
    summerize_expenses()

def get_user_expense():
    print("Getting user expense...")
    expence_name = input("Enter expense name: ")
    expence_amount = float(input("Enter expense amount: "))
    expence_categories = {
        1: "Food",
        2: "Transport",
        3: "Utilities",
        4: "Entertainment",
        5: "Other"
    } 

    print(f"Expense name is: {expence_name}, {expence_amount},{expence_categories}")

    while True:
        print("Select a category:")
        for i in expence_categories:
            print(f"{i}. {expence_categories[i]}")
        break
   

def save_user_expense():
    print("Saving user expense...")


def summerize_expenses():
    print("Summarizing expenses...")
   


if __name__ == "__main__":
    main()