# zad 3
import random
import time
from datetime import datetime
from collections import namedtuple

destinations = ("Gdansk", "Gdynia", "Sopot")
sizes = ("A", "B", "C")
Parcel = namedtuple('Parcel', 'destination,send_time, size,serial_number')

def __parcel_generator():
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

parcel_generator = __parcel_generator()
# print(next(parcel_generator))
# print(next(parcel_generator))
# print(next(parcel_generator))
# print(next(parcel_generator))





# def x():
#     for i in range(5):
#         if i==5:
#             parcel5=next(parcel_generator)
#             print(parcel5.size)
# x()