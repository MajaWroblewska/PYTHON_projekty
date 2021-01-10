
class MyError(Exception):
    pass

number_of_beers=-9

if number_of_beers<=0:
    raise MyError("Iliść piw <=0 - wartość niedozwolona")
