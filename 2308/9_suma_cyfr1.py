#cuma cyfr i pomija litery
string=input('Podaj liczbe:')
suma=0

for znak in string:
    if znak.isnumeric():
        suma=suma+int(znak)
print(suma)
