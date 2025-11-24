class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add(self):
        entry = input("Enter journal entry: ")
        try:
            with open(self.filename, "a") as file:
                file.write("\\n" + entry)
            print("Entry added successfully")
        except Exception as e:
            print("Failed to add entry:", e)

    def view(self):
        try:
            with open(self.filename, "r") as file:
                print("Your journal entries are:")
                print("------------------------------")
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print("Error: The journal file does not exist, please add a new entry first.")
        except Exception as e:
            print("Error reading file:", e)

    def delete(self):
        confirm = input("Are you sure you want to delete all entries (yes/no): ")
        if confirm.lower() == "yes":
            try:
                with open(self.filename, "w") as file:
                    pass
                print("All entries deleted")
            except Exception as e:
                print("No journal entries to delete:", e)
        else:
            print("Not deleted")

    def search(self):
        keyword = input("Enter a keyword from journal entry to view that specific entry: ")
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
            for line in lines:
                if keyword in line:
                    print(line.strip())
                    break
            else:
                print("No matching entries found")
        except FileNotFoundError:
            print("Error: The journal file does not exist, please add a new entry first.")
        except Exception as e:
            print("Error reading file:", e)

def run_journal_manager_menu():
    jm = JournalManager()
    while True:
        print("""
Personal Journal Manager!
Please select an option:
1. Add a new entry
2. View all entries
3. Search for an entry
4. Delete all entries
5. Exit
""")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer choice.")
            continue

        if choice == 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        elif choice == 1:
            jm.add()
        elif choice == 2:
            jm.view()
        elif choice == 3:
            jm.search()
        elif choice == 4:
            jm.delete()
        else:
            print("====Enter Valid Choice====")
