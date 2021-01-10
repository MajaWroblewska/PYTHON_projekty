# a=None
# b=1
#
# print(dir(a))       #wyświetli dostepne metody dla None czyl tylko magiczne
# print(dir(b))       #wyświetli dostepne metody dla b=1 czyl magiczne i zwykłe

############################################################################
class Zwierze(object):
    def __init__(self, imie, waga, wiek):
        self.wiek = wiek
        self.imie = imie
        self.waga = waga
    def jedz(self, ilosc):
        self.waga += ilosc
class Kot(object):
    def __init__(self):
        pass
class Pies(Zwierze):
    def __init__(self, lata, masa, nazwa, rasa, wielkosc):
        self.rasa = rasa
        self.rozmiar = wielkosc
        Zwierze.__init__(self, nazwa, masa, lata)
    def __str__(self):
        return "To jest pies"

psiak = Pies(5, 600, "Reks", "York", "sredni")
# print(psiak)
# print(psiak.rasa)
# print(psiak.rozmiar)
# print(psiak.wiek)
# print(psiak.imie)
# print(psiak.waga)
# print(psiak.jedz(1000))
# print(psiak.waga)

# print(dir(psiak))       #dostepne metody na obieckie (psiak)
print(str(psiak))
print(psiak)