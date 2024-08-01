# Pythonic Version Control System

**Pythonic Version Control System** is a lightweight, Python-based version control system designed to track changes in your project files. It provides basic version control functionality by allowing you to commit changes, track new files, and view commit history. This system is ideal for projects where a full-featured version control system might be too complex.

## Introduction

This tool implements a simple version control system in Python, allowing users to:

- Create and manage versions of their project.
- Track changes to files and directories.
- Commit changes with custom messages.
- List all available versions and their commit messages.

It's designed to be easy to use and understand, making it a great choice for small to medium-sized projects.

## To Run

1. **Initialize the Repository**  
   Run the command to set up the version control system in a test folder:

    ```sh
    python bit.py --path C:\Users\adnan\Desktop\Test_Folder
    ```

2. **Commit Changed Files**  
   Run the command to commit changes with a custom message:

    ```sh
    python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command commit-"Initial commit"
    ```

3. **List All Versions**  
   Run the command to list all versions of the files:

    ```sh
    python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command list_versions
    ```

## Example Command

To initialize the repository:

```sh
python bit.py --path C:\Users\adnan\Desktop\Test_Folder
```

To list all versions:

```sh
python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command list_versions
```

To commit changes:

```sh
python bit.py --path C:\Users\adnan\Desktop\Test_Folder --command commit-"Added new feature"
```

## Current Features

1. **Version Control System Creation**  
   Creates a version control system in the specified directory (`C:\Users\adnan\Desktop\Test_Folder`).

2. **Change Tracking**  
   Tracks changes in files within the directory and records commit messages.

3. **New File Detection**  
   Detects and commits new files added to the directory.

4. **Commit Message Retrieval**  
   Allows users to view all commit messages in the version history.

## Additional Information

In case of any errors, feel free to contact me on LinkedIn: [Adnan](https://www.linkedin.com/in/adnan-karol-aa1666179/)
