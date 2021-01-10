print('Wyszukanie max 2-ch liczb')

a=float(input('Podaj liczbę a\n'))
b=float(input('Podaj liczbę b\n'))

def wypiszMax(a, b):
    if a > b:
        print(f'{a}, to maksimum')
    elif a == b:
        print (f'{a}, jest równe, {b}')
    else:
        print (f'{b}, to maksimum')
    return
wypiszMax(a, b)

print('*'*30)
print(max(a,b),'to maksimum')

print('*'*30)
print('Maksimum to:',max(13,70,80))