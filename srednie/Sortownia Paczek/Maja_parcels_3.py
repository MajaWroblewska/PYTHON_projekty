'Zad 3\
W pliku parcels.py zdeﬁniuj namedtuple o nazwie Parcel i polach destination, send_time, size, \
serial_number. Zwracaj typ Parcel zamiast poprzednio przygotowanej krotki.'

import random
import time
from collections import namedtuple
from datetime import datetime

destinations=('Wrocław','Toruń','Rzeszów')
sizes=('A','B','C')
Parcel = namedtuple('Parcel','destination, send_time, size, serial_number') #zdefiniowanie nametuple - 1str z przecinkami wew
# Parcel = namedtuple('Parcel',['destination', 'send_time', 'size', 'serial_number']) # nametuple - lista
# Parcel = namedtuple('Parcel','destination send_time size serial_number') # nametuple- spacje


def __parcel_generator(): #generator paczek
    serial_number =0
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