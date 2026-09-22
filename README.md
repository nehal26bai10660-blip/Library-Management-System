# Library Management System

A simple Python-based command-line application for managing books in a library.

## Overview

The Library Management System is a Python project designed to make basic library operations easier to manage.

Users can add, remove, search, borrow, and return books. The system also allows users to view all books and check which books are currently available.

The project demonstrates important Python Essentials concepts such as:

❁ Object-Oriented Programming

❁ Functions

❁ Modules and Packages

❁ Lists

❁ Loops

❁ Conditional Statements

❁ Exception Handling

❁ Testing with Pytest

## Features

❁ Add Book - Add a new book with its title and author.

❁ Remove Book - Remove a book from the library.


❁ Search Book - Search for a specific book.

❁ Display All Books - View all books in the library.

❁ Display Available Books - View books that are currently 
available.

❁ Borrow Book - Borrow an available book.

❁ Return Book - Return a borrowed book.

❁ Duplicate Prevention - Prevent adding the same book twice.

❁ Input Validation - Prevent empty book titles and author names.

❁ Exception Handling - Handle invalid menu input.

## Project Structure

```text
Library-Management-System/
|
├── library/
│   ├── __init__.py
│   ├── __main__.py
│   ├── book.py
│   ├── library.py
│   └── validators.py
|
├── tests/
│   └── test_library.py
|
├── .gitignore
├── dev-requirements.txt
├── pyproject.toml
├── README.md
└── statement.md
``` 

## Modules

### book.py

Contains the `Book` class.

It handles operations related to individual books, including:

❁ Displaying book information

❁ Borrowing a book

❁ Returning a book

### library.py

Contains the `Library` class.

It manages the collection of books and provides functions for:

❁ Adding books

❁ Removing books

❁ Searching books

❁ Displaying books

❁ Borrowing books

❁ Returning books

### validators.py

Contains validation functions used to check:

❁ Book titles

❁ Author names

### __ main__.py

Contains the main program and menu.

It handles user interaction and controls the flow of the application.

### __ init__.py

Defines the `library` Python package.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Object-Oriented Programming | Classes and objects |
| Modules | Organizing the program |
| Lists | Storing books |
| Loops | Repeating operations |
| Conditional Statements | Decision making |
| Exception Handling | Handling invalid input |
| Pytest | Automated testing |

