def fun1():
    a=1
    b=2
    return a,b

def fun2():
    a=1
    b=2
    return [a,b]

def fun3():
    a=1
    b=2
    return {a,b }

def fun4():
    a=1
    b=2
    return {a:'x',b:'y'}

print(fun1())
print(fun2())
print(fun3())
print(fun4())

