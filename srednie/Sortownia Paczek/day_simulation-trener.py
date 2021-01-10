from time import sleep
import random
from sender import Sender
from sorting_facility import SortingFacility
number_of_days = 1
senders = (
    Sender("Jan Kowalski", "Tczew"),
            )
           # Sender("Maria Rutkowska", "Rumia"),
           # Sender("Jerzy Brzuszek", "Wejherowo"))
print(senders)
facility = SortingFacility()
for _ in range(number_of_days):
    for sender in senders:
        parcels = sender.prepare_parcels(random.randint(2, 10))
        facility.take_parcels_from_sender(parcels)
    sleep(1)