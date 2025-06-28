
expenses = []
FILENAME = "expenses.txt"

def add_expense():
    description = input("What did you spend on?").strip()
    amount = input("How much?").strip()
    category = input("What's the category?").strip().capitalize()
    
    if not amount.replace('.', '', 1).isdigit():
        print("Amount must be a number")
        return
    
    entry = f"{description} - ${amount} - {category}"
    expenses.append(entry)

    with open(FILENAME, "a") as file:
        file.write(entry + "\n")

    print("Expense added!")


def view_expense():
    if not expenses:
         print("No expenses recorded yet")
    else:
        print("Your expenses:")
        for item in expenses:
            print("*", item)

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
    print("Total Spent: $", round(overall, 2))

def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            for line in file: 
                expenses.append(line.strip())

            if expenses:
                print("Previous expenses:")
                for item in expenses:
                    print(".", item)
    except FileNotFoundError:
        print("No previous expeses found. Starting Fresh")        

def main_menu():
    load_expenses()
    print("Welcome to the Expense Tracker CLI")

    while True: 
        command = input("What would you like to do? (add/view/summary/exit):").strip().lower()

        if command == "add":
            add_expense()
            
        elif command == "view":
            view_expense()

        elif command == "summary":
            show_summary()
            
        elif command == "exit":
            print("Goodbye")
            break
        else:
            print("Invalid command. Please chosse add, view or exit")

main_menu()