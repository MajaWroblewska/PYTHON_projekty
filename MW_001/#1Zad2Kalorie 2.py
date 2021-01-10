to, ja = "Maja", "Wroblewska"
print(to)
print(ja)

waga = int(input("Podaj swoją wagę w kg: \n"))
wzrost = int(input("Podaj swój wzrost w cm: \n"))
wiek = int(input("Podaj swój wiek:\n"))
s = input("Podaj swoją płeć w formacie M lub K: \n")
S = 0
if s == 'M':
    S = 5
else:
    S = -161

BMI = waga/((wzrost/100)**2)

aktywność = {'a':1.2, 'b':1.4, 'c':1.6, 'd':1.8, 'e':2.0}
p = input('Jaką pracę wykonujesz? Podaj porszę odpowiednią literę:\n'
          'a:Praca siedząca, brak dodatkowej aktywności fizycznej.\n'
          'b:Praca niefizyczna, mało aktywny tryb życia.\n'
          'c:Lekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu.\n'
          'd:Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu.\n'
          'e:Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu\n'
          'Podaj a lub b lub c lub d lub e: ')
ap = aktywność[p]
#print(S) – tylko kontrolnie, aby mieć pewność że warunek działa
PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + s
print('///////////////////////////////////////////////////')

print('Twoja masa ciała BMI to: ' + str(round(BMI,2)))
print('——————————')
print('Współczynnik PPM to: ' + str(PPM))
kalorie = PPM * ap
print('——————————')
print('Twoje zapotrzebowanie kalorie to: ' + str(kalorie))

#pętla
#activity = int(input('Wybierz numer odpowiadający twojej aktywności fizycznej: \n'
#                    'Praca siedząca, brak dodatkowej aktywności fizycznej – 1\n'
#                    'Praca niefizyczna, mało aktywny tryb życia – 2\n'
#                    'Lekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu – 3\n'
#                    'Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu – 4\n'
#                    'Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu – 5n'))

#if activity == 1:
#    multiplier = 1.2
#if activity == 2:
#   multiplier = 1.4
#if activity == 3:
#    multiplier = 1.6
#if activity == 4:
#   multiplier = 1.8
#if activity == 5:
#   multiplier = 2.0