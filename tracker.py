from tracker_logic import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    tracker.load()

    print("Welcome to Modular Expense Tracker!")

    while True:
        command = input("\nWhat would you like to do? (add/view/summary/exit): ").strip().lower()

        if command == "add":
            tracker.add_expenses()
        elif command == "view":
            tracker.view_expense()
        elif command == "summary":
            tracker.show_summary()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please choose add, view, summary, or exit.")

if __name__ == "__main__":
    main()
