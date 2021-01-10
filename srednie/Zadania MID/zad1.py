'Zad 1 - \
Napisz funkcję, która zwraca sumę, różnicę, średnią i iloczyn dwóch liczb. /'
'Rozpakuj zwróconą wartość i wypisz na ekran sumę i różnicę.'
#brake coninue

def fun(num1:int,num2:int) -> tuple:
    return num1+num2, num1-num2, 0.5*(num1+num2), num1*num2

suma, roznica, srednia, iloczyn= fun(15,8)
print('operacje na liczbach 15 i 8: \nsuma:',suma,'\nróżnica:', roznica,'\nśrednia:',srednia,'\niloczyn:',iloczyn)
print("*"*30)

a,b,_,_ = fun(15,8) #__nieistotne poszczególne dane i przypisanie w locie
print('suma i róznica:',a,b)
print('nieistotne 2 wartość jako "_" i "_" (losowa?):', _,_)
print("*"*30)

a,b,*_ =fun(15,8)   #*_ nieistotne wiele danych(*=argsy) i przypisanie w locie
print('suma i róznica',a,b)
print('nieistotne wiele danych *_=args(jako lista):',_)
print("*"*30)

'przypisanie zmiennych w locie'

name, surname, age =("Jan", "Kowalewski",23)
print(f'Hi {name}')
print(f' Nazwisko: {surname} \n Wiek: {age}')
print("*"*30)

###########################################################################
import numpy

a=numpy.array([1,2,3])
print('tablica numpy.array:',a)
print("*"*30)





