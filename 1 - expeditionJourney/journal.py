import journal

def add_entry(path, place, gold):
    with open(path, "a") as f: # Opens the file "journal.txt" to append to it, creating it if it doesn't exist
        f.write(f"{place},{gold}\n")

def read_entries(path): # Reads the journal entries from the file at the given path and returns a list of tuples containing the place and gold amount for each entry. If the file does not exist, it returns an empty list.
    try:
        with open(path, "r") as f:
            entries = []
            for line in f:
                place, gold = line.strip().split(",")
                entries.append((place, int(gold))) 
            return entries
    except FileNotFoundError:
        return []

def total_gold(path): # Calculates the total amount of gold from all journal entries in the file at the given path. It uses the read_entries function to get the list of entries and then sums up the gold amounts. If the file does not exist, it returns 0.
    return sum(gold for _, gold in read_entries(path))

def main(path="journal.txt"): # This function provides a simple command-line interface for the user to interact with the journal. It allows the user to add entries, view existing entries, and see the total amount of gold collected. The user can choose to add an entry by providing a place name and gold amount, view all entries along with the total gold, or quit the program.
    while True:
        print("1) Add entry")
        print("2) View entries")
        print("3) Quit")
        choice = input("Choice: ")

        if choice == "1": # This handles when the user adds a new entry.
            place = input("Place: ") # First, it prompts the user for the place name.
            gold_input = input("Gold: ") # Then, it prompts for the amount of gold.
            try:
                gold = int(gold_input) # It attempts to convert the gold input into an integer.
            except ValueError:
                print("Invalid gold amount. Please enter a number.") # If the conversion fails (e.g., if the user enters a non-numeric value), it catches the ValueError and informs the user that the input was invalid.
            else:
                if gold < 0: # If the gold amount is negative, it informs the user that gold cannot be negative.
                    print("Gold cannot be negative.")
                else: # Otherwise, it calls the add_entry function to add the new entry to the journal and confirms that the entry was added.
                    journal.add_entry(path, place, gold)
                    print(f"Entry added: {place}, {gold}")
            finally:
                print("--")

        elif choice == "2": # This handles when the user wants to view the existing entries in the journal.
            entries = journal.read_entries(path)
            if not entries:
                print("The journal is empty.")
            else:
                for i, (place, gold) in enumerate(entries, start=1):
                    print(f"{i}. {place}, {gold}")
                total = journal.total_gold(path)
                print(f"Total gold: {total}")

        elif choice == "3": # This handles when the user chooses to quit the program. It prints a message indicating that the journal is closed and breaks out of the loop, ending the program.
            print("Journal closed.")
            break

        else:
            print("Choose 1, 2 or 3.")

if __name__ == "__main__":
    main(path="journal.txt")