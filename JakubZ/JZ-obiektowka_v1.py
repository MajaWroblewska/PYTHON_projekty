import random
import datetime
import time

class Telefon(object):
    def __init__ (self, oem, model, liczba1, liczba2):
        self.data = [oem, model]
        self.OEM = oem
        self.model = model
        self.ID = random.randint(0, 999999)
        self.production_date = datetime.datetime.now()

        self.x = liczba1
        self.y = liczba2

        print(f'{self.OEM} {self.model} {self.ID}')

    def fun(self):
        return self.x + self.y

    def age(self):
        time.sleep(4)
        end = datetime.datetime.now()
        return end - self.production_date

Telefon('Samsung', 'Coop', 4, 10)
a = Telefon('Samsung', 'Galaxy S9', 5, 10)
print(a.age())
print(a.fun())

