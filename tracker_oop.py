class ExpenseTracker:
    def _init_(self, filename="expenses.txt"):
        self.expenses = []
        self.filename = filename

    def load_expenses(self):
        try: 
            with open (self.filename, "r") as file:
                for line in file: 
                    self.expenses.append(line.strip())
            if self.expenses:
                print("Previous Expenses:")
                for item in self.expenses:
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
        self.expenses.append(entry)

        with open(FILENAME, "a") as file:
            file.write(entry + "\n")

        print("Expense added!")

    def view_expense():
        if not self.expenses:
            print("No expenses recorded yet")
        else:
            print("Your expenses:")
            for item in self.expenses:
                print("*", item)

    def show_summary():
        totals = {}

        for entry in self.expenses:
            parts = entry.split("-")

            if len(parts) != 3:
                continue

            description = parts[0]
            raw_amount = parts[1]
            category = parts[2]

            amount = float(raw_amount.strip().replace("$", ""))

            if category not in totals:
                totals[category] = 0 

            totals[category] += amount

        overall = 0
        print("Expense Summary by category")
        for cat, total in totals.items():
            print(f"* {cat}: ${total: .2f}")
            overall += total
        def show_summary():
    totals = {}

    for entry in expenses:
        parts = entry.split("-")

        if len(parts) != 3:
            continue

        description = parts[0]
        raw_amount = parts[1]
        category = parts[2]

        amount = float(raw_amount.strip().replace("$", ""))

        if category not in totals:
            totals[category] = 0 

        totals[category] += amount

    overall = 0
    print("Expense Summary by category")
    for cat, total in totals.items():
        print(f"* {cat}: ${total: .2f}")
        overall += total
    print(f"\n💵 Total Spent: ${round(overall, 2)}")
