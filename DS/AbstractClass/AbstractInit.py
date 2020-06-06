from abc import ABCMeta, abstractmethod
from abc import ABC
class Book(ABC):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display():
        pass
class MyBook(Book):
    price = 0
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display():
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))
test = MyBook('Mine Kalf','Hitler', 9823)