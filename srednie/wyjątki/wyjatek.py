
class MyError(Exception):
    pass

number_of_beers= -2
# number_of_beers= 8

if number_of_beers<=0:
    raise MyError("Iliść piw <=0 - wartość niedozwolona")
else:
    print('Wszystko ok')
    # raise MyError('OK')


