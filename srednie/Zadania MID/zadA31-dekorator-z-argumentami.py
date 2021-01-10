'zad31\
Zmodyﬁkuj dekorator z zadania 30, aby przyjął argumenty typu bool z domyślnymi wartościami \
True: name, args, kwags, execution_time. W zależności od argumentów wypisuj dane informacje lub nie.\
zmienić!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

from datetime import datetime
import time
from functools import wraps


def czas(name=True,print_args=True,print_kwargs=True,execution_times=True):
    def decorator_czas(func):
        @wraps(func)
        def wrapper(*args, **kwargs):   # *args bo funkcja greet_president przyjmuje jakąś wartość przy wywołaniu-pozycyjne\
                                        # **kwargs bo może f-cja gree_president by mogła przyjmować argumenty nazwane
            start=time.time()
            print(f"start: {start}")
            func(*args, **kwargs)
            stop=time.time()
            print(f"stop: {stop}")
            czas=stop-start
            print(f'czas funkcji: {czas} sekund')
            print("***" * 30)
        return wrapper
    return decorator_czas

@czas(name=False,print_kwargs=False)
def greet_president(name,a="XXIII"):
    print(f'Witam Panie Prezydencie {name} {a}')
    time.sleep(5)


greet_president('Maja',a='pierwsza')
greet_president('Luc')