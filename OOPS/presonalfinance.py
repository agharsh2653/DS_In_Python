class PersonalFinanceManager:
    def __init__(self):
        self.balance = 0.0
        self.income_records = []
        self.expense_records = []

    def add_income(self, amount, description):
        if amount <= 0:
            print("Income amount must be positive.")
            return
        self.balance += amount
        self.income_records.append((amount, description))
        print(f"Income added: ₹{amount} - {description}")

    def add_expense(self, amount, description):
        if amount <= 0:
            print("Expense amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance to add this expense.")
            return
        self.balance -= amount
        self.expense_records.append((amount, description))
        print(f"Expense added: ₹{amount} - {description}")

    def view_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")

    def view_income_records(self):
        if not self.income_records:
            print("No income records found.")
            return
        print("Income Records:")
        for amount, description in self.income_records:
            print(f"₹{amount} - {description}")

    def view_expense_records(self):
        if not self.expense_records:
            print("No expense records found.")
            return
        print("Expense Records:")
        for amount, description in self.expense_records:
            print(f"₹{amount} - {description}")

    def max_expense(self):
        if not self.expense_records:
            print("No expense records found.")
            return
        max_expense = max(self.expense_records, key=lambda x: x[0])
        print(f"Maximum Expense: ₹{max_expense[0]} - {max_expense[1]}")

    def min_expense(self):
        if not self.expense_records:
            print("No expense records found.")
            return
        min_expense = min(self.expense_records, key=lambda x: x[0])
        print(f"Minimum Expense: ₹{min_expense[0]} - {min_expense[1]}")

    def menu(self):
        print("\nPersonal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Income Records")
        print("5. View Expense Records")
        print("6. View Maximum Expense")
        print("7. View Minimum Expense")
        print("8. Exit")

def main():
    manager = PersonalFinanceManager()
    
    while True:
        manager.menu()
        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Exiting...")
            break

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            manager.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            manager.add_expense(amount, description)
        elif choice == '3':
            manager.view_balance()
        elif choice == '4':
            manager.view_income_records()
        elif choice == '5':
            manager.view_expense_records()
        elif choice == '6':
            manager.max_expense()
        elif choice == '7':
            manager.min_expense()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
