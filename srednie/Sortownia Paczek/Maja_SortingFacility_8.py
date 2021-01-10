'zad 8'
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
    używa funkcji chain na liście parcels przechowywanej wewnątrz klasy\
Symulacja dnia:
Stworzyć kilku nadawców paczek
Stworzyć jedną sortownię
W pętli przez zdeﬁniowaną liczbę dni:
Każdy nadawca generuje losową liczbę paczek z narzuconego przedziału
Każdy nadawca przekazuje swoje paczki do sortowni (poprzez take_parcels_from_sender)
Po odebraniu paczek od wszystkich nadawców, sortownia przygotowuje paczki 
(sort_parcels - na ten moment wypisanie wszystkich paczek po kolei)'''

from itertools import chain

class SortingFacility:
    def __init__(self):
        self.parcels = [] #zainicjowana lista parcels

    def take_parcels_from_sender(self,parcels_from_sender):
        print(f'{len(parcels_from_sender)} new parcels in facility-nowych paczek w sortowni')   #ile nowych paczep przyszło do sortowi
        self.parcels.append(parcels_from_sender)    #dodawanie nowej paczki do listy paczek = parcels

    def sort_parcels(self): #
        for parcel in chain(*self.parcels):
            print(parcel)   #Zaimplementować metodę sort_parcels, która na razie wypisuje wszystkie paczki \
                            # i używa funkcji chain na liście parcels przechowywanej wewnątrz klasy



