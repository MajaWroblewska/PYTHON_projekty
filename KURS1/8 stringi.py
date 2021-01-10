# zad 9 stringi

string=input('Podaj napis')
if string==True:
    print('Napis to:',string)
    print('cały napis\t\t\t\t\t\t\t\t:',string[:]) #cały wyraz
    print('napis od 2-3 znak\t\t\t\t\t\t:',string[1:3]) #od 1 do 3 znaku
    print('napis od początku do końca co 2 znak\t:',string[::2]) # od początku do końca co 2 znaki
    print('napis -1 znak od końca:\t\t\t\t\t:',string[-1]) # ostania litera od końca
    print('napis od -8 do -1 znak od końca:\t\t\t\t\t:',string[-8:-1]) # ostania litera od końca
    print('napis -8 znak od końca:\t\t\t\t\t:',string[-3:-1]) # ostania litera od końca
    print(napis, '\n', '*' * 30)

else:
    string='MajaWroblewska'
    print('Napis to:', string)
    print('cały napis to\t\t\t\t\t\t\t:', string[:])  # cały wyraz
    print('napis od 2-3 znak\t\t\t\t\t\t:', string[1:3])  # od 1 do 3 znaku
    print('napis od początku do końca co 2 znak\t:', string[::2])  # od początku do końca co 2 znaki
    print('napis -2 znak od końca:\t\t\t\t\t:', string[-2])  # ostania litera od końca
    print('napis od -8 do -1 znak od końca\t\t\t:', string[-8:-1])  # ostania litera od końca
    print('napis od -3 znak do -1  od końca\t\t:', string[-3:-1])  # ostania litera od końca
    print('wspak:',string[::-1])
    print('*'*30)

napis='To jest {} o wadze {}g i {} kaloriach'.format('CZEKOLADA','100','2580')
print(napis,'\n','*'*30)

txt='Jestem'+' Maja '+'Wroblewska'+' SUPER'+' '+'programista.'
print(txt)
print('*'*30)

print(max(string))  #zwraca literę najdalej od A w napisie w ()
print(min(string))  #zwraca literę najbliżej od A w napisie w ()
print(string)

a='wrocław'
print(a)
print(a[3]) #4znak
print(a[3:]) #4znak do końca
print(a[::2])
print(a[::-2])
print(a[::-1])