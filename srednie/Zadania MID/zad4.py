
'Swap trick \
W Pythonie korzystając ze składni rozpakowywania można zastosować dość unikatową konstrukcję, \
by zamienić aktualne wartości zmiennych:'

a = 1
b = 5
print('a=',a,'b=',b)
a, b = b, a
print('a=',a,'b=',b)

print("*"*30)

'Rozpakowywanie w wywołaniu funkcji'

def get_next_person_from_database():
    # db stuff...
    return "Jan", "Kowalski", 23    # tuple

def print_greeting(name, surname, age):
    print(f"Hi {name} {surname}. You are {age} years old.")

person = get_next_person_from_database()
print_greeting(*person)  #oooooo!
print("*"*30)

'Z pomocą przychodzi operator *. Wszystkie obiekty, które dadzą się rozpakować do dokładnie trzech elementów \
prawidłowo wywołają funkcję print_greeting.\
Aby rozpakować słownik, należy użyć operatora **. Klucze w słowniku muszą odpowiadać nazwom argumentów funkcji.'

'4zad \
Użyj funkcji range by wygenerować listę 10 elementów. Napisz funkcję, która przyjmuje 10 elementów \
i zwraca ich sumę oraz różnicę. Użyj rozpakowywania w wywołaniu funkcji, aby przekazać 10 parametrów.'

#zad 4
a=[*range(10)]
print('lista 10-elementowa range(10):',a)

b=[a for a in range(10)]
print('lista 10-elementowa comprehensions:',b)  #a=b ta sam lista

c=[2,5,90]
print('lista c:',c)

def fun(*args):
    return sum(args), sum(-i for i in args)

print('suma i róznica range(10):',fun(*a))  #wywołanie "fun()" przez print
print('fun(1,25,55):',fun(1,25,55))     #wywołanie  przypisaniem

print("*"*30)

############################################################################
'prawdziwa różnica metoda "reduce((funkcja),lista))" '
from functools import reduce

d=[2,5,90,]  #suma=97 różnica=93
print('lista d:',d)
a=reduce((lambda x,y: x-y ), d)
print('różńica kolejnych elem. listy d:',a)

def fun2(*args):
    return sum(args), reduce((lambda x,y: x-y ), d)

print('suma i roznica dla fun2(*d):', fun2(*d))
print('fun2(*d):',fun2(*d))      #wywołanie 'fun()' dla dowolnej listy