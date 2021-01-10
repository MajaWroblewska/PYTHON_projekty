'''#suma cyfr liczby np 123=1+2+3

liczba=input('Wpisz liczbę: ') #int daje str ale on nie jest iterowalny w pętli for
suma=0 #wartośc sumy początkowa
for cyfra in liczba:
    #print(type(cyfra), cyfra)  #sprawdzenie
    int_cyfra = int(cyfra)      #zamienia str'cyfra' na liczbę int
    #print(int_cyfra, type(int_cyfra))
    #print('suma to:',int_cyfra+suma) #pokazuje kolejną sumę cyfr
    suma +=int_cyfra

print(suma)'''


liczba=input('Wpisz liczbę: ')

while True:
    suma = 0

    for cyfra in liczba:
        # print(cyfra) #printuje 321
        suma=int(cyfra)+suma
    #print(suma)

    if suma<10:
        break
    else:
        liczba=str(suma)
print(suma)



