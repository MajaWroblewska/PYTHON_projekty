a={1,2,3,4}
b={4,5,6}
c={'a','b','c'}
# print(a[0])
#set is not subscriptable- nie indeksowalny
a.add(5)
print(a)
c.add('w')
print(c)
print(a.intersection(b))
print(b.intersection(a))
print(a.differance(b))
print(b.differance(a))
print(a.symmeric_differance(b))
print(b.symmeric_differance(a))