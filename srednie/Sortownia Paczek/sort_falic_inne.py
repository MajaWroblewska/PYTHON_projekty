# zad 8

# sorting_facility
from itertools import chain, groupby


class SortingFacility:
    def __init__(self):
        self.parcels_sorted_by_destination = {}  # słownik paczek

    def take_parcels_from_sender(self, parcels_from_sender):  # lista paczek wsadza do -wywołuje _sort_parcels pponiżej
        # sender_name=parcels_from_sender[0].sender_name
        print(f"{len(parcels_from_sender)} new parcels in facility")
        # zmiana wymagań, paczki sortujemy od razu po odebraniu od nadawcy
        self._sort_parcels(parcels_from_sender)

    def _sort_parcels(self, parcels):
        sorted_parcels = sorted(parcels,
                                key=lambda parcel: parcel.destination)  # sortowanie po mieście by zrobić groupby
        print(sorted_parcels)

        for destination, parcels in groupby(sorted_parcels, lambda parcel: parcel.destination):
            if destination not in self.parcels_sorted_by_destination.keys():
                self.parcels_sorted_by_destination[destination] = list(parcels)  # self.parcels_sort_by_ to lista !!!!!!!!!!!
            else:   #!!!!!!!!!!!!!!
                self.parcels_sorted_by_destination[destination].append(list(parcels))  # self.parcels_sort_by_ to lista

            # print(destination)

            # print(parcels)

# -> {'Gdansk': [lista paczek...],