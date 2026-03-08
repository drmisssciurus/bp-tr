class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Pages: {self.__pages}"

    def set_title(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            self.__title = "Unknown title"

    def get_title(self):
        return self.__title

    def set_author(self, author):
        if isinstance(author, str):
            self.__author = author
        else:
            self.__author = "Unknown author"

    def get_author(self):
        return self.__author

    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            self.__pages = 0

    def get_pages(self):
        return self.__pages

class FictionBook(Book):
    def __init__(self, title: str, author: str, pages: int, genre: str):
        super().__init__(title, author, pages)
        self.__genre = genre

    def __str__(self):
        return f"{super().__str__()}, genre: {self.__genre}"

    def set_genre(self, genre):
        if isinstance(genre, str):
            self.__genre = genre
        else:
            self.__genre = "Unknown fiction book"

    def get_genre(self):
        return self.__genre

class EducationBook(Book):
    def __init__(self, title: str, author: str, pages: int, subject: str):
        super().__init__(title, author, pages)
        self.__subject = subject

    def __str__(self):
        return f"{super().__str__()}, subject: {self.__subject}"

    def set_subject(self, subject):
        if isinstance(subject, str):
            self.__subject = subject
        else:
            self.__subject = "Unknown education book"

    def get_subject(self):
        return self.__subject

class KidsFictionBook(FictionBook):
    def __init__(self, title: str, author: str, pages: int, genre: str, age: int):
        super().__init__(title, author, pages, genre)
        self.__age = age

    def __str__(self):
        return f"{super().__str__()}, age: {self.__age}+"

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

book1 = FictionBook("Dune", "Frank Herbert", 412, "Sci-Fi")
book2 = FictionBook("The Hobbit", "J.R.R. Tolkien", 310, "Fantasy")
book3 = FictionBook("1984", "George Orwell", 328, "Dystopia")

book4 = EducationBook("Grokking Algorithms", "Aditya Bhargava", 256, "Algorithms")
book5 = EducationBook("Python Crash Course", "Eric Matthes", 544, "Programming")
book6 = EducationBook("Clean Code", "Robert Martin", 464, "Software Engineering")
book7 = EducationBook("Introduction to Algorithms", "Cormen", 1312, "Computer Science")

book8 = KidsFictionBook("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 309, "Fantasy", 10)
book9 = KidsFictionBook("Alice in Wonderland", "Lewis Carroll", 200, "Fantasy", 8)
book10 = KidsFictionBook("Charlie and the Chocolate Factory", "Roald Dahl", 176, "Adventure", 7)



library = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

for book in library:
    print(book)