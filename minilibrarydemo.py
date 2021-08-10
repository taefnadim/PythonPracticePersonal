# Displaybook() : To display the available books
# Lendbook(): To lend a book to a user
# Addbook(): To add a book in the library
# Returnbook(): To return the book in the library.


class Library:

    def __init__(self, library_name, list_of_books):
        self.list_of_books = list(list_of_books)
        self.library_name = library_name
        self.lender_dict = {}
        print("Welcome to", self.library_name)

    # Compulsory methods 
    def displayBooks(self):
        """
        Displays the books available in the library
        """
        print("Books available in the library: ")
        for book in self.list_of_books:
            print(book)

    def lendBook(self):
        def lenderCanIssueBook():
            for key, value in self.lender_dict.items():
                if value == lender_name:
                    return False
            return True

        lender_name = input("Enter your name: ").lower()
        if lenderCanIssueBook():
            bookToIssue = input("Enter the book name: ").lower()
            if bookToIssue in self.list_of_books:
                newItem = {bookToIssue: lender_name}
                self.lender_dict.update(newItem)
                self.list_of_books.remove(bookToIssue)
                print("Book issued successfully")
            else:
                print("Sorry no such book exists !")
        else:
            print("Sorry you cannot issue more than one book at a time")

    def addBook(self):
        """
        Helps in donating book the library
        """
        bookName = input("Enter the book name: ")
        self.list_of_books.append(bookName)  # adds at the end
        print("Book added successfully")

    def returnBook(self):
        """
        Returns the book back to the library
        """
        bookToReturn = input("Enter the book name: ").lower()
        if bookToReturn in self.lender_dict.keys():
            del self.lender_dict[bookToReturn]
            self.list_of_books.append(bookToReturn)
            print("Book returned successfully")
        else:
            print("Sorry, no such book is issued yet")

    # Additional method
    def printLenderList(self):
        for key, value in self.lender_dict.items():
            print(f"{value} has issued {key}")


mLib = Library("satlib", "ramayan", "mahabharat")


def main():
    while 1:
        choice = input(">> ").lower().replace(" ", "")
        if choice == "displaybook":
            mLib.displayBooks()
        elif choice == "lendbook":
            mLib.lendBook()
        elif choice == "addbook":
            mLib.addBook()
        elif choice == "returnbook":
            mLib.returnBook()
        elif choice == "printlenderlist":
            mLib.printLenderList()
        elif choice == "exit":
            break
        else:
            print("Not a valid command !")
    print("Library is closed now")


main()