class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return (f'Название книги: {self.title}, автор: \
{self.author}, год издания: {self.year}')

my_book = Book('Война и мир','Лев Толстой', 1867)

print(my_book.get_info())

# print('Название книги: {}, автор: \
# {}, год издания: {}'.format(my_book.title,my_book.author,my_book.year))