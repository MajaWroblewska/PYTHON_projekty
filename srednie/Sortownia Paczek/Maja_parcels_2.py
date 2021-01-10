'Zad 2\
destinations = ("Gdansk", "Gdynia", "Sopot")\
sizes = ("A", "B", "C")\
def __parcel_generator():\
\
# wpisz kod, który:\
# zwraca krotkę składającą się z: \
# - losowej lokalizacji z kolekcji destinations\
# - aktualnej daty\
# - losowego rozmiaru z kolekcji sizes\
# - kolejnego numeru seryjnego (większy o 1 dla każdego wywołania)'

import random
import time
from datetime import datetime

destinations=('Wrocław','Toruń','Rzeszów')
sizes=('A','B','C')

def __parcel_generator(): #generator paczek
    serial_number =0
    while True:
        time.sleep(1)
        destination = random.choice(destinations)
        send_time = str(datetime.now())
        size = random.choice(sizes)
        yield (destination, send_time,size,serial_number,)   #'yield' bo to jest generator

        serial_number+=1


parcel_generator=__parcel_generator()   #wywołanie przez nadanie nazwy
print(next(parcel_generator))   #kolejne uruchomienie generatora
print(next(parcel_generator))
print(next(parcel_generator))
print(next(parcel_generator))