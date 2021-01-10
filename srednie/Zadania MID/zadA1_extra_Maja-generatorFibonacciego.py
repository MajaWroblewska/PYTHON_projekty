'zad 1*'
'Dodaj do funkcji generującej argument n, który ograniczy liczbę generowanych wyrazów ciągu.\
Stwórz generator i użyj go w wyrażeniu list comprehension (typu  [x for x in f] ) by stworzyć listę \
będącą kwadratami pierwszych n wyrazów ciągu Fibonacciego.# zad 1* ciąg fibonaciego.'

def fibonaci2(n):
    a=0
    b=1
    for i in range(n):
        yield a
        c=a+b
        a,b=b,c

for i in fibonaci2(20):
    print(i)

lista_fibonaci2=[x for x in fibonaci2(20)]
print('lista:',lista_fibonaci2)

set_fibonaci2={x for x in fibonaci2(20)}
print('set:', set_fibonaci2)

dict_fibonaci2={x:y for x in fibonaci2(20)}
print('dict:',dict_fibonaci2)
