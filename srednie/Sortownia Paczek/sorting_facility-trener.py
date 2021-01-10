class SortingFacility:
    def __init__(self):
        self.parcels_sorted_by_destination = defaultdict(list)
    @log_sorting_facility_status
    def take_parcels_from_sender(self, parcels_from_sender):
        sender_name = parcels_from_sender[0].sender_name
        print(
            f"{len(parcels_from_sender)} new parcels in facility from {sender_name}"
        )
        self._sort_parcels(parcels_from_sender)

    def _sort_parcels(self, parcels: list):
        parcels_sorted_by_dest = sorted(parcels, key=lambda parcel: parcel.destination)
        for destination, parcels in groupby(parcels_sorted_by_dest, lambda parcel: parcel.destination):
            for parcel in list(parcels):
                self.parcels_sorted_by_destination[destination].append(parcel)

    def log_parcels(self):
        pprint(dict(self.parcels_sorted_by_destination))
        for city, parcels in self.parcels_sorted_by_destination.items():
            print(f"{city}, parcels count: {len(parcels)}")