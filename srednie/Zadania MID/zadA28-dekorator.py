'zad28\ '
'Dopisz dekorator @greet_time do funkcji witającej prezydenta (zad 27) i sprawdź wpływ kolejności \
dekoratorów na rezultat wywołania funkcji.'

from datetime import datetime

def greet_time(func):
    def wrapper():
        print(f"New guest arrived at {datetime.now()}")
        func()
        print("----")
    return wrapper

def do_twice(func):
    def wraper():
        # print('Func 2 razy:')
        # func()
        # func()
        return func(),func()
    return wraper   #zwracanie funkcji to bez nawiasów a wraper() -> wywołanie funkcji

#1-dekorator
@do_twice
@greet_time
def greet_president():
    print('Witam Panie Prezydencie')

# greet_president() #musi być z dekoratorami 1 lub 2


# 2-dekorator
@greet_time
@do_twice
def greet_president():
    print('Witam Panie Prezydencie')

greet_president() #musi być z dekoratorami 1 lub 2

# do_twice(greet_time(greet_president))()    #to jest dekorator 1
# greet_time(do_twice(greet_president()))()   #to jest dekorator 2

