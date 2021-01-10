# zad 6 zmiany zad 3

import random
import time
from datetime import datetime
from collections import namedtuple
from dataclasses import dataclass

destinations = ("Gdansk", "Gdynia", "Sopot")
sizes = ("A", "B", "C")
# Parcel = namedtuple('Parcel', 'destination,send_time, size,serial_number') #tupla wczsśniejsza

@dataclass
class Parcel:
    destination: int
    send_time: int
    size: int
    serial_number: int
    sender_name: str =None
    sender_origin: str =None

def __parcel_generator():   #generatot przesyłak
    serial_number = 0
    while True:
        # time.sleep(2)
        destination = random.choice(destinations)
        send_time = str(datetime.now())
        size = random.choice(sizes)
        yield Parcel(destination=destination,
                     send_time=send_time,
                     size=size,
                     serial_number=serial_number
                     )
        serial_number += 1

parcel_generator = __parcel_generator()     #metoda klasy Parcel-wywoalnie metody odwolujemy sie do niej



# print(next(parcel_generator))
# print(next(parcel_generator))
# print(next(parcel_generator))
#
# parcel1=next(parcel_generator)
# print(parcel1.destination)


