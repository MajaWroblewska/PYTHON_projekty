# numbers = [6, 9, 3, 1]
# numbers_sorted = sorted(numbers)
# numbers_sorted  #[1, 3, 6, 9]
# numbers #[6, 9, 3, 1]
# numbers.sort()
# numbers #[1, 3, 6, 9]

#zad11-1
'Napisz funkcję sortującą litery w stringu i zwracającą string.'
napis="jakis napis"
print(str(sorted(napis)))

#zad11-2
'Napisz funkcję, która posortuje i zwróci listę liczb bez duplikatów.'
lista=[1,25,87,2,0,0,1,99,41]
a=lista.sort()
# print(a) #>>> None
print('posortowana lista=lista.sort():',lista)

b=sorted(lista)
print('b=sorted(list):',b)
c=set(b)
b=list(c)
print('bez duplikatów:',b)
print('szybko bez powtórzeń\nsorted((set(lista))):',sorted(set(lista)))
##########################################################################################

from typing import List #właczenie typownia

def fun1(string: str) ->str:
    return '-'.join(sorted(string))

def fun2(seq:List[int]) ->List[int]:
    return sorted(set(seq), reverse=True)

def fun3(seq:List[int]) : # nie musi być '->List[int]'
    lista_a=list(set(seq))
    lista_a.sort()
    return lista_a

seq=[123,2,20,7,85,2,44]
seq2=('w','e','t','u','a')
string="jakis napis2"
print('fun1:',fun1(string))
print('fun2:',fun2(seq))
print('fun3:',fun3(seq))
print('fun3 na seq2:',fun3(seq2))
