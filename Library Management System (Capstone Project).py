# DATA INITIALIZATION
# List of menu options in this Library Management System
menu = ['1. View All Books',
        '2. Add New Book',
        '3. Borrow / Return Book',
        '4. Delete Book', 
        '5. Library Statistics',
        '6. Exit']

# Books Data: Book ID (primary key), Book Name, Author, Availability
# books = list of dictionaries, where each dictionary represents one book record 
books = [
    {
        "Book ID": "B001",
        "Book Name": "Atomic Habits",
        "Author": "James Clear",
        "Availability": "Available",
    },
    {
        "Book ID": "B002",
        "Book Name": "The Psychology of Money",
        "Author": "Morgan Housel",
        "Availability": "Available",
    },
    {
        "Book ID": "B003",
        "Book Name": "The Housemaid's Secret",
        "Author": "Freida McFadden",
        "Availability": "Borrowed",
    },
    {
        "Book ID": "B004",
        "Book Name": "Funny Story",
        "Author": "Emily Henry",
        "Availability": "Available",
    },
    {
        "Book ID": "B005",
        "Book Name": "The Midnight Library",
        "Author": "Matt Haig",
        "Availability": "Available",
    },
    {
        "Book ID": "B006",
        "Book Name": "The Seven Husbands of Evelyn Hugo",
        "Author": "Taylor Jenkins Reid",
        "Availability": "Borrowed",
    },
    {
        "Book ID": "B007",
        "Book Name": "Days at the Morisaki Bookshop",
        "Author": "Satoshi Yagisawa",
        "Availability": "Available",
    },
    {
        "Book ID": "B008",
        "Book Name": "Secrets of Divine Love",
        "Author": "A. Helwa",
        "Availability": "Available",
    },
    {
        "Book ID": "B009",
        "Book Name": "Loved One",
        "Author": "Aisha Muharrar",
        "Availability": "Borrowed",
    },
    {
        "Book ID": "B010",
        "Book Name": "The Love Hypothesis",
        "Author": "Ali Hazelwood",
        "Availability": "Available",
    },
    {
        "Book ID": "B011",
        "Book Name": "Project Hail Mary",
        "Author": "Andy Weir",
        "Availability": "Available",
    },
]

# READ FUNCTION --> view and search books
def viewbooks(): 
    # Keeps the viewbooks menu running until the user choose Back to Main Menu
    while True: 
        option_viewbooks = input('''
        1. View All Books
        2. Search Book by Book ID
        3. Back to Main Menu

        Choose your option: ''')
        # OPTION 1: VIEW ALL BOOKS --> display all books records that stored in the library
        if option_viewbooks == '1':
            # Cheks whether the library currently has any books
            if books == []:
                print("\nNo books available.")
            else:
                # Displays the table header for all books records
                print("\n========================================== ALL BOOKS ==========================================")
                print(f"{'Book ID':<10} {'Book Name':<40} {'Author':<30} {'Availability':<15}")
                print("-" * 95)

                # Loops through every book in the booklist & display each book as one row in a table
                for book in books:
                    print(f"{book['Book ID']:<10} "
                        f"{book['Book Name']:<40} "
                        f"{book['Author']:<30} "
                        f"{book['Availability']:<15}")
                print("-" * 95)

        # OPTION 2: SEARCH BOOK BY BOOK ID --> allows users to find specific book using the primary key
        elif option_viewbooks == '2':
            # Gets the Book ID entered by user. 
            # Using .upper which allows inputs to become uppercase
            bookID = input("Input Book ID: ").upper()

            # Initially assumes that the requested book doesnt exist
            found = False

            # Searches through each book record
            for book in books:
                # Checks whether the Book ID matches the user's input & display the matching book information
                if book['Book ID'] == bookID:
                    print(f'''
                    ==================== BOOK FOUND ====================
                    Book ID     : {book["Book ID"]}
                    Book Name   : {book["Book Name"]}
                    Author      : {book["Author"]}
                    Availability: {book["Availability"]}
                    =====================================================
                    ''')

                    # Change the status because the book has been found
                    found = True
                    # Stops the search because matching Book ID has already been found
                    break

                # If no matching Book ID exists, notify the user
            if found == False:
                print("\nBook ID not found")

        # OPTION 3: BACK TO MAIN MENU --> exit sub menu and return to main menu
        elif option_viewbooks == '3':
            break
        # Invalid option
        else:
            print("\nInvalid option. Choose 1-3.")

