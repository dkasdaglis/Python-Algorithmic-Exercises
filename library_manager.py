# Project: Library Management System
# Description: A CRUD-like system to manage books, loans, and ratings using Dictionaries.

def display_menu():
    print("\n=== LIBRARY SYSTEM ===")
    print("1. Show all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Rating Statistics")
    print("5. Exit")

# Initial Data (Translated to English)
Library = {
    '9789604618020': {'title': 'The Iliad', 'author': 'Homer', 'is_available': True},
    '9789604619126': {'title': '1984', 'author': 'George Orwell', 'is_available': True},
    '9789604617153': {'title': 'The Prince', 'author': 'Machiavelli', 'is_available': True},
    '9789604618884': {'title': 'The Republic', 'author': 'Plato', 'is_available': True}
}

ratings = {
    '9789604618020': [4, 5, 4],
    '9789604619126': [5, 4, 5, 4],
    '9789604617153': [3, 4, 4],
    '9789604618884': [4, 3, 4, 4]
}

def display_books():
    print("-" * 90)
    print(f"{'ISBN':<15} {'TITLE':<25} {'AUTHOR':<20} {'STATUS'}")
    print("-" * 90)
    for isbn, details in Library.items():
        status = "AVAILABLE" if details['is_available'] else "BORROWED"
        print(f"{isbn:<15} {details['title']:<25} {details['author']:<20} {status}")
    print("-" * 90)

def borrow_book():
    isbn = input("Enter ISBN: ")
    if isbn not in Library:
        print("Book not found.")
        return
    
    if not Library[isbn]['is_available']:
        print(f"Sorry, '{Library[isbn]['title']}' is already borrowed.")
        return
    
    name = input("Enter borrower's name: ")
    Library[isbn]['is_available'] = False
    print(f"Success! {name} borrowed '{Library[isbn]['title']}'.")

def return_book():
    isbn = input("Enter ISBN: ")
    if isbn not in Library:
        print("Book not found.")
        return

    if Library[isbn]['is_available']:
        print(f"Error: '{Library[isbn]['title']}' is not currently borrowed.")
        return
    
    # Process Return and Rating
    Library[isbn]['is_available'] = True
    print(f"Returned: {Library[isbn]['title']}")
    
    while True:
        try:
            score = int(input("Please rate this book (1-5): "))
            if 1 <= score <= 5:
                if isbn in ratings:
                    ratings[isbn].append(score)
                else:
                    ratings[isbn] = [score]
                print("Rating saved.")
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input.")

def display_stats():
    print("\n--- BOOK RATINGS ---")
    for isbn, scores in ratings.items():
        if isbn in Library:
            avg = sum(scores) / len(scores)
            book = Library[isbn]
            print(f"{book['title']} | Average Rating: {avg:.1f} ({len(scores)} votes)")

# --- Main Loop ---
while True:
    display_menu()
    choice = input("Select option (1-5): ")

    if choice == "1":
        display_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        display_stats()
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
