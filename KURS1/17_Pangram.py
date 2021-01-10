'''
#1 dokończyć licznik znaki specjalne
# alfabet ręcznie wpisany

import string
alfabet='abcdefghijklmnopqrstuvwxyz'
alfabet_set=set(alfabet)  #zamiana na unikalny set
print('alfabet :\t\t',alfabet_set)

napis=input('czy to pangram? : ')
napis_set=set(napis)   #zamiana na unikalny set
# print(napis_set)   #wypisanie różnych liter

counter=0
for znak in napis_set:
    # print(znak, znak.isalpha())  #czy to litera
    if znak.isalpha():       #zwraza True tylko dla liter,  # w if oraz for musza "==" i znak bo jest w for
        counter+=1
if counter==len(alfabet_set):
    print('TAK')
else:
    print('NIE')
print('Ilość wpisanych różnych liter: ',counter)
print('Wpisane znaki to : ',napis_set)
'''


#2 alfabet angielski wydrukowany 
# f-ce log. zbiorów: A.intersection(B), A.differance(B), A.symmeric_differance(B)
import string
print(string.ascii_lowercase)  #alfabet jako str

alfabet=string.ascii_lowercase
alfabet_set=set(alfabet)
print(alfabet_set)    #alfabet jako set

napis=input('czy to pangram? :')
# napis.lower()   #zmniejszamy znaki w napisie
napis_set=set(napis.lower())   #zamiana na unikalny set oraz zmniejszamy znaki w napisie
print(napis_set)   #set z małymi literami

roznica=alfabet_set.difference(napis_set)  #różnica zbiorów

if len(roznica)==0:
    print('TAK')
else:
    print('NIE')
