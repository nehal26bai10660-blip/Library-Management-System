
from .library import Library


def main():
    library=Library()

    while True:
        print("=" * 20, "LIBRARY", "=" * 20)
        print("  " * 5, "1. DISPLAY ALL BOOKS")

        print("  " * 5, "2. DISPLAY AVAILABLE BOOKS")

        print("  " * 5, "3. SEARCH FOR A BOOK",end='\n')
        print("  " * 5, "4. BORROW BOOK")

        print("  " * 5, "5. RETURN BOOK")
        print("  " * 5, "6. REMOVE BOOK",end='\n')
        print("  " * 5, "7. ADD BOOK")
        print("  " * 5, "8. EXIT")

        print("=" * 46)

        try:
             ch=int(input("Enter your choice (1/2/3/4/5/6/7/8): "))

        except ValueError:
               print("Invalid input!Please enter a number from 1 to 8 !")
               continue

        if ch ==1:
            library.display_all_books()
        elif ch==2:

              library.display_available_books()

        elif ch==3:
             
             t =input("Enter title of book: ").strip()
             library.search_book(t)

        elif ch==4:
            t=input("Enter title of book: ").strip()
            library.borrow_book(t)
        elif ch ==5:
             
             t=input("Enter title of book: ").strip()
             library.return_to_library(t)

        elif ch==6:
            t = input("Enter title of book: ").strip()
            library.remove_book(t)
        elif ch ==7:
           library.add_book()
        elif ch==8:
              print("Thank you for using the Library Management System!:)")
              break

        else:
                print("Invalid choice!!!! Please choose between 1 and 8.!!!")

        input("Press enter to continue...")


if __name__ == "__main__":
    main()