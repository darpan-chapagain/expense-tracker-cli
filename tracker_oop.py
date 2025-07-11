class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.__expenses = []
        self.__filename = filename

    def load_expenses(self):
        try: 
            with open (self.__filename, "r") as file:
                for line in file: 
                    self.__expenses.append(line.strip())
            if self.__expenses:
                print("Previous Expenses:")
                for item in self.__expenses:
                    print("*", item)
        except FileNotFoundError:
            print("File not found")

    def add_expenses(self):
        description = input("What did you spend on?").strip()
        amount = input("How much?").strip()
        category = input("What's the category?").strip().capitalize()
        
        if not amount.replace('.', '', 1).isdigit():
            print("Amount must be a number")
            return
        
        entry = f"{description} - ${amount} - {category}"
        self.__expenses.append(entry)

        with open(self.__filename, "a") as file:
            file.write(entry + "\n")

        print("Expense added!")

    def get_expense(self):
        return self.__expenses.copy()

    def view_expense(self):
        if not self.__expenses:
            print("No expenses recorded yet")
        else:
            print("Your expenses:")
            for item in self.__expenses:
                print("*", item)

    def show_summary(self):
        totals = {}

        for entry in self.__expenses:
            parts = entry.split("-")
            if len(parts) != 3:
                continue

            category = parts[2].strip()
            amount = float(parts[1].strip().replace("$", ""))

            if category not in totals:
                totals[category] = 0
            totals[category] += amount

        overall = 0
        print("\n📊 Expense Summary by Category:")
        for cat, total in totals.items():
            print(f"* {cat}: ${total:.2f}")
            overall += total

        print(f"\n💵 Total Spent: ${round(overall, 2)}")

    def run(self):
        self.load_expenses()
        print("Welcome to the OOP Expense Tracker CLI!")

        while True:
            command = input("\nWhat would you like to do? (add/view/summary/exit): ").strip().lower()

            if command == "add":
                self.add_expenses()
            elif command == "view":
                self.view_expense()
            elif command == "summary":
                self.show_summary()
            elif command == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid command. Please choose add, view, summary, or exit.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()

        


