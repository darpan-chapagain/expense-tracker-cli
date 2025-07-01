def load_expenses(filename):
    data = []
    try:
        with open(filename, "r") as f:
            for line in f: 
                data.append(line.strip())
    except FileNotFoundError:
        print("Starting fresh...")

    return data

def save_expenses(filename, entry):
    with open(filename, "a") as f:
        f.write(entry + "\n")