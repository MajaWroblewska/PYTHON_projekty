# Lista operacje

w=['napis', [1,2,3],True,None, 9] #elementy różnego typu
print('LISTA "w": ',w)
print('0 element listy: ', w[0])
print('1 element listy: ', w[1])
print('2 element listy: ', w[2])
print('3 element listy: ', w[3])

print('*'*30)
lista=[0,1,2,3,4,5,6,7,8,9]
a=lista
print('a:\t  ',a)
print('lista:',lista)
print('Całą lista:',a[:])
print('2-4 Element listy:',a[1:4]) #2-4element
print('co 2el w liście:',a[::2])
print('Wspak:',a[::-1])

print('*'*30)
a = [66.25, 333, 333, 1, 1234.5]
print(a)
print (a.count(333), a.count(66.25), a.count('x')) #wskazanie nr elementu listy o wskazanej wartości (liczy od 1)
# 2 1 0
a.append(777) #dadanie na końcy listy
print(a)
a.extend(888)
print(a)
a[len(a):] = [L]
print(a)
