class Uzytkownik(object):
    def __init__(self,nazwa,haslo,email,databas):
        self.nazwa= nazwa
        self.haslo= haslo
        self.email= email
        self.x = x

h = 'abc'
a=Uzytkownik(h,'haslo','wrob@x.pl', None)
print(a)
print(a.nazwa)
print(a.haslo)
print(a.email)
print(a.x)

class BazaDanych(object):
    def __init__(self):
        self.UsersDatas ={}    #tworzywy pusty słownik o nazwie UsersData z danymi użytkowników

    def DodajUzytkonika(self,user):
        # ma powstać slownik poczatkowy : klucz ->'login' a wartość -> user {'login':user}
        # self.usersDatas={name:user}
print(


a=Uzytkownik()
# db=BazaDanych()
# db.DodajUzytkownika(a)
#
# b=BazaDanych()
# print(b)

print(Uzytkownik.nazwa)
print(Uzytkownik.haslo)
print(Uzytkownik.email)
