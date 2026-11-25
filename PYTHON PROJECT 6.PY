
import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    # 1. Add a new journal entry
    def add_entry(self):
        try:
            # Create file if it does not exist
            try:
                with open(self.filename, "x", encoding="utf-8"):
                    pass
            except FileExistsError:
                pass

            entry = input("\nEnter your journal entry: ").strip()

            if not entry:
                print("Error: Journal entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Append mode
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")

        except OSError as e:
            print("Error:", e)

    # 2. View all journal entries
    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if not content.strip():
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("--------------------------------")
                print(content.rstrip())

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")

        except OSError as e:
            print("Error:", e)

    # 3. Search for a journal entry
    def search_entry(self):
        try:
            keyword = input(
                "\nEnter a keyword or date to search: "
            ).strip()

            if not keyword:
                print("Error: Please enter a keyword or date.")
                return

            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            entries = [
                entry.strip()
                for entry in content.strip().split("\n\n")
                if entry.strip()
            ]

            matches = []

            for entry in entries:
                if keyword.casefold() in entry.casefold():
                    matches.append(entry)

            if matches:
                print("\nMatching Entries:")
                print("--------------------------------")

                for entry in matches:
                    print(entry)
                    print()

            else:
                print(
                    f"No entries were found for the keyword: {keyword}."
                )

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied. Cannot search the file.")

        except OSError as e:
            print("Error:", e)

    # 4. Delete all journal entries
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")

            elif confirmation == "no":
                print("\nDeletion cancelled.")

            else:
                print("\nInvalid confirmation. Please enter yes or no.")

        except PermissionError:
            print("Error: Permission denied. Cannot delete the file.")

        except OSError as e:
            print("Error:", e)

    # 5. Demonstrate write mode
    def overwrite_entries(self, text):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(text + "\n")

            print("Journal file overwritten successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")

        except OSError as e:
            print("Error:", e)

    # Main menu
    def menu(self):

        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option:\n")

            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print(
                    "\nThank you for using Personal Journal Manager. Goodbye!"
                )
                break

            else:
                print(
                    "\nInvalid option. Please select a valid option from the menu."
                )


# Main program execution
if __name__ == "__main__":

    journal = JournalManager()

    journal.menu()
