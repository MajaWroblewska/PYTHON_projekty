'Dekorator który pozwoli na dziłanie funkcji tylko w dzień miedzy 7-22'

from datetime import datetime
import time
from functools import wraps         #dekorator podawaniz nazwy f-ji wykonywanej z dekkoratorami
from freezegun import freeze_time   #dekorator zamrożenie czasu


def blokada(func):      #def disable_at_night(func):
    @wraps(func)
    def wrapper(*args, **kwargs):   # *args bo funkcja greet_president przyjmuje jakąś wartość przy wywołaniu-pozycyjne\
                                    # **kwargs bo może f-cja gree_president by mogła przyjmować argumenty nazwane
        start = datetime.now().hour
        if 7<=start<22:      #start>7 and start<22:
            print(f"start: {start}")
            result=func(*args, **kwargs)
            return result
        else:
            print('Jest noc')
    return wrapper


@freeze_time('2020-10-18 5:04:05')

@blokada
def greet_president(name,a="XXIII"):
    print(f'Witam Panie Prezydencie {name} {a}')
    print("***" * 30)
    time.sleep(5)

greet_president('Maja',a='pierwsza')

greet_president('Luc')