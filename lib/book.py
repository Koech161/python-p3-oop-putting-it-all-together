#!/usr/bin/env python3
class Book:
    def __init__(self,  title='And Then There Were None', page_count=272):
        self.title = title
        self.page_count = page_count  
        self._turn_page = 0

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print('page_count must be an integer')

    @property
    def turn_page(self):
        return self._turn_page

    # @turn_page.setter
    # def turn_page(self, value):
    #     if isinstance(value, int) and 0 <= value <= self._page_count:
    #         self._turn_page = value
    #     else:
    #         print('turn_page must be an integer between 0 and page_count')

    def turn_page(self):
        if self._turn_page < self._page_count:
            self._turn_page += 1
            print('Flipping the page...wow, you read fast!')
        else:
            print("You've reached the end of the book.")
           

    def __str__(self):
        return f'Title: {self.title}, Page Count: {self.page_count}, Turn Page: {self.turn_page}'
book = Book("The World According to Garp", 69)
print(book)
book.turn_page()
print(book)                 