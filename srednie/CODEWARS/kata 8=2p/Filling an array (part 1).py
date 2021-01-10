def arr(n=0):
    return list(range(n))

def arr(n=0):
    return [ x for x in range(n)] if n>0 else []

arr = lambda n=0: list(range(n))

def arr(n=int()): return list(range(int(),n))

arr = lambda n=0: [i for i in range(n)]

arr=lambda a=0:[*range(a)]

def arr(n=0):
    return [x if n != 0 else [] for x in range(n)]

print(arr(5))   #>>[0, 1, 2, 3, 4]
