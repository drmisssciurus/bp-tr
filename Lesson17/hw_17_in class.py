from Lesson16_OOP_inheritance.hw_in_class import Product, mini_market
from Lesson16_OOP_inheritance.hw_in_class_2 import Book, FictionBook, KidsFictionBook, EducationBook

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



def find_books_by_min_pages(books:list, min_pages:int) -> list:
	new_books = []
	if not isinstance(min_pages, int) or not isinstance(books, list):
			return new_books
	return [n for n in books
	        if isinstance(n, Book) and n.get_pages() >= min_pages]

result = find_books_by_min_pages(library, 1100)
for book in result:
	print('my',book)


def find_prod_by_price_range(products:list, price_from: float|int, price_to: float|int) -> list:
	if not isinstance(products, list):
		return []
	if not isinstance(price_from,(int, float)) or not isinstance(price_to,(int, float)):
		return []
	if price_from < 0 or price_from > price_to:
		return []
	return [
		p for p in products
		if isinstance(p, Product) and price_from<=p.get_price()<=price_to
	]

print(find_prod_by_price_range(mini_market, 1, 100))