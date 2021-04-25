'dekorator'
from datetime import datetime

def greet_time(func):
    def wrapper():
        print(f"Dekorator 'greet_time'\nNew guest arrived at {datetime.now()}")
        func()
        print("---- po funkcji 'greet_time' ----")
    return wrapper

@greet_time
def greet():
    print("Hello guest")

# greet()

# print("---")
## greet_with_time = greet_time(greet)
## greet_with_time()
# print("---")
### greet_time(greet)()

'Zad27\'' \
'Napisz dekorator do_twice, który każdą funkcję, którą dekoruje wywoła dwukrotnie.\
Napisz funkcję greet_president, która napisze uroczyste powitanie prezydenta i z szacunku \
udekoruj ją napisanym dekoratorem.'

def do_twice(func):
    def wraper():
        print('Func 2 razy:')
        # func()
        # func()
        return func(),func()
    return wraper   # zwracnie funkcji to bez nawiasów a wraper() -> wywołanie funkcji

@do_twice
def greet_president():
    print('Witam Panie Prezydencie')
# greet_president()

'zad28\ '
'Dopisz dekorator @greet_time do funkcji witającej prezydenta (zad 27) i sprawdź wpływ kolejności \
dekoratorów na rezultat wywołania funkcji.'


@greet_time
@do_twice
def greet_president():
    print('FUN=Witam Panie Prezydencie')

greet_president()
print('koniec *** greet_time + do_twice ***\n')


@do_twice
@greet_time
def greet_president():
    print('FUN=Witam Panie Prezydencie')

greet_president()
print('koniec *** do_twice + greet_time ***\n')
