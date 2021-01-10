from collections import defaultdict
from statistics import mean
from itertools import groupby

cars_prices = [('GLS', 300), ('A', 20), ('CLA', 400), ('GLS', 450), ('A', 12)]
cars = defaultdict(list)

for model, price in cars_prices:
    cars[model].append(price)

# print(cars)
# print('średnia cena auta GLS:',mean(cars["GLS"]))
# print('średnia cena auta A:',mean(cars["A"]))
# print('średnia cena auta CLA:',mean(cars["CLA"]))

schronisko=["Cat Alek", "Dog Marian", "Cat Szczepan", "Rat Cat", "Dog Reksio"]
animals=defaultdict(list)
# for i in schronisko:
#     print(i,)
for i in schronisko:
    i.split(i)
    print(i)

# for name, group in groupby(schronisko, lambda x: x[:3]):
#     print(name)
#     print(list(group))


# for zwierz, imie in schronisko:
#     animals[zwierz].append(imie)

# print(animals)