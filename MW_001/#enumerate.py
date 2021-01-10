# wyliczanie składników listy i numerowanie ich

fruits=['apple','orange','pear','banana','apple']

i=0
for fruit in fruits:
    i+=1
    print(i, end='-')    # end='' sprawi ze kolejny print wydrukuje w tej samej linii co ten- nie utworzy kolejnje linii
    print(fruit)

# to samo co wyżej czyli wyliczanie składników listy i numerowanie ich
print('*'*30)
print('start')

for i, fruit in enumerate(fruits): #enumerate wypisuje od 0, tu definiuję 'fruit'
    if i==4:        # przerwanie po wyliczeniu 3 elementu
        break
    # print(i+1,end='-')        # wypisuje nr pozycji składnika w liście "fruits" od i=0+(1) lub\
    # print(fruit)              # linia 18 i 19 muszą być razem!!!!
    print(i + 1, '-', fruit)    # w 1 lini ale większe spacje niż z lini 18 i 19 razem
       # jak dam fruit-S to wypisze całą listę z wszystkimi elementami
print('koniec')


