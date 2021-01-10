#połąćzenie plików
# wysyłanie paczek

import parcels
from time import sleep

class Sender:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def _prepare_parcel(self): #wywołuje kolejny obiekt generatora
        sleep(0.01)         # it takes some time to prepare parcel...
        new_package = next(parcels.parcel_generator)
        # sender_details = (sender_name, sender_origin)
        sender_details = (self.name, self.origin)
        return new_package + sender_details

    def prepare_parcels(self, n):   #n ile paczek generujemy-prygotawanie wszystkich paczek
        return [self.prepare_parcel() for _ in range(n)]