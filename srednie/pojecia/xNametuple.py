from collections import namedtuple

person_1 = ("Jan", "Kowalski", 23)
Person = namedtuple("Person", "name surname age")
person_2 = Person("Jan", "Kowalski", 23)
person_2.age
