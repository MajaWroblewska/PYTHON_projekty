'zad 26\
Napisz funkcję przyjmującą argument n, która będzie zwracała funkcję przyjmującą argument a \
i zwracała tablicę elementów [a, aa, aaa..., n * a]'

def multiplier(n):
    def func(a):
        result=[]
        for i in range(1,n+1):
            result.append(a*i)  #a->str i->int
        print(result)
    return func

make_5=multiplier(5)
make_5('8')

make_6=multiplier(9)('w')


