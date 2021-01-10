'zad1 \
generatory \
Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.'

'lista i gentrator to iterator'

def fibonaci1():
    a=0
    b=1
    for i in range(15):
        yield a
        c=a+b
        a,b=b,c

f=fibonaci1()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

for i in fibonaci1():
    print(next(f))