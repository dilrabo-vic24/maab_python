class BookNotFoundException(Exception):
    def __init__(self, title):
        self.title = title
        self.message = f"Book {title} not found in the library"
        super().__init__(self.message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, title):
        self.title = title
        self.message = f"Book {title} is already borrowed"
        super().__init__(self.message)

class MemberLimitExceededException(Exception):
    def __init__(self, name, limit):
        self.limit = limit
        self.message = f"Member '{name}' has reached the maximum limit of {limit} books."
        super().__init__(name. limit)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isborrowed = False

    def __str__(self):
        status = "Borrowed" if self.isborrowed else "Available"
        return f"{self.title} by {self.author} ({status})"
    
class Member:
    MAX_NUMBER = 3
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return self.borrowed_books < self.MAX_NUMBER
    
    def borrow_book(self, book):
        if not self.can_borrow():
            raise MemberLimitExceededException(self.name, self.MAX_NUMBER)
        self.borrow_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def __str__(self):
        borrowed_count = len(self.borrowed_books)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(author=author, title=title)
        self.books.append(book)
        return book
    
    def add_member(self, name):
        member = Member(name=name)
        self.members.append(member)
        return member
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == member.lower():
                return member
        return None
    
    def borrow_book(self, book_title, member_name):

        member = self.find_member(name=member_name)
        if not member:
            raise ValueError(f"Member '{member_name}' not registered.")
        
        book = self.find_book(title=book_title)
        if not book:
            raise BookNotFoundException(title=book_title)
        
        if book.isborrowed:
            raise BookAlreadyBorrowedException(title=book_title)
        
        member.borrow_book(book)
        book.isborrowed = True
        print(f"{member.name} has borrowed '{book.title}'.")

    def return_book(self, book_title, member_name):
        member = self.find_member(member_name)
        if not member:
            raise ValueError(f"Member '{member_name}' not registered.")
        
        book = self.find_book(book_title)
        if not book:
            raise BookNotFoundException(book_title)
        
        if not book.isborrowed:
            print(f"Book '{book_title}' was not borrowed.")
            return
        if book not in member.borrowed_books:
            print(f"{member.name} did not borrow '{book_title}'.")
            return
        member.return_book(book)
        book.is_borrowed = False
        print(f"{member.name} has returned '{book.title}'.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        print("\nLibrary Books:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
    
    def display_members(self):
        if not self.members:
            print("No members registered.")
            return
        
        print("\nLibrary Members:")
        for i, member in enumerate(self.members, 1):
            print(f"{i}. {member}")
            if member.borrowed_books:
                print("   Borrowed books:")
                for j, book in enumerate(member.borrowed_books, 1):
                    print(f"   {j}. {book.title}")


def main():
    library = Library()
    
    library.add_book("O‘tkan kunlar", "Abdulla Qodiriy")
    library.add_book("Mehrobdan Chayon", "Abdulla Qodiriy")
    library.add_book("Kecha va Kunduz", "Chingiz Aytmatov")
    library.add_book("Dunyoning ishlari", "O'tkir Hoshimov")
    library.add_book("Ulug‘bek xazinasi", "Odil Yoqubov")
    
    library.add_member("Shahzoda Karimova")
    library.add_member("Javohir Bekmurodov")
    
    library.display_books()
    library.display_members()
    
    try:
        library.borrow_book("Shahzoda Karimova", "O‘tkan kunlar")
        library.borrow_book("Shahzoda Karimova", "Kecha va Kunduz")
        library.borrow_book("Javohir Bekmurodov", "Dunyoning ishlari")
    except Exception as e:
        print(f"Xatolik: {e}")
    
    library.display_members()
    
    try:
        library.return_book("Shahzoda Karimova", "O‘tkan kunlar")
    except Exception as e:
        print(f"Xatolik: {e}")
    
    library.display_members()
    
    try:
        library.borrow_book("Shahzoda Karimova", "Temur tuzuklari")
    except BookNotFoundException as e:
        print(f"Kutilgan xatolik: {e}")
    try:
        library.borrow_book("Shahzoda Karimova", "Dunyoning ishlari")
    except BookAlreadyBorrowedException as e:
        print(f"Kutilgan xatolik: {e}")
    
    try:
        library.borrow_book("Shahzoda Karimova", "Ulug‘bek xazinasi")
        library.borrow_book("Shahzoda Karimova", "Mehrobdan Chayon")
    except MemberLimitExceededException as e:
        print(f"Kutilgan xatolik: {e}")
    
    library.display_books()
    library.display_members()


if __name__ == "__main__":
    main()

        



