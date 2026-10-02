# 📚 Library Management System

A simple console-based Library Management System built with Python.

## 🎯 Project Overview

This project is a CRUD-based library management system that allows users to manage book records through a menu-driven program.

The system allows users to:

- View all books
- Search for a book by Book ID 
- Add new book
- Borrow book
- Return book
- Delete book
- View library statistics
- Exit the program

## ✨ Features

### 📖 Read

- View all books in the library
- Search for a specific book using its Book ID
- Display book details including:
  - Book ID
  - Book Name
  - Author
  - Availability
- Handle Book IDs that don't exist

### ➕ Create

- Add a new book to the library
- Check for duplicate Book IDs
- Automatically set new books as `Available`
- Confirm before saving a new book
- Handle invalid save options

### 🔄 Update

- Borrow an available book
- Return a borrowed book
- Check whether the Book ID exists
- Display book information before updating
- Confirm before updating the book status
- Prevent borrowing an already borrowed book
- Prevent returning a book that is already available

### 🗑️ Delete

- Delete a book using its Book ID
- Display book information before deletion
- Confirm before deleting a book
- Handle Book IDs that do not exist

### 📊 Library Statistics

- Display total number of books
- Display number of available books
- Display number of borrowed books
- Calculate the library availability rate

## 🗂️ Data Structure

The library data is stored using a list of dictionaries.

Each book record contains:

- `Book ID` — Primary Key
- `Book Name`
- `Author`
- `Availability`

Example:

```python
{
    "Book ID": "B001",
    "Book Name": "Atomic Habits",
    "Author": "James Clear",
    "Availability": "Available"
}
