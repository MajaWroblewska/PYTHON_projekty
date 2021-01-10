# dataclass
#(frozen=True) # nie możemy modyfikować pól w klasie-
# nie trzeba konstruktora

from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Book:
    name: str # wartośc domyślna name='wa'
    author: str #wymuszamy typ str
    # page: int ()

#namedtuple
Book_namedtuple=namedtuple('Book_nametuple','name author') #klasa Book_namedtuple
book1=Book_namedtuple(name='Hrabia', author='Dumas') #obiekt klasy Book

#dataclass-obiekt klasy Book
book2= Book('Hrabia','Dumas',)       #obiekt klasy Book
print('name:',book2.name)
print('author:',book2.author)

#tuple
book3=('Hrabia' ,'Dumas', )    #tupla zwykła

#słownik zwyky
book4={'name':'Hrabia','author':'Dumas'} #słownik zwykły

print('named-dataclass:',book1 == book2)
print('named-tuple:',book1 == book3)
print('named-dict:',book1 == book4)
print('dataclass-tuple:',book2 == book3)
print('dataclass-dict:',book2 == book4)
print('tuple-dict:',book3 == book4)

# print(book1.author)


