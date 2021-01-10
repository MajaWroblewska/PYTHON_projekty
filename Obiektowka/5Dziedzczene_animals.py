class Animals(object):
    def __init__(self,name,weight,age):
        self.name=name
        self.weight=weight
        self.age=age
        self.__noga=2   # pole prywatne
        self._uszy=3    #pole chronione
    def jedz(self,kg):
        self.weight=self.weight+kg
        print(f"Zjadłeś {kg} więc ważysz teraz {self.weight}")

class Kot(Animals):
    def __init__(self,name,wasy,umaszczenie, wiek, waga):
        self.name=name
        self.wasy='ma'
        self.umaszczenie=umaszczenie
        Animals.__init__(self,name,waga,wiek)   #

    def daj_glos(self):
        self.sound='miow miow'
        return self.sound


a=Animals('Reks',10,2)
print('imię Animals:',a.name, '\nwaga:',a.weight, '\nwiek:',a.age)

k=Kot("maja", 'a','rudy',wiek=5,waga=2)       #mam dostęp do pól Animals np.dziedziczę wagę (wada=a.weight)
print('imię kota:',k.name)
print('waga kota:',k.weight)
print('wiek kota:',k.age)
print('wąsy kota:',k.wasy)
print('umaszczenie:',k.umaszczenie)
print('dzwięk:', k.daj_glos())

a.jedz(3)   #karmienie zwierza
k.jedz(3)   #karmienie kota
print('wąsy:',k.wasy)

# print(a.__noga)       # wywołanie prywtne nie da
print('uszy:',a._uszy)          # wywołanie chronione możliwe
print('czy ma 3 uszy?:',a._uszy==3)       #
print('po karmieniu Animal waży:',a.weight)
