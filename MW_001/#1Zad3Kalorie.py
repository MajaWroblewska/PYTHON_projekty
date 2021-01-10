# Podstawa: 10 x masa ciała + 6.25 x wzrost w cm – 5 x wiek + S
# współczynnik S: dla kobiet = -161, dla mężczyzn= +5




waga=int(input('Podaj swoją wagę w kg:\n'))
wzrost=int(input('Podaj swój wzrost w cm:\n'))
wiek=int(input('Podaj swój wiek:\n'))
sex=input('Wybierz płeć K/M\n')

s=0
if sex=="k":
    s=-161
#    PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + s

else:
    s=5
#    PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + s


print('Praca siedząca, brak dodatkowej aktywności fizycznej........................= 1,2\n'
      'Praca niefizyczna, mało aktywny tryb życia................................  = 1,4\n'
      'Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu.... = 1,6\n'
      'Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu............= 1,8\n'
      'Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu.................= 2,0')


print()
aktywnosc=float(input(('Określ swoją aktywność fizyczną:')))
print()

PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + s

print('Podstawa kaloryczna PPM',PPM)
print("Dzienne Twoje zapotrzebowanie kaloryczne wynosi:", PPM * aktywnosc, "kcal")