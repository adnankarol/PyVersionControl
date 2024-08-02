# PyVersionControl: Pythonic Version Control System

**PyVersionControl** is a lightweight, Python-based version control system designed to track changes in your project files. It provides basic version control functionality by allowing you to commit changes, track new files, and view commit history. This system is ideal for projects where a full-featured version control system might be too complex.

## Features

- **Version Control System Creation:** Initialize a version control system in a specified directory.
- **Change Tracking:** Track changes in files within the directory and record commit messages.
- **New File Detection:** Detect and commit new files added to the directory.
- **Commit Message Retrieval:** View all commit messages in the version history.

## Usage

### Initialize the Repository
Set up the version control system in a test folder:

```sh
python bit.py --path C:\Users\adnan\Desktop\Test_Folder
```

### Commit Changes
Commit changes with a custom message:

```sh
python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command commit-"Initial commit"
```

### List All Versions
List all versions of the files:

```sh
python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command list_versions
```

## Example Commands

- **Initialize the repository:**

    ```sh
    python bit.py --path C:\Users\adnan\Desktop\Test_Folder
    ```

- **List all versions:**

    ```sh
    python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command list_versions
    ```

- **Commit changes:**

    ```sh
    python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command commit-"Added new feature"
    ```

## Additional Functionalities

Based on the main logic of PyVersionControl, additional functionalities can be implemented:

1. **Rollback to Previous Version:**
    Restore the project to a previous version by copying files from the selected version directory back to the main project directory.

2. **Track Specific File Changes:**
    Implement a feature to track changes in specific files rather than the entire directory.

3. **Enhanced Commit Messages:**
    Allow for more detailed commit messages, possibly including metadata such as the date and time of the commit, the user who made the commit, and a summary of changes.

4. **Conflict Detection:**
    Implement conflict detection to alert users when two different changes conflict with each other, potentially merging those changes or alerting the user to resolve conflicts manually.

5. **Automated Backups:**
    Schedule automated backups at regular intervals to ensure that all changes are consistently tracked.

6. **Graphical User Interface (GUI):**
    Develop a simple GUI to make the version control system more user-friendly.

## Contact

For any inquiries or support, please contact me on LinkedIn: [Adnan Karol](https://www.linkedin.com/in/adnan-karol-aa1666179/)
