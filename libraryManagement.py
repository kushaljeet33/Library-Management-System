class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.checked_out = False

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"Book(ID: {self.book_id}, Title: '{self.title}', Author: {self.author}, Status: {status})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __repr__(self):
        return f"Member(ID: {self.member_id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)})"


class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.transactions = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
            return f"Book '{title}' added successfully."
        return "Book with this ID already exists."

    def remove_book(self, book_id):
        if book_id in self.books:
            book = self.books.pop(book_id)
            return f"Book '{book.title}' removed successfully."
        return "Book not found."

    def search_book(self, book_id):
        return self.books.get(book_id, None)

    def add_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
            return f"Member '{name}' added successfully."
        return "Member with this ID already exists."

    def remove_member(self, member_id):
        if member_id in self.members:
            member = self.members.pop(member_id)
            return f"Member '{member.name}' removed successfully."
        return "Member not found."

    def search_member(self, member_id):
        return self.members.get(member_id, None)

    def checkout_book(self, member_id, book_id):
        member = self.search_member(member_id)
        book = self.search_book(book_id)

        if not member:
            return "Member not found."
        if not book:
            return "Book not found."
        if book.checked_out:
            return "Book is already checked out."

        book.checked_out = True
        member.borrowed_books.append(book)
        self.transactions[book_id] = member_id
        return f"Book '{book.title}' checked out to '{member.name}'."

    def return_book(self, member_id, book_id):
        member = self.search_member(member_id)
        book = self.search_book(book_id)

        if not member:
            return "Member not found."
        if not book:
            return "Book not found."
        if not book.checked_out or self.transactions.get(book_id) != member_id:
            return "This book was not checked out by this member."

        book.checked_out = False
        member.borrowed_books.remove(book)
        del self.transactions[book_id]
        return f"Book '{book.title}' returned by '{member.name}'."

    def list_books(self):
        return '\n'.join(str(book) for book in self.books.values())

    def list_members(self):
        return '\n'.join(str(member) for member in self.members.values())


def get_input(prompt):
    return input(prompt).strip()

def display_message(message):
    print(message)


def main():
    lms = LibraryManagementSystem()
    
    while True:
        display_message("\nLibrary Management System")
        display_message("1. Add Book")
        display_message("2. Remove Book")
        display_message("3. Search Book")
        display_message("4. Add Member")
        display_message("5. Remove Member")
        display_message("6. Search Member")
        display_message("7. Checkout Book")
        display_message("8. Return Book")
        display_message("9. List All Books")
        display_message("10. List All Members")
        display_message("11. Exit")
        
        choice = get_input("Enter your choice: ")
        
        if choice == '1':
            book_id = get_input("Enter book ID: ")
            title = get_input("Enter book title: ")
            author = get_input("Enter book author: ")
            message = lms.add_book(book_id, title, author)
            display_message(message)
        
        elif choice == '2':
            book_id = get_input("Enter book ID: ")
            message = lms.remove_book(book_id)
            display_message(message)
        
        elif choice == '3':
            book_id = get_input("Enter book ID: ")
            book = lms.search_book(book_id)
            display_message(str(book) if book else "Book not found.")
        
        elif choice == '4':
            member_id = get_input("Enter member ID: ")
            name = get_input("Enter member name: ")
            message = lms.add_member(member_id, name)
            display_message(message)
        
        elif choice == '5':
            member_id = get_input("Enter member ID: ")
            message = lms.remove_member(member_id)
            display_message(message)
        
        elif choice == '6':
            member_id = get_input("Enter member ID: ")
            member = lms.search_member(member_id)
            display_message(str(member) if member else "Member not found.")
        
        elif choice == '7':
            member_id = get_input("Enter member ID: ")
            book_id = get_input("Enter book ID: ")
            message = lms.checkout_book(member_id, book_id)
            display_message(message)
        
        elif choice == '8':
            member_id = get_input("Enter member ID: ")
            book_id = get_input("Enter book ID: ")
            message = lms.return_book(member_id, book_id)
            display_message(message)
        
        elif choice == '9':
            display_message("\nAll Books:")
            display_message(lms.list_books())
        
        elif choice == '10':
            display_message("\nAll Members:")
            display_message(lms.list_members())
        
        elif choice == '11':
            display_message("Exiting...")
            break
        
        else:
            display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
