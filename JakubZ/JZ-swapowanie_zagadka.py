def fun():
    a=1
    b=2
    return a, b

c,d = fun()
print(c)
print(d)
print('\n')


def fun1():
    a=1
    b=2
    return [a, b]

c,d = fun1()
print(c)
print(d)
print('\n')


def fun2():         #set może byc niestabilny i zwrocic wartosci nie tak jak trzeba
    a=1
    b=2
    return {a, b}

c,d = fun2()
print(c)
print(d)
print('\n')


def fun3():         # slownik zwroci tylko klucze, wartosic klucza zostana utracone
    a=1
    b=2
    return {a: 'x', b: 'y'}

c,d = fun3()
print(c)
print(d)
print('\n')