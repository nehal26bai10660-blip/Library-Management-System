
from library.book import Book

from library.library import Library


def test_book_creation():
    book = Book("THE ALCHEMIST", "PAULO COELHO", True)

    assert book.title=="THE ALCHEMIST"

    assert book.author=="PAULO COELHO"
    assert book.available is True
def test_borrow_book():


     book = Book("NARUTO","KISHIMOTO",True)

     book.borrow()

     assert book.available is False
def test_return_book():
    book =Book("NARUTO","KISHIMOTO",False)

    book.return_book()
    assert book.available is True


def test_library_add_book():
    library=Library()

    book=Book("THE ALCHEMIST", "PAULO COELHO", True)
    library.books.append(book)

    assert len(library.books)==1
    assert library.books[0].title=="THE ALCHEMIST"

def test_library_remove_book():
  library = Library()

  book = Book("THE ALCHEMIST", "PAULO COELHO", True)
  library.books.append(book)

  library.remove_book("THE ALCHEMIST")

  assert len(library.books) == 0