# CREATE FUNCTION -->  add new book
# Allows the user to add new book record to the system
def addbook():
    # keeps the Add Book submenu running until user choose back to main menu
    while True:
        option_addbook = input('''
        1. Add New Book
        2. Back to Main Menu

        Choose your option: ''')

        # OPTION 1: ADD NEW BOOK -
        if option_addbook == '1':
            book_id = input("Input Book ID: ").upper()

            # Checking duplicate book ID
            duplicate = False

            for book in books:
                # Cheks whether the entered book ID already exists 
                if book['Book ID'] == book_id:
                    duplicate = True
                    # Stops searching once a duplicate is found
                    break

            if duplicate: 
                print("\nBook ID already exists. Please input another Book ID.")

            # If the Book ID unique, continue creating the new book record
            else: 
                book_name = input("Input Book Name: ")
                author = input("Input Author's Name: ")

                # Creates new book as a dictionary, and automatically have 'Available' status
                newbook = {
                    "Book ID": book_id,
                    "Book Name": book_name,
                    "Author": author,
                    "Availability": "Available"
                }

                # Asks user to confirm before saving the new book
                save = input("Save this book? (YES/NO): ").upper()
                if save == 'YES':
                    # Adds the new dictionary to books list
                    # Append represent the CREATE function 
                    books.append(newbook)
                    print(f"""
                        Book successfully added!.
                        =====================================================
                        Book ID     : {newbook['Book ID']}
                        Book Name   : {newbook['Book Name']}
                        Author      : {newbook['Author']}
                        Availability: {newbook['Availability']}
                        =====================================================""")
                elif save == 'NO':
                    print("\nBook was not saved.")
                else: 
                    print("\nInvalid option. Book was not saved.")    
        
        # OPTION 2: BACK TO MAIN MENU
        elif option_addbook == '2':
            break

        # INVALID OPTION
        else: 
            print("\nInvalid option. Choose 1 or 2.")

# UPDATE FUNCTION --> borrow / return book
def updatebook():
    # Keeps the submenu running until user choose back to main menu
    while True:
        option_updatebook = input('''
        1. Borrow Book
        2. Return Book
        3. Back to Main Menu

        Choose your option: ''')

        # OPTION 1: BORROW BOOK
        if option_updatebook == '1':
            book_id = input("Input Book ID: ").upper()

            # Initially assume the book has not been found 
            found = False 

            # Search the requested book
            for book in books:
                
                if book['Book ID'] == book_id:
                    found = True
                    # Display the existing book data 
                    print(f'''
                    ==================== BOOK FOUND ====================
                    Book ID     : {book["Book ID"]}
                    Book Name   : {book["Book Name"]}
                    Author      : {book["Author"]}
                    Availability: {book["Availability"]}
                    =====================================================
                    ''')

                    # Check whether the book is available to borrow
                    if book['Availability'] == 'Available':
                        # Ask user whether they want to continue to update book status
                        continue_update = input("Continue to borrow this book? (YES/NO): ").upper()
                        if continue_update == 'YES':
                            # Ask user to confirm the update
                            confirm_update = input("Confirm borrow? (YES/NO): ").upper()

                            if confirm_update == 'YES':
                                # Updates book record
                                book['Availability'] = 'Borrowed'
                                print(f"""
                                Book successfully borrowed!.
                                =====================================================
                                Book ID     : {book['Book ID']}
                                Book Name   : {book['Book Name']}
                                Author      : {book['Author']}
                                Availability: {book['Availability']}
                                =====================================================""")

                            elif confirm_update == "NO":
                                print("\nBook was not borrowed.")
                            else:
                                print("\nInvalid option. Book was not borrowed.")

                        elif continue_update == "NO":
                            print("\nUpdate book cancelled.")
                        else:
                            print("\nInvalid option. Update book cancelled.")

                    else:
                        print("\nBook is already borrowed")
                    
                    break       
            
            if found == False:
                print("\nBook ID not found.")

        # OPTION 2: RETURN BOOK
        elif option_updatebook == '2':
            book_id = input("Input Book ID: ").upper()

            # Initially assume the book has not been found
            found = False 

            # Search the requested book
            for book in books:
                if book['Book ID'] == book_id:
                    found = True
                    # Display the existing book data 
                    print(f'''
                    ==================== BOOK FOUND ====================
                    Book ID     : {book["Book ID"]}
                    Book Name   : {book["Book Name"]}
                    Author      : {book["Author"]}
                    Availability: {book["Availability"]}
                    =====================================================
                    ''')

                    # Check whether the book is currently borrowed
                    if book['Availability'] == 'Borrowed':
                        # Ask user whether they want to continue to update book status
                        continue_update = input("Continue to return this book? (YES/NO): ").upper()
                        if continue_update == 'YES':
                            # Ask user to confirm the update
                            confirm_update = input("Confirm return? (YES/NO): ").upper()

                            if confirm_update == 'YES':
                                # Updates the status back to 'Available'
                                book['Availability'] = 'Available'
                                print(f"""
                                Book successfully returned!
                                =====================================================
                                Book ID     : {book['Book ID']}
                                Book Name   : {book['Book Name']}
                                Author      : {book['Author']}
                                Availability: {book['Availability']}
                                =====================================================""")

                            elif confirm_update == "NO":
                                print("\nBook was not returned.")
                            else:
                                print("\nInvalid option. Book was not returned.")

                        elif continue_update == "NO":
                            print("\nUpdate book cancelled.")
                        else:
                            print("\nInvalid option. Update book cancelled.")

                    else:
                        print("\nBook is already available.")
                    
                    break 

            # If no matching Book ID exists        
            if found == False:
                print("\nBook ID not found.")

        # OPTION 3: BACK TO MAIN MENU
        elif option_updatebook == '3':
            break

        else: 
            print("\nInvalid option. Choose 1-3.")

# DELETE FUNCTION --> delete book
# Allows the user to remove a book record
def deletebook():
    while True:
        option_deletebook = input('''
        1. Delete Book
        2. Back to Main Menu
        
        Choose your option: ''')

        # OPTION 1: DELETE BOOK
        if option_deletebook == '1':
            book_id = input("Input Book ID: ").upper()
            found = False

            # Search the requested book
            for book in books: 
                if book['Book ID'] == book_id:
                    found = True

                    # Display the existing book data 
                    print(f'''
                    ==================== BOOK FOUND ====================
                    Book ID     : {book["Book ID"]}
                    Book Name   : {book["Book Name"]}
                    Author      : {book["Author"]}
                    Availability: {book["Availability"]}
                    =====================================================
                    ''')

                    # Ask user to confirm before deleting
                    confirm_delete = input("Delete this book? (YES/NO): ").upper()

                    if confirm_delete == 'YES':
                        # Removes the matching book record from the list
                        # Remove represents the DELETE function by using .remove
                        books.remove(book)
                        print(f"""
                        Book successfully deleted.
                        =====================================================
                        Book ID     : {book['Book ID']}
                        Book Name   : {book['Book Name']}
                        Author      : {book['Author']}
                        =====================================================""")

                    elif confirm_delete == 'NO':
                        print("\nBook was not deleted.")
                    else: 
                        print("\nInvalid option. Book was not deleted.")
                    break    


            # If no matching Book ID            
            if found == False:
                print("Book ID not found.")

        # OPTION 2: BACK TO MAIN MENU
        elif option_deletebook == '2':
            break 
        # INVALID OPTION
        else:
            print("\nInvalid option. Choose 1 or 2.")


# STATISTICS FUNCTION --> library statistics
# Provides overview of the current library data, by calculates the total number of books, available books, borrowed books, and the availability rate
def statistics():
    while True:
        option_statistics = input('''
        1. View Library Statistics
        2. Back to Main Menu
        
        Choose your option: ''')

        # OPTION 1: VIEW LIBRARY STATISTICS
        if option_statistics == '1':
            # Counts the total number of book records in the library, by using len/length
            total_books = len(books)
            # Variables used to count books based on their availability
            available_books = 0
            borrowed_books = 0

            # Loops through all book records to calculate the available and borrowed books
            for book in books:
                if book['Availability'] == 'Available':
                    available_books += 1
                elif book['Availability'] == 'Borrowed':
                    borrowed_books += 1

            # Calculates the percentage of book currently available
            # The condition prevents division by zero when there are no books in library
            if total_books > 0:
                availability_rate = (available_books / total_books) * 100
            else:
                availability_rate = 0

            print(f"""
            ================= LIBRARY STATISTICS ================
            Total Books       : {total_books}
            Available Books   : {available_books}
            Borrowed Books    : {borrowed_books}
            Availability Rate : {availability_rate:.2f}%
            =====================================================""")

        # OPTION 2: BACK TO MAIN MENU
        elif option_statistics == '2': 
            break

        else:
            print("\nInvalid option. Choose 1 or 2.")



# MAIN MENU 
# It continuously displays the main menu and directs user to the selected function, until they choose Exit
while True:
    print("\n==== LIBRARY MANAGEMENT SYSTEM ====")
    # Displays every menu option that stored in the menu list
    for item in menu:
        print(item)
    user_input = input("Choose menu: ")

    # Routes the user to the appropriate function based on their input
    if user_input == '1':
        viewbooks()
    elif user_input == '2':
        addbook()
    elif user_input == '3':
        updatebook()
    elif user_input == '4':
        deletebook()
    elif user_input == '5':
        statistics()
    # Option 6 exists the entire program (break)
    elif user_input == '6':
        break
    else:
        print("\nInvalid option. Choose 1 - 6.")



