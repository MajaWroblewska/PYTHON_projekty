# instancja=obiekt

class A(object):
    def func(self):
        print("A")
    def func_from_a(self):
        print("i am in A")

class B(A):
    def func(self):
        print("B")
    def func_from_b(self):
        print("i am in B")

a=A()
b=B()
print(a,'\n',b)  #obiekty
a.func_from_a()
# a.func_from_b()       #nie dziedziczy z B
b.func_from_b()
b.func_from_a()         #bo dziedziczy z A