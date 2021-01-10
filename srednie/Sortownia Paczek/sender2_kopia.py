#połąćzenie plików
# wysyłanie paczek

import parcels2
from time import sleep

class Sender:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def _prepare_parcel(self): #wywołuje kolejny obiekt generatora
        sleep(0.01)         # it takes some time to prepare parcel...
        new_package = next(parcels2.parcel_generator)    #tworzenie instancji tupla / import z pliku terza obiekt
        # print(type(new_package)) # tupla
        # sender_details = (sender_name, sender_origin)
        # sender_details = (self.name, self.origin)   #zmienna przetrzymuje zmienne name i origin tupla
        new_package.sender_name=self.name #przypisanie zmiennych do pól
        new_package.sender_origin=self.origin #przypisanie zmiennych do pól
        return new_package      #dodawanie

    def prepare_parcels(self, n):   #n ile paczek generujemy-prygotawanie wszystkich paczek
        ' n - ilosc paczek '
        return [self._prepare_parcel() for _ in range(n)]

sender1=Sender(name='DHL',origin='Gdansk')
sender2=Sender(name='DPD',origin='Sopot')
# paczki=sender1.prepare_parcels(10)    #odchaszować do zad 6?
#
# for paczka in paczki:
#     print(paczki)
# paczka
