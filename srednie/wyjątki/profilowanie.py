

# timeit.timeit(stmt=None,setup=None, timer=None, number=None, globals=None)

# stmp=blok kodu do zmierzenia czasu
# setup= kod który zostaje wykonany przez wykonaniem statement np. importy mogułów
# number= ile razy ma byćwykonany kod

import timeit


setup = '''
from time import sleep
import random
from sender2 import Sender
from sorting_facility import SortingFacility
import random

number_of_days = 3  #

senders = (Sender("Jan Kowalski", "Tczew"),)  # , by sender był iterowalny jako tupla
# Sender("Maria Rutkowska", "Rumia"),
# Sender("Jerzy Brzuszek", "Wejherowo"))

facility = SortingFacility()  # inicjalizacja klasy z plikiu sorting.py
'''

code = '''

for _ in range(number_of_days):
    for sender in senders:
        parcels = sender.prepare_parcels(random.randint(2, 10)) #dostajemy paczki
        facility.take_parcels_from_sender(parcels)# przekazyjemy do sortowni
        # facility.long_parcels() #zad 32
        print(facility.parcels_sorted_by_destination) # -> {'Gdansk': [lista paczek...],

    sleep(1)
'''
print(timeit.timeit(stmt=code, setup=setup))
