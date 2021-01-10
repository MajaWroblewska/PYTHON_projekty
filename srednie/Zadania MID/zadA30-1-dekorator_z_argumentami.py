'zad30\
Napisz dekorator funkcji, który przed wykonaniem zacznie mierzyć czas a na koniec wypisze:\
Nazwę wykonanej funkcji, wszystkie argumenty przekazane do funkcji, czas wykonania.\
Samodzielnie zaproponuj funkcje, które udekorujesz i sprawdzisz działanie dekoratora.'

from datetime import datetime
import time
from functools import wraps

def do_twice(func):
    @wraps(func)
    def wraper(*args,**kwargs):
        # print('Func 2 razy:')
        func(*args, **kwargs)
        func(*args, **kwargs)

        # return func(),func()
    return wraper   #zwracanie funkcji to bez nawiasów a wraper() -> wywołanie funkcji


def czas(func):
    @wraps(func)        #możemy wypprintować nazwę funkcji
    def wrapper(*args, **kwargs):   # *args bo funkcja greet_president przyjmuje jakąś wartość przy wywołaniu-pozycyjne\
                                    # **kwargs bo może f-cja greet_president by mogła przyjmować argumenty nazwane
        start=time.time()
        # print(f"start: {start}")

        result=func(*args, **kwargs)        #result=100**100000

        stop=time.time()
        # print(f"stop: {stop}")
        czas=stop-start
        print(f'czas funkcji: {czas} sekund')   #print(f'czas{time.tine()-start}')
        print(f'Nazwa funkcji: {func.__name__}')
        print(f'Agruments: {args}')
        # print(f'Keyword arguments: {[k,v for k,v in kwargs.items()]}')
        print(f'Keyword arguments: {kwargs}')
        print("***" * 30)
        return result
    return wrapper


@czas
@do_twice
def greet_president(name,a="XXIII"):
    print(f'Witam Panie Prezydencie {name} {a}')
    time.sleep(5)

@czas
def some(a):
    return a**1000000

some(100)

greet_president('Maja',a='pierwsza')
greet_president('Luc')