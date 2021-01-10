'Zad 8'
'''Wspólnie rozbudujmy naszą aplikację o moduł sortowni (sorting_facility.py)\ 
oraz zróbmy symulację dnia pracy (day_simulation.py)\
W tym ćwiczeniu ważne jest dopytanie o szczegóły oraz dokładne zapoznanie się z wymaganiami poniżej.\
Sortownia:\
-Stworzyć klasę SortingFacility, która będzie przechowywać paczki i wykonywać na nich operacje z danego dnia
-Zainicjować listę parcels\
-Dodać metodę resetującą stan listy paczek na początku dnia (start_day)\
-Zaimplementować metodę take_parcels_from_sender dodającą podaną jako argument listę \
paczek do zmiennej parcels (nie rozpakowywać i nie modyfkować wejścia). Metoda ta \
wypisuje, ile paczek nowych paczek przyszło do sortowni.\
-Zaimplementować metodę sort_parcels, która na razie wypisuje wszystkie paczki i \
    używa funkcji chain na liście parcels przechowywanej wewnątrz klasy'''


# import parcels
import Maja_parcels_6
from time import sleep


class Sender:
    def __init__(self,name,origin):
        self.name = name    # pole nadawcy = name
        self.origin = origin    # pole pochodzenia = origin

    def _prepare_parcel(self):   #metoda do tworzenia kolejnej paczki- wywołuje kolejny obiekt generatora
        sleep(0.01)
        new_package = next(Maja_parcels_6.parcel_generator) #importowanie z pliku Maja_parcel_6.py obiektu 'parcel_generator' (linia 43) \
        # new_package = next(Maja_parcels_3.parcel_generator) #importowanie z pliku Maja_parcel_3.py obiektu 'parcel_generator' (linia 32) \
        # new_package = next(parcels.parcel_generator) #importowanie z pliku parcels.py(linia 25) obiektu 'parcel_generator'
        # parcels.py(linia 25) = Maja_parcel_3.py
        new_package.sender_name = self.name #???
        new_package.sender_origin = self.origin #???
        # sender_details = (self.name, self.origin)   #przypisanie detali do wysyłki - krotka z danymi nadwacy i pochdzenia
        return new_package #+ sender_details     #zwraca połączoną tuple =paczka +nadawca(senedr + origin)

    def prepare_parcels(self,n):     #trorzenie N-paczek - wszystkich paczek
        ' n - ilosc paczek '
        return [self._prepare_parcel() for i in range(n)]
