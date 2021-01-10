#Zadanie 2 – lokata
#Napisz skrypt, który, który obliczy stan konta za kilka lat. Program pyta użytkownika o:

#stan początkowy konta,
#stopę oprocentowania rocznego (zwróć uwagę, że odsetki podlegają miesięcznej kapitalizacji)
#liczbę lat na lokacie.
#Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu. Wypisz np. takie zdanie:
#Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.

start = float(input("Stan początkowy konta wynosi: \n"))

#np. stopa oprocenotwania 6% = 0.06
rate = float(input("Stopa oprocenotowania w skali roku: \n"))

n = int(input("Liczba lat na lokacie: \n"))
end = start*(1 + rate*n)

print("Po {} latach kapitał będzie wynosił {} zł".format(n, end))

#--------------------------------------------------------
# 2 Drugie to uwzględnienie średniej inflacji przez okres lokaty –
# tak aby sprawdzić czy faktycznie zyskujemy czy może mimo wzrostu nominalnej wartości kapitału,
# tak naprawdę tracimy 😉
# Dzięki temu możemy jaką będzie miał realną siłę nabywczą kapitał, który wypłacimy z lokaty.
# Założenia:
# — poziom inflacji jest w granicach celu NBP, czyli około 2.5%
# — inflacja jest indeksowana raz do roku (przekładając na nasze „odsetki” naliczane są raz na rok)

# wynik2= podatekBelki,
# start= kapitalPoczatkowy,
# wynik5 = zyskNetto,

start=float(input("Stan początkowy konta:"))
stopa=float(input('Stopa oprocentowania w %:'))
czas=int(input('Okres lokaty w latach:'))
czas2= czas*12
tax=0.19
inflation=0.025
stopa2=stopa/100
wynik = start * ((1 + (stopa2/12)) ** (12*czas))
wynik2= (wynik-start)*tax
wynik3= (wynik-wynik2-start)*inflation
wynik4= wynik-wynik2-wynik3
wynik5= wynik4-start
print('Twoje {:.0f} zł przez {} lata na lokacie {} % urośnie do {:.2f} zł.'.format(start, czas, stopa, wynik4))
print('Twoj zysku w ciagu {} miesiecy bedzie wynosil: {:.2f} zl'.format(czas2,wynik5))

#-------------------------------------------
# -*- coding: UTF-8 -*-

#kapital = input("Podaj wartość kapitału początkowego: ")

print("Program oblicz sumę odsetek z lokaty")

kapital = float(input("Wprowadź kapitał początkowy: "))
opr = float(input("Wprowadź oprocenotwanie loakty (np. 2.7 == 2.7%): "))
liczbaLat = float(input("Wprowadź okres lokaty: "))

"""
Założenia:
    --kapitalizacja odsetek następuje co miesiac
    --oprocenowanie podawane jest jako % poczym zamieniany jest na ułamek dziesiętny
    --liczbaLat może zostać podana jako ułamek dziesiętny np. 0.25 - oznacza 3 miesięca; 0.3333 oznacza 4 miesiace 
"""

odsetki = ((1+(opr/100)/12)**(12*liczbaLat)-1)*kapital
inflacja = ((1+2.5/100)**liczbaLat-1)*kapital;

print("Twoje początkowe {:.2f}zł przez {:.2f} lat na lokacie {:.2f}% urośnie do {:.2f}" .format(kapital, liczbaLat, opr, odsetki+kapital))
print("-"*50)
print("Kapitał początkowy:      {:15.2f} zł".format(kapital))
print("Oprocentowanie:          {:15.2f}".format(opr))
print("Okres lokaty:            {:15.2f}".format(liczbaLat))
print("Odsetki brutto:          {:15.2f} zł".format(odsetki))
print("Odsetki netto:           {:15.2f} zł".format(odsetki*0.81))
print("-"*50)
print("Kapitał po {:.2f} latach:      {:15.2f} zł".format(liczbaLat,odsetki*0.81+kapital))
print("Wartość nabywcza po {:.2f} latach i uwzględnieniu średniej inflacji(2.5%): {:.2f}".format(liczbaLat,odsetki*0.81+kapital-inflacja))

#---------------------------
#print(„Stan początkowy:”)
#stanp=float(input())
#print(„Stopa oprocentowania, w %:”)
#stopa=float(input())
#print(„Okres lokaty, w latach:”)
#czas=int(input())
#stopa2=stopa/100
#wynik = stanp * ((1 + (stopa2/12)) ** (12*czas))
#print(„Twoje {} zł przez {} lata na lokacie {} % urośnie do {:.2f} zł.” .format(stanp, czas, stopa, wynik))

#-------------------------------------------------
#start = float(input(„Please provide your initial balance: „))
#rate = float(input(„What is your yearly % rate gain: „))
#period = int(input(„How many years will you keep the account: „))
#rate2 = rate/100
#end_b = (start*((1 + rate2 / 12)) ** 12 * period)
#tax = (end_b – start)*19/100
#end = end_b – tax

#print(„Your initial {:.2f} will grow to {:.2f} in {} years including monthly capitalization and tax cut.”.format(start, end, period))

#-------------------------------------------------
#print(„Obliczenie zysku z lokaty terminowej”)
#stan = int(input(„Podaj stan początkowy konta w zł:”))
#stopa = int(input(„Podaj stope oprocentowania rocznego lokaty w procentach:”))
#lata = int(input(„Liczbę lat na lokacie:”))
#dni = lata * 365
#wynik = (stan * stopa / 100 * dni / 365) + stan
#print(„Twoje”, stan, „zł przez”, lata, „lat na koncie z oprocentowaniem”, stopa,”% urośnie do”, wynik,”zł”)

#-----------------------------------------------------
# stanpocz = int(input(„Podaj stan początkowy konta”))
# oprocentowanie = float(input(„Podaj stope oprocentowania”))*0.01
# czas = int(input(„Podaj czas kapitalizacji latach”))*12
# stan = stanpocz*(1 + oprocentowanie/12)**czas
# print(„Twoje {} zł przez {} lata na lokacie {} % urośnie do {:.2f}.”.format(stanpocz,int(czas/12),oprocentowanie,stan))

#---------------------------------------------------------


