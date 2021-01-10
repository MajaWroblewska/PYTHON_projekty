'zad1 \
generatory \
Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.'

'lista i gentrator to iterator'

def fibonaci1():     #iteracyjna
    a=0
    b=1
    for i in range(20):     #by iterować w pętli for przy wywołaniu f-cji, lub  while True: - w pętli nieskończonej
        yield a             #by wyświetlał od 1elementu czyli 1elem=0, 2elem=1, 3elem=1elem+2elem
        c=a+b
        a,b = b,c
        # a=b     #a,b==b,a
        # b=c
        # yield c           #wyświetla od 2elem=1


g=fibonaci1()   #wywołanie f-cji generatora przez przypisanie do zmiennej "g"
# print('1elem:',next(g)) #=0 - 1 uruchomienie generatora fibonaci1 przez next(g) ....
# print('2elem:',next(g)) #=1 - 2 uruchomienie generatora fibonaci1 przez next(g) ....
# print('3elem:',next(g)) #=1 - 3 uruchomienie generatora fibonaci1 przez next(g) ....
# print('4elem:',next(g)) #=2
# print('5elem:',next(g)) #=3
# print('6elem:',next(g)) #=5
# print('7elem:',next(g)) #=8
# print('8elem:',next(g)) #=13
# print('9elem:',next(g)) #=21
# print('10elem:',next(g)) #=34
# print('adres genertora:',g)
##############################################
print("*"*30)
##################################
'lub bo nie wyświetla się jednocześnie z powyższym "print("10elem:",next(g))" i z pętlą poniżej'
# for i in g:
#     print(next(g))  #wyswietla co 2 elem generatora

for i in range(1,21):  #musi być range(1,11) bo ogranicza nas ciało f-cji "Fibonaci1" -> for in range(20): ...ta trzeba zmienić
    print(f'{i}elem:',next(g))


'zad 1*'
'Dodaj do funkcji generującej argument n, który ograniczy liczbę generowanych wyrazów ciągu.\
Stwórz generator i użyj go w wyrażeniu list comprehension (typu  [x for x in f] ) by stworzyć listę \
będącą kwadratami pierwszych n wyrazów ciągu Fibonacciego.# zad 1* ciąg fibonaciego.'

def fibonaci2(n):  # iteracyjna
    a = 0   #a,b=0,1
    b = 1
    for _ in range(n):  #i nie ważna zmienna wiec "-"
        yield a     #by wyświetlał sie 1elem=0
        a,b = b, a+b


lista_Fibonaciego=[x for x in fibonaci2(20)]
print(lista_Fibonaciego)





















# def fib_rec(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib_rec(n-1) + fib_rec(n-2)
#
# print(fib_rec(35))
