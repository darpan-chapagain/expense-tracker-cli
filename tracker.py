
expenses = []
FILENAME = "expenses.txt"

def add_expense():
    description = input("What did you spend on?").strip()
    amount = input("How much?").strip()
    
    if not amount.replace('.', '', 1).isdigit():
        print("Amount must be a number")
        return
    
    entry = f"{description} - ${amount}"
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
        command = input("What would you like to do? (add/view/exit):").strip().lower()

        if command == "add":
            add_expense()
            
        elif command == "view":
            view_expense()
            
        elif command == "exit":
            print("Goodbye")
            break
        else:
            print("Invalid command. Please chosse add, view or exit")

main_menu()