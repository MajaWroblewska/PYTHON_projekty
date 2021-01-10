import random

'Losowa liczba z przedziału <0.0; 1.0)'
# random.random
a=random.random()
print('losowa liczba od <0.0 do 1.0)=',a)
print("*"*30)

'Losowa liczba całkowita z przedziału <a, b>'
# random.randint(a, b)
b=random.randint(10, 20)
print('losowa liczba od <10 do 20)=',b)
print("*"*30)

'Losowy element kolekcji'
# random.choice(seq)
kolekcja1="asdfghj"
print('kolekcja1=',kolekcja1)
c=random.choice(kolekcja1)
print('losowa liczba z kolekcji1=',c)
print("*"*30)

kolekcja2=[2,8,4,55,9]
print('kolekcja2=',kolekcja2)
c=random.choice(kolekcja2)
print('losowa liczba z kolekcji2=',c)
print("*"*30)
