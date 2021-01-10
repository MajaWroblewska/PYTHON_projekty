class SortingFacility:
    def __init__(self):
        self.parcels_sorted_by_destination = {}

    # @log_sorting_facility_status_after_method

    def take_parcels_from_sender(self, parcels_from_sender):
        print(f"{len(parcels_from_sender)} new parcels in facility")
        # zmiana wymagań, paczki sortujemy od razu po odebraniu od nadawcy
        self.sort_parcels(parcels_from_sender)
    def sort_parcels(self, parcels):
        # uzupełnij o nową metodę sortowania