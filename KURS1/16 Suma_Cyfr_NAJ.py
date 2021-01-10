#1 suma cyfr liczby np 1239=1+2+3+9=15

liczba=input('Wpisz liczbę: ') #int daje str ale on nie jest iterowalny w pętli for
suma=0  #wartośc sumy początkowa

for cyfra in liczba:  #cyfra to str.
    #print(type(cyfra), cyfra)  #sprawdzenie
    int_cyfra = int(cyfra)      #zamienia str'cyfra' na liczbę int
    #print(int_cyfra, type(int_cyfra))
    #print('suma to:',int_cyfra+suma) #pokazuje kolejną sumę cyfr
    suma +=int_cyfra    # suma=suma+int_cyfra

print(suma)
print('*'*30)

# 2 suma cyfr liczby np 1239=1+2+3+9=15=1+5=6 -warunek if sum<10:
# czemu musi być: while???????????????????????????????
liczba=input('Wpisz liczbę: ') #input daje str ale on nie jest iterowalny w pętli for
while True:
    suma=0  #wartośc sumy początkowa

    for cyfra in liczba:  #cyfra to str.
        # print(type(cyfra), cyfra)  #sprawdzenie
        int_cyfra = int(cyfra)      #zamienia str'cyfra' na liczbę int
        #print(int_cyfra, type(int_cyfra))
        #print('suma to:',int_cyfra+suma) #pokazuje kolejną sumę cyfr
        suma +=int_cyfra

    if suma<10: #war. dla kolejnej sumy (suma sumy itd)
        break
    else:
        liczba = str(suma)  #suma staje się ponownie liczbą i powtarza się pętla FOR
                            # (musi być str(suma) bo str jest iterowany w FOR

    print('Podsuma: ',liczba)
print('Suma końcowa: ',suma)
print('*'*30)

# 3suma cyfr liczby np 1239=1+2+3+9=15=1+5=6 -
liczba=input('Wpisz liczbę: ')
while True:
    suma = 0

    for cyfra in liczba:
        # print(cyfra) #printuje 321
        suma=int(cyfra)+suma
    #print(suma)

    if suma>9:      #odwrotny warunek if jak #2
        liczba=str(suma)
    else:
        break
    print('Podsuma: ',liczba)
print('Suma sum: ',suma)
