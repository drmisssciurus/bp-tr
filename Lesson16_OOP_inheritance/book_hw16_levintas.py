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