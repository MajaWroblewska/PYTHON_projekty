slownik={'a':1,'b':2,'c':3}
for i in slownik:
    print(i)
print(slownik)
print(slownik.items())

print('*'*30)
#
s={'a':1}
print(s['b']) #keyError - brak klucza w słowniku

s={1:'a','b':2}
print(s)


