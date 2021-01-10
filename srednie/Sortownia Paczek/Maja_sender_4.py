'Zad 4\
Przygotuj plik sender.py, który będzie korzystał z generatora parcel_generator do przygotowania \
listy paczek do nadania.\
\
Zapoznaj się z tym modułem, będziemy go modyﬁkować w kolejnym ćwiczeniu. \
Napisz próbny kod tworzący klasę Sender i generujący listę paczek z wykorzystaniem metody prepare_packages.\
Zwróć uwagę na to, jaki typ danych znajduje się w zwróconej tablicy i dlaczego.'

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
        sender_details = (self.name, self.origin)   #przypisanie detali do wysyłki - krotka z danymi nadwacy i pochdzenia
        return new_package + sender_details     #zwraca połączoną tuple =paczka +nadawca(senedr + origin)

    def prepare_parcels(self,n):     #trorzenie N-paczek - wszystkich paczek
        ' n - ilosc paczek '
        return [self._prepare_parcel() for i in range(n)]
