# zad 8

# sorting_facility
from itertools import chain
class SortingFacility:
    def __init__(self):
        self.parcels = []   #lista paczek

    def take_parcels_from_sender(self, parcels_from_sender): #lista paczek wsadza do
        sender_name=parcels_from_sender[0].sender_name
        print(f"{len(parcels_from_sender)} new parcels in facility from: {sender_name}")
        self.parcels.append(parcels_from_sender) #dodawanie paczek do listy SoringFa

    def _sort_parcels(self): #sortowanie paczek
        for parcel in chain(*self.parcels):
            print(parcel) #dopisać