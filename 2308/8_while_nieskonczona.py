'''i=0
while i<10:
    print('działam')
    i+=1
'''
liczby=[]
while True:
    liczba=input('podaj liczbe:')

    if liczba=='end':
        break
    else:
        liczby.append(float(liczba)) #float lub int też

