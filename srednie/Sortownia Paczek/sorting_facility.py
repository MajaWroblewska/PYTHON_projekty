# zad 8

# sorting_facility
from collections import defaultdict
from functools import wraps
from itertools import chain, groupby
from pprint import pprint

def log_sorting_facility_status(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Function name: {func.__name__}")
        print(f"Arguments passed: {args}")
        print(f"Keyword arguments: {kwargs}")
        result=func(self, *args, **kwargs)
        try:
            self.log_parcels()
        except AttributeError as exc:
            print(f'Brak metody log_parcels = No log_parcels method {exc}')
        return result
    return wrapper

class SortingFacility:
    def __init__(self):
        self.parcels_sorted_by_destination = defaultdict(list)
        # self.parcels_sorted_by_destination = {}     #słownik paczek zad 19


    @log_sorting_facility_status
    def take_parcels_from_sender(self, parcels_from_sender): #lista paczek wsadza do -wywołuje _sort_parcels pponiżej
        # sender_name=parcels_from_sender[0].sender_name
        print(f"{len(parcels_from_sender)} new parcels in facility")
        # zmiana wymagań, paczki sortujemy od razu po odebraniu od nadawcy
        self._sort_parcels(parcels_from_sender)


    def _sort_parcels(self,parcels):
        sorted_parcels=sorted(parcels, key=lambda parcel: parcel.destination) #sortowanie po mieście by zrobić groupby
        # print(sorted_parcels)

        for destination, parcels in groupby(sorted_parcels, lambda parcel: parcel.destination):

            # if destination not in self.parcels_sorted_by_destination.keys():              #zad19
            #     self.parcels_sorted_by_destination[destination]= []  # self.parcels_sort_by_ to lista - \
            #                                             # i tworze pustą liste by móc póżniej kozystać a append poniżej
            # self.parcels_sorted_by_destination[destination].append(len(list(parcels)))    #drukuje tylko ilość paczek
            for parcel in list(parcels):    #appenduje każdy element listy
                self.parcels_sorted_by_destination[destination].append(parcel)       #self.parcels_sort_by_ to lista
                                                                         # self.parcels_sort_by_ to lista
            # self.sum(parcels_sorted_by_destination[destination])????    #suma paczek z danego miasta??
        # print(self.parcels_sorted_by_destination)
            # print(destination)
            # print(parcels)

    # def log_parcels(self):
    #     pprint(dict(self.parcels_sorted_by_destination))#zamieniamy difoltdict na zwykłego
    #     for city, parcels in self.parcels_sorted_by_destination.items():
    #         print(f'Miasto: {city}, ilość pczaczek: {len(parcels)}')

# -> {'Gdansk': [lista paczek...],