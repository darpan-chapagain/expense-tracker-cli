from file_utils import load_expenses, save_expenses

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.__expenses = []
        self.__filename = filename

    def load(self):
        self.__expenses = load_expenses(self.__filename)

    def add_expenses(self):
        description = input("What did you spend on?").strip()
        amount = input("How much?").strip()
        category = input("What's the category?").strip().capitalize()
        
        if not amount.replace('.', '', 1).isdigit():
            print("Amount must be a number")
            return
        
        entry = f"{description} - ${amount} - {category}"
        self.__expenses.append(entry)

        save_expenses(self.__filename, entry)

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
        


