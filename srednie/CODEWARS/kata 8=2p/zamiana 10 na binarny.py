binar='111101111'
hexar='757'
print(int(hexar,8))   #zamiana na 10 z 8-kowego
print(int(binar,2))   #zamiana na 10 z 2-kowego

liczba=1001
w=bin(5)
a=bin(liczba)[2:]    #->str
b=oct(liczba)[2:]
c=hex(liczba)[2:]

print(a,b,c)