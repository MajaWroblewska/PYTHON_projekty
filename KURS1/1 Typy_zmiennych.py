# zad1 typy zmiennych i narzucanie typy
print("Hello world")
counter=100     #integer
miles=1000.5    #float
name="John"     #string

print('\n',counter,'\n',miles,'\n',name)
print(counter,miles,name)
print(counter, type(counter),miles, type(miles), name, type(name))

print('\n',counter,type(counter),'\n',miles,type(miles),'\n', name,type(name),'\n')

#narzucanie typów zmiennych
numer=int('234')
print(numer, type(numer))
miles=int(1000.9)   # int obcina wszystko po przecinku- NIE ZAOKRĄGLA!!!!
print(miles, type(miles),' -int obcina wszystko po przecinku- NIE ZAOKRĄGLA!!!!')

print('*'*30)
#wpisanie wielu zmiennych jednokrotnie
a,b,c=100,1000.5,'John'
print(a,b,c)

#narzucanie typów
print('*'*30)
numer = int('234')
print(numer,type(numer))

# Zad 3
print('*'*30)
a=float(input('Podaj liczbe:'))
print(a)
print('Twoja liczba ma typ:',type(a))