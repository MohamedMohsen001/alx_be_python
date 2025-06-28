class Book:
    _is_checked_out = False
    
    def __init__(self, title, author):
         self.title = title
         self.author = author
         
    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False
    
class Library:
    _books =  []
    
    def __init__(self):
        pass
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out == True:
                    book.check_out()
                    self.list_available_books()
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
                    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")