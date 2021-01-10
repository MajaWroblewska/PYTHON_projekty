'''Zad 8\
Symulacja dnia:
Stworzyć kilku nadawców paczek
Stworzyć jedną sortownię
W pętli przez zdeﬁniowaną liczbę dni:
Każdy nadawca generuje losową liczbę paczek z narzuconego przedziału
Każdy nadawca przekazuje swoje paczki do sortowni (poprzez take_parcels_from_sender)
Po odebraniu paczek od wszystkich nadawców, sortownia przygotowuje paczki
(sort_parcels - na ten moment wypisanie wszystkich paczek po kolei)'''

import random
from Maja_sender_8 import Sender
from Maja_SortingFacility_8 import SortingFacility


number_of_days = 3  #

senders = (Sender("Maja Wroblewska", "Koło"), #, by sender był iterowalny jako tupla
           Sender('Kuba Narloch','Leszno'),
           Sender("Sylwia Mały", "Tyniec"))

facility = SortingFacility()    #inicjalizacja klasy z plikiu sorting.py
                                ##tworzenie 1 srtowni,  inicjalizacja klasy z plikiu Maja_SortingFacility_8 (#sorting.py)


for _ in range(number_of_days):  #W pętli przez zdeﬁniowaną liczbę dni
    for sender in senders:
        parcels = sender.prepare_parcels(random.randint(2, 5)) #dostajemy paczki od nadawcy\
                                        # #Każdy nadawca generuje losową liczbę paczek z narzuconego przedziału
        facility.take_parcels_from_sender(parcels)  #Każdy nadawca przekazuje swoje paczki do sortowni (poprzez take_parcels_from_sender)
                                             ## przekazyjemy do sortowni
    facility.sort_parcels()                #Po odebraniu paczek od wszystkich nadawców, sortownia przygotowuje paczki
                #(sort_parcels - na ten moment wypisanie wszystkich paczek po kolei)
