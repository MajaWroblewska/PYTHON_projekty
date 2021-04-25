binar='111101111'
hexar='757'
print(int(hexar,8))   #zamiana na 10 z 8-kowego
print(int(binar,2))   #zamiana na 10 z 2-kowego
print(f'liczba 111 binarnie to dziesiętnie {int("111",2)}')   #zamiana na 10 z 2-kowego
print(int('70',8))   #zamiana na 10 z 2-kowego

liczba=1001
w=bin(5)
a=bin(liczba)[2:]    #->str
b=oct(liczba)[2:]
c=hex(liczba)[2:]

print(f'{liczba} binarny-2: {a},\n{liczba} ósemkowo-8 : {b}\n{liczba} hex-16:{c}')