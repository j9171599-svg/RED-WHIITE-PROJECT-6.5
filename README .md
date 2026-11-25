# File Operator – Personal Journal Manager

**Author:** Jaineel Shingala  
**Language:** Python 3  
**Project type:** Menu-driven file-handling application using Object-Oriented Programming (OOP)

## 1. Project Overview

The **Personal Journal Manager** is a menu-driven Python application that allows a user to maintain a personal journal in a text file. It uses a `JournalManager` class to organize the journal operations and stores entries in `journal.txt`.

Each journal entry is saved with a date and time. The user can add entries, view all saved entries, search by a keyword or date, and delete all entries after confirmation.

## 2. Features

1. **Add a New Entry** – accepts a journal entry, adds a timestamp, and appends it to `journal.txt`.
2. **View All Entries** – reads and displays all saved journal entries.
3. **Search for an Entry** – searches journal entries using a keyword or date. The search is case-insensitive.
4. **Delete All Entries** – asks for confirmation before deleting the journal file.
5. **Exit** – closes the application with a goodbye message.

## 3. OOP Structure

The program defines a `JournalManager` class.

- `__init__()` initializes the journal filename as `journal.txt`.
- `add_entry()` creates the file when needed and appends a timestamped entry.
- `view_entries()` reads and displays the journal contents.
- `search_entry()` finds entries containing the entered keyword or date.
- `delete_entries()` asks for confirmation and removes the journal file when the user confirms.
- `overwrite_entries()` demonstrates write mode.
- `menu()` displays the main menu and calls the selected operation.

The main program creates a `JournalManager` object and starts the menu.

## 4. File-Handling Modes Demonstrated

| Mode | Purpose in the project |
|---|---|
| `x` | Creates the journal file only if it does not already exist. |
| `a` | Appends a new journal entry without replacing earlier entries. |
| `r` | Reads the journal contents for viewing and searching. |
| `w` | Demonstrates overwriting the journal file in `overwrite_entries()`. |

The program uses UTF-8 encoding when opening the text file.

## 5. Exception Handling

The program handles common file and input errors, including:

- `FileNotFoundError` – shown when the journal file is not available for reading or searching.
- `FileExistsError` – handled when the file already exists during the create operation.
- `PermissionError` – shown when the program does not have the required file permission.
- `OSError` – handles other operating-system file errors.
- Empty journal entries and empty search terms are rejected.
- Invalid menu choices and invalid deletion confirmations are handled with messages.

## 6. Main Menu

When the program starts, it displays:

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

## 7. Requirements

- Python 3.x
- No third-party Python packages are required.
- A terminal or Command Prompt.

## 8. How to Run

1. Keep the Python file in your project folder.
2. Open Command Prompt or a terminal in that folder.
3. Run the following command:

   ```bash
   python "PYTHON PROJECT 6.PY"
   ```

4. Select an option from `1` to `5`.
5. Follow the prompts displayed by the program.

The file `journal.txt` is created in the program's working directory when the first journal entry is added.

## 9. Example Workflow

The screenshots of the program are arranged below in the same order as the demonstrated program workflow.

### Screenshot 1 – Add a New Entry and View All Entries

Choose option `1` to enter a journal entry. The program adds a timestamp and confirms that the entry was saved. Then choose option `2` to display the saved journal entries.

![Screenshot 1 – Add and view entries](screenshots/01-add-and-view-entries.png)

### Screenshot 2 – Search for an Entry and Begin Deletion

Choose option `3` and enter a keyword or date. The program displays matching entries. Then choose option `4` to start the delete operation and show the confirmation prompt.

![Screenshot 2 – Search and delete confirmation](screenshots/02-search-and-delete-confirmation.png)

### Screenshot 3 – Confirm Deletion and Exit

Enter `YES` (or `yes`) to confirm deletion. The program removes the journal file and displays the deletion message. Choose option `5` to exit.

![Screenshot 3 – Delete and exit](screenshots/03-delete-and-exit.png)

## 10. Supplementary Project Reference Screenshots

The following images document the project overview, requirements, and additional expected behavior supplied with the project.

### Reference 1 – Project Overview and Learning Objectives

![Project overview](screenshots/project_reference/01-project-overview.png)

### Reference 2 – Requirements and Menu Example

![Requirements and menu](screenshots/project_reference/02-requirements-and-menu.png)

### Reference 3 – Error Handling and Exit Reference

![Error handling and exit reference](screenshots/project_reference/03-error-handling-and-exit-reference.png)

## 11. Project Folder Structure

```text
personal_journal_manager/
│
├── PYTHON PROJECT 6.PY
├── README.md
└── screenshots/
    ├── 01-add-and-view-entries.png
    ├── 02-search-and-delete-confirmation.png
    ├── 03-delete-and-exit.png
    └── project_reference/
        ├── 01-project-overview.png
        ├── 02-requirements-and-menu.png
        └── 03-error-handling-and-exit-reference.png
```

## 12. Conclusion

The Personal Journal Manager demonstrates how Python OOP and file handling can be combined to create a simple text-based journal application. It covers creating, reading, appending, searching, and deleting file data, along with timestamps, input validation, and exception handling.

---

**Author: Jaineel Shingala**
