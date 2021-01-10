# print([i for i in range(10) if i % 2])
import self as self

shop=[('eggs',6), ('spam',3),('coke',2),('bread',7)]
# print({k:v for k, v in shop if 'e'in k})

items=['eggs','spam', 'sausage', 'carrots']
q=[5,2,1]
# print(list(zip(items,q)))

def is_palindrom(word):
    return word==word[::-1]

# print(is_palindrom('na na'))

class Emplayee:
    rais_amount=1.04

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def rais_salary(self):
        self.salary=int(self.salary*self.rais_amount)

emp_1=Emplayee('Jan', 50000)
emp_2=Emplayee('Ola', 50000)

# print(emp_1.rais_amount)
# print(emp_2.rais_amount)

Emplayee.rais_amount=1.0
# print(emp_1.rais_amount)
# print(emp_2.rais_amount)

emp_2.rais_amount=1.1
# print(emp_1.rais_amount)
# print(emp_2.rais_amount)

emp_1.rais_salary()
emp_2.rais_salary()

# print(emp_1.salary, emp_2.salary)

class A:
    def __init__(self):
        print("A sssss")
class B(A):
    def __init__(self):
        super().__init__()
        print("B zzzzzz")
b=B()

import abc
import math

class Shape(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self):
        pass

class Rectangule(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        return self.side_a * self.side_b

class Square(Rectangule):
    def __init__(self, side):
        super().__init__(side,side)

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def calculate_area(self):
        return self.radius * math.pi

shapes= [Rectangule(2,4), Square(3), Circle(4)]
for shape in shapes:
    print(shape.calculate_area())






