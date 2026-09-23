from .book import Book
from .validators import validate_title, validate_author

class Library:
    def __init__(self):
       self.books = []

    def add_book(self):
        T=input("Enter title: ").strip().upper()
        A=input("Enter author: ").strip().upper()
        if not validate_title(T):
            print("Title cannot be empty.")

            return


        if not validate_author(A):

            print("Author cannot be empty.")
            return
        obj = Book(T, A, True)
        for bk in self.books:
           if T == bk.title:
                print(f"{T} already in library.")
                break
        else:
            self.books.append(obj)
            print("Book added successfully")



    def remove_book(self, title):
        for bk in self.books:
            if title.upper() == bk.title.upper():
                self.books.remove(bk)
                print(f"{title} removed from library.")
                break
        else:
            print("Book not found!!!")

    def display_all_books(self):
        if not self.books:
            print("Library is empty")
        else:
             for bk in self.books:
               bk.display()
    def search_book(self, title):
        for bk in self.books:

             if title.upper() == bk.title.upper():
                bk.display()
                break
        else:
            print("Book not found!!")

    def display_available_books(self):
        c = 0
        for bk in self.books:
              if bk.available:
                bk.display()
                c += 1
        if c == 0:
              print("No books are currently available.")
    def borrow_book(self, title):
        for bk in self.books:
          if title.upper() == bk.title.upper():
                  bk.borrow()
                  break
        else:
            print(f"{title} not found!!")

    def return_to_library(self, title):
        for bk in self.books:
            if title.upper() == bk.title.upper():
                 bk.return_book()
                 break
        else:
            print(f"{title} is not library book.")