import timeit

setup ='from math import sqrt'

code = '''
def fun():
    [sqrt(x) for x in range(100)]
        '''

print('sqrt:',timeit.timeit(stmt=code, setup=setup))


print('join:',timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
# 0.8187260627746582

print("-".join(str(n) for n in range(100)))

slowo='ab cd ef re'
print('*'.join(slowo))
a=slowo.split() # zamienia srt -> [] \ 'ab cd ef    re'->['ab', 'cd', 'ef', 're']
print(a)
b='++'.join(a)
print(b)
