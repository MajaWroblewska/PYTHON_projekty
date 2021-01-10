# czy jest PANGRAMEM (wielkość liter jest NIE ważna-proba)
import string  #inportowanie metod stringu

alfabet=string.ascii_lowercase    #alfabet małymi literami (string.ascii_uppercase -

print(alfabet, type(alfabet))
napis=input('Podaj napis a ja sprawdzę czy jest on PANGRAMEM-zaiera wszystkie litery alfabetu ')


alfabet_set=set(alfabet) #zamiana str alfabet na set
napis_set=set(napis.lower())    #zamiana str napis na set

print(alfabet_set, napis_set) # wypisanie setów
roznica=alfabet_set.difference(napis_set)    #roznica działa tylko na setach wiec jw. i zwraca na set
print('Roznica zbiorów ALFABET i NAPIS to:',roznica)

print('Długość roznicy to:',len(roznica))

if len(roznica)==0:
    print('Wpisany tekst jest PANGRAMEM')
else:
    print('To nie jest PANGRAM, bo nie wykożystałeś wszystkich liter alfabetu')


