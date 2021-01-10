from dataclasses import dataclass

@dataclass()    # nie możemy modyfikować pół w klasie-
                    # #nie trzeba konstruktora
class Person:
    author: str = 12
    name: str ='Mat'# musi być typ str a nie dowolne słowo

person=Person()
print((person.author, person.name))
person.name='Kot'
print(person.name)