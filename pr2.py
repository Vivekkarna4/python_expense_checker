# Function to display the menu options to the user
def display_menu():
    print("Expense Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

# Function to add income to the income_list
def add_income(income_list):
    amount = float(input("Enter income amount: "))  # Prompt user to enter income amount and convert it to float
    income_list.append(amount)  # Add the income amount to the list
    print("Income added.")  # Confirm that income has been added

# Function to add an expense to the expense_list
def add_expense(expense_list):
    amount = float(input("Enter expense amount: "))  # Prompt user to enter expense amount and convert it to float
    category = input("Enter expense category (e.g., food, transportation): ")  # Prompt user to enter expense category
    expense_list.append((amount, category))  # Add the expense amount and category as a tuple to the list
    print("Expense added.")  # Confirm that expense has been added

# Function to view a summary of income, expenses, and balance
def view_summary(income_list, expense_list):
    total_income = sum(income_list)  # Calculate total income by summing all values in the income list
    total_expenses = sum(amount for amount, category in expense_list)  # Calculate total expenses by summing all amounts in the expense list
    balance = total_income - total_expenses  # Calculate balance by subtracting total expenses from total income

    # Print the summary
    print("\nSummary")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance}\n")

# Main function to run the program
def main():
    income_list = []  # Initialize an empty list to store income
    expense_list = []  # Initialize an empty list to store expenses

    # Start an infinite loop to keep the program running until the user chooses to exit
    while True:
        display_menu()  # Display the menu options to the user
        choice = input("Choose an option: ")  # Prompt user to choose an option

        if choice == '1':
            add_income(income_list)  # Call add_income function if user chooses option 1
        elif choice == '2':
            add_expense(expense_list)  # Call add_expense function if user chooses option 2
        elif choice == '3':
            view_summary(income_list, expense_list)  # Call view_summary function if user chooses option 3
        elif choice == '4':
            print("Exiting the program.")  # Print exit message if user chooses option 4
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")  # Print error message for invalid choice

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to run the program
