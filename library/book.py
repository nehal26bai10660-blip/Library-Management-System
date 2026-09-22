class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def display(self):
        print(f"TITLE: {self.title}")
        print(f"AUTHOR: {self.author}")
        print(f"AVAILABLE: {self.available}")

    def borrow(self):
        if not self.available:
            print(f"SORRY {self.title} is already borrowed!")
        else:
            print(f"You borrowed {self.title}.")
            self.available = False

    def return_book(self):
        if self.available:
            print(f"{self.title} is already in library.")
        else:
            print(f"You have returned {self.title}.")
            self.available = True