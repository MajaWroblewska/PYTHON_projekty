import random

class Telefon(object):
    def __init__(self,value1,value2):
        self.data=[value1, value2]
        self.x=value1
        self.y=value2
        self.procesor=value1
        self.kolor='czerwony'
        self.model=random.randint(0,10)
        self.rok_produjcji=2020
    def fun(self):
        print('-'*30)
        return self.x+self.y

my_object_var=Telefon(88,2)
print(my_object_var)
print(type(my_object_var))
a=my_object_var.fun()   #wywołanie przez prypisanie
print(a)
print(my_object_var.kolor)
print(my_object_var.model)




