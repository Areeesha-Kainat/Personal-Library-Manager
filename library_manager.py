import json
import os

LIBRARY_FILE = "library.json"

# Load the library from a file
def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return []
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []  # Return empty if file is corrupted

# Save the library to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book(library):
    print("\n📖 Add a New Book")
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter book genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    print(f"\n✅ '{title}' added successfully!")

# Remove a book
def remove_book(library):
    if not library:
        print("\n📚 Your library is empty!")
        return

    title_to_remove = input("\nEnter the title of the book to remove: ").strip().lower()

    for book in library:
        if book["title"].lower() == title_to_remove:
            library.remove(book)
            save_library(library)
            print(f"\n✅ '{book['title']}' has been removed!")
            return
    
    print("\n⚠️ Book not found!")

# Search for a book by title or author
def search_book(library):
    if not library:
        print("\n📚 Your library is empty!")
        return

    print("\n🔍 Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice (1/2): ").strip()
    
    query = input("\nEnter search term: ").strip().lower()
    
    results = []
    for book in library:
        if (choice == "1" and query in book["title"].lower()) or \
           (choice == "2" and query in book["author"].lower()):
            results.append(book)

    if results:
        print("\n📖 Matching Books:")
        for idx, book in enumerate(results, start=1):
            status = "Read ✅" if book["read"] else "Unread ❌"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("\n⚠️ No books found!")

# Display all books
def display_books(library):
    if not library:
        print("\n📚 Your library is empty!")
        return

    print("\n📚 Your Book Collection:")
    for idx, book in enumerate(library, start=1):
        status = "Read ✅" if book["read"] else "Unread ❌"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_statistics(library):
    if not library:
        print("\n📚 Your library is empty!")
        return

    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"✅ Books read: {read_books} ({percentage_read:.2f}%)")

# Main function with menu system
def main():
    library = load_library()
    
    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\n📖 Library saved! Goodbye! 👋")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    main()
