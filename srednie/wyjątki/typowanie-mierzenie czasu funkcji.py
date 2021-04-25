import timeit

setup ='from math import sqrt'

code = '''
def fun():
    [sqrt(x) for x in range(100)]
        '''

print('sqrt:',timeit.timeit(stmt=code, setup=setup))
##############################

print('join:',timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
# 0.8187260627746582

print("-".join(str(n) for n in range(100)))
##############################

slowo='ab cd ef   re'
print('*'.join(slowo)) #zmienia str -> str z separatorem '*' między znakami
a=slowo.split() # zamienia str -> [] \ 'ab cd ef re'->['ab', 'cd', 'ef', 're']
print(a)
b='++'.join(a) # zmieia [] -> str - łączy el listy na str z łącznikiem '++'
print(b, type(b))

ab=[str(n) for n in range(10)]
ba=[n for n in range(10)]

print(ab)
print(ba)
w='+'.join(ab)
print(w)