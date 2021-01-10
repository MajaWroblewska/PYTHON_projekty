'Zad 6-zmniany zad 3\
Zmodyﬁkuj kod pliku parcels.py, by zamiast krotki zawierał dataclass Parcel ze wszystkimi do tej pory \
potrzebnymi parametrami (destination, send_time, size, serial_number, sender_name, sender_origin).\
Parametrom, których nie ustawia bezpośrednio generator (sender_name, sender_origin) przypisz wartości domyślne None.\
Zmodyﬁkuj plik sender.py, by aktualizował pola sender_name i sender_origin każdej utworzonej paczki.'

import random
import time
from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime

destinations=('Wrocław','Toruń','Rzeszów')
sizes=('A','B','C')
# Parcel = namedtuple('Parcel','destination, send_time, size, serial_number') #zdefiniowanie nametuple - 1str z przecinkami wew


@dataclass
class Parcel:
    destination: str
    send_time: int
    size: str
    serial_number: int
    sender_name: str = None
    sender_origin: str = None

def __parcel_generator(): #generator paczek
    serial_number =1
    while True:
        time.sleep(1)
        destination = random.choice(destinations)
        send_time = str(datetime.now())
        size = random.choice(sizes)
        yield Parcel(destination = destination,     #zwraca namedtuple o nazwie Parcels
                     send_time = send_time,
                     size = size,
                     serial_number = serial_number,)   #'yield' bo to jest generator

        serial_number+=1


parcel_generator=__parcel_generator()   #wywołanie przez nadanie nazwy
# print(next(parcel_generator))   #kolejne uruchomienie generatora
# print(next(parcel_generator))
# print(next(parcel_generator))
# print(next(parcel_generator))

# parcel1=next(parcel_generator)    #dostęp do pól stworzonego obiektu 'parcels1'
# print(parcel1)
# print(parcel1.destination)
# print(parcel1.send_time)
# print(parcel1.size)
# print(parcel1.serial_number)