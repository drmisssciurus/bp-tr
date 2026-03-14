class Book:
	def __init__(self, title:str, author:str,pages:int):
		self._title = ''
		self._author = ''
		self._pages = 0

		self.set_title(title)
		self.set_author(author)
		self.set_pages(pages)

	def get_title(self):
		return self._title
	def get_author(self):
		return self._author
	def get_pages(self):
		return self._pages

	def set_title(self, title):
		if isinstance(title, str) and title.strip():
			self._title = title
		else:
			print("Invalid title")

	def set_author(self, author):
		if isinstance(author, str) and author.strip():
			self._author = author
		else:
			print("Invalid author")

	def set_pages(self, pages):
		if isinstance(pages, int) and pages > 0:
			self._pages = pages
		else:
			print("Invalid pages")

	def __str__(self):
		return f"title: {self._title}| author: {self._author} | pages: {self._pages}"

	def __repr__(self):
		return f"title={self._title}, author={self._author}, pages={self._pages}"

class FictionBook(Book):
    def __init__(self, title: str, author: str, pages: int, genre: str):
        super().__init__(title, author, pages)
        self._genre = ""
        self.set_genre(genre)

    def get_genre(self):
        return self._genre

    def set_genre(self, genre):
        if isinstance(genre, str) and genre.strip():
            self._genre = genre
        else:
            print("invalid genre")

    def __str__(self):
        return f"Fiction Book-> {super().__str__()} | genre: {self._genre}"

class KidsFictionBook(FictionBook):  # Book->FictionBook
    def __init__(self, title: str, author: str, pages: int, genre: str, age: int):
        super().__init__(title, author, pages, genre)
        self._age = 0
        self.set_age(age)

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            print("invalid age")

    def get_age(self):
        return self._age

    def __str__(self):
        return f"KidsFiction Book-> {super().__str__()} | age: {self._age}"


class EducationBook(Book):
    def __init__(self, title: str, author: str, pages: int, subject: str):
        super().__init__(title, author, pages)
        self._subject = ""
        self.set_subject(subject)

    def get_subject(self):
        return self._subject

    def set_subject(self, subject):
        if isinstance(subject, str) and subject.strip():
            self._subject = subject
        else:
            print("invalid subject")

    def __str__(self):
        return f"Education Book-> {super().__str__()} | subject: {self._subject}"

library = [
    FictionBook("1984", "George Orwell", 328, "dystopia"),
    FictionBook("Dune", "Frank Herbert", 540, "science fiction"),
    FictionBook("Dracula", "Bram Stoker", 418, "horror"),

    KidsFictionBook("Harry Potter1", "J.K. Rowling", 350, "fantasy", 10),
	KidsFictionBook("Harry Potter2", "J.K. Rowling", 345, "fantasy", 10),
	KidsFictionBook("Harry Potter3", "J.K. Rowling", 7568, "fantasy", 10),

	KidsFictionBook("Alice in Wonderland", "Lewis Carroll", 200, "fantasy", 7),
    KidsFictionBook("The Little Prince", "A. de Saint-Exupery", 120, "philosophical", 8),

    EducationBook("Python Basics", "John Smith", 400, "programming"),
    EducationBook("Physics 101", "Albert Newton", 500, "physics"),
    EducationBook("Math for Beginners", "Kate Brown", 350, "mathematics"),
    EducationBook("History of Europe", "Anna White", 600, "history")
]

# for b in library:
# 	print(b)
#
# print(library)

# def validate_non_empty_str(value, field_name):
# 	if not isinstance(value, str):
# 		print(f"{field_name} must be a non-empty string")
# 	elif not value.strip():
# 		print(f"{field_name} must be a non-empty string")
# def find_books_by_authors(books, author):
# 	if isinstance(author, str) and isinstance(books, list):
# 		return [book for book in books if book.get_author().lower() == author.lower()]
# 	else: return []

# books1=find_books_by_authors(library, "J.K. Rowling")
# for b in books1:
# 	print('hehe', b)


# def find_books_by_title_part(books, title_part):
# 	if isinstance(title_part, str) and isinstance(books, list):
# 		new_list = []
# 		for book in books:
# 			if book.get_title().lower().find(title_part.lower()) >= 0:
# 				new_list.append(book)
# 		return new_list
# 	return []



def find_books_by_title_part(books, title_part):
	if not isinstance(books, list) or not isinstance(title_part, str):
		return []

	title_part = title_part.lower()
	return [book for book in books if title_part in book.get_title().lower()]

# print(find_books_by_title_part(library, 'potter'))

