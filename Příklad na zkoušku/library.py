from os.path import join, dirname, realpath
from book import Book

class Library:
    def __init__(self, path_to_file):
        self.books = []
        with open(join(dirname(realpath(__file__)), "data.txt"), "r", encoding="utf_8") as f:
            lines = f.readlines()
            for line in lines:
                self.books.append(Book(line.rstrip()))
        self.books.sort()

    def add_book(self, book):
        if book not in self.books:
            book.set_id(self.get_unique_id())
            self.books.append(book)
            print(f"Kniha přidána s ID: {book.id}")
        else:
            print("Kniha má již unikátní ID")

    def get_unique_id(self):
        return max(book.id for book in self.books) + 1

    def show_available_books(self):
        for book in self.books:
            if book.available:
                print(book)

    def find_book_and_borrow_it(self, name):
        found_books = []
        for book in self.books:
            if book.available == False:
                continue
            if name.lower() in book.name.lower():
                found_books.append(book)

        if len(found_books) == 0:
            print("Kniha nenalezena")
        elif len(found_books) > 1:
            print("Nalezeno více knih")
            for book in found_books:
                print(book)
        else:
            print(found_books)
            odpoved = input("Chcete si knihu půjčit? (A/N): ")
            if odpoved == "A":
                found_books[0].available = False
                print("Kniha půjčena")
            elif odpoved == "N":
                print("Kniha nebyla půjčena")
            else:
                print("Neplatná odpověď")

    def __repr__(self):
        return '\n'.join(map(str, self.books))
