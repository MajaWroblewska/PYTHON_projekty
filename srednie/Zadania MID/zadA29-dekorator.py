'zad29\ '
'Zmodyﬁkuj dekorator do_twice by pasował do każdego rodzaju funkcji. \
Wymyśl 3 rodzaje funkcji: z argumentami pozycyjnymi, z argumentami nazwanymi i mieszaną \
oraz bez argumentów. Przetestuj, że dekorator działa z każdą z funkcji.'

from datetime import datetime

def greet_time(func):
    def wrapper():
        print(f"New guest arrived at {datetime.now()}")
        func()
        print("----")
    return wrapper

def do_twice(func):
    def wraper(*args,**kwargs):
        # print('Func 2 razy:')
        func(*args, **kwargs)
        func(*args, **kwargs)

        # return func(),func()
    return wraper   #zwracanie funkcji to bez nawiasów a wraper() -> wywołanie funkcji

# 1-dekorator
@do_twice
# @greet_time
def greet_president(name):
    print(f'Witam Panie Prezydencie {name}')

greet_president(name='Abraham')

print(greet_time.__name__)



