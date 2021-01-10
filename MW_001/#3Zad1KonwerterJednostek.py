#Zadanie 1 – konwerter jednostek
#Utwórz nowy plik np. jednostki.py, który po podaniu przez użytkownika długości w cm będzie wyświetlał wynik w metrach i calach zaokrąglając do 4 miejsc po przecinku.
#Podobny skrypt możesz wykonać dla zamiany kg na funty.
#1 cal = 25,4 mm=2,54cm
#1 kilogram =2,20462262 funta
#Wynik wyświetl używając dowolnego sposobu formatowania tekstu.

#dlugosc=float(input("Podaj długość w cm\n"))
#print("Długość",'{:,.3f}'.format(dlugosc).replace(',',' '),"cm to:",'{:,.6f}'.format(dlugosc/100).replace(',',' '),"m")

waga=float(input("Podaj wagę w kg\n"))
print("Waga ok",'{:,.3f}'.format(waga).replace(',',' '),"kg to:",'{:,.6f}'.format(waga*2.20462262).replace(',',' '),"funtów")

dlugosc=float(input("Podaj długość w cm\n"))
print("Długość",'{:,.3f}'.format(dlugosc).replace(',',' '),"cm to:"
      ,'{:,.6f}'.format(dlugosc/100).replace(',',' '),"m"
    " lub",'{:,.3f}'.format(dlugosc/2,54).replace(',',' '),'cala')

#zamiana na m i cale
cm = float(input("Podaj długość w cm: "))
cm_to_m = cm/100
cm_to_cal = cm/0.394

print("Długość {} cm to {} metrów lub {:.3f} cali".format(cm, cm_to_m, cm_to_cal))

#zamiana na funty
kg = int(input("Podaj wagę w kg: "))
kg_to_g = kg * 1000
kg_to_funt = kg * 2.4419

print("Waga {}kg to {}g lub {:.4f} funty".format(kg, kg_to_g,kg_to_funt))