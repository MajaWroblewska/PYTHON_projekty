def outerFun(a, b):
    def innerFun(c, d):
        return c + d
    return innerFun(a, b)
    return a

result = outerFun(5, 10)
print(result)

def fun1(num):
    return num + 25

fun1(5)
# print(num)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

def display(**kwargs):
    for i in kwargs:
        print(i)
display(a='5', salary=9000)

def fun1 (name, wiek):
    print (name, wiek)
fun1( wiek=23, name='Ki')

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break

print(abs(-45.300))
print(int(2.999))
print(round(100.2563, 3))
print(round(100.000056, 3))
z = complex(1.25,3)
print(z)
print(0b101)
print(0o10)
print(0x1F)

from numbers import Number
from decimal import Decimal
from fractions import Fraction
print(isinstance(2.0, Number))
print(isinstance(Decimal('2.0'), Number))
print(isinstance(Fraction(2, 1), Number))
print(isinstance("2", Number))

import math
print(math.ceil(252.4))
print(math.floor(252.4))
print( (1.1 + 2.2) == 3.3 )
print(1.1+2.2)
print(3.3)
a = 10,1256
print(a)

print("John" > "Jhon")
print("Emma" < "Emm")

str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())
ord ('char')
# print(a)