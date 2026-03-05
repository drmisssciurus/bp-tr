class Car:
    def __init__(self, model: str, year: int, color: str):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        to_print = f"Car: {self.model}, year: {self.year}, color: {self.color}"
        return to_print

    def turn_right(self):
        print(f"{self.model} turned right")

    def turn_left(self):
        print(f"{self.model} turned left")

    def stop(self):
        print(f"{self.model} stopped")


car1 = Car("Toyota-Corolla", 2018, "white")
car2 = Car("BMW-X5", 2022, "black")
car3 = Car("Tesla-Model-3", 2023, "red")
car4 = Car("Audi-A4", 2020, "gray")
car5 = Car("Honda-Civic", 2017, "blue")

car_list = [car1, car2, car3, car4, car5]

for car in car_list:
    print(car)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, {self.pages} pages"



book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Grokking Algorithms, 2nd Edition", "Aditya Bhargava", 336)
book3 = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 435)

books_list = [book1, book2, book3]

for book in books_list:
    print(book)

