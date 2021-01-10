import pytest

# pytest.

a=[1,'a',2,'b']
print(a[::2])
print([1,2].extend([3,4]))
w=[1,2]+[3,4]
print(w)

def nazwa(x):
    return x**2
print(nazwa(5))

abc = lambda x: x**2

print(abc(5))