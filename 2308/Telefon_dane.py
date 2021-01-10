import random, datetime, time

class Telefon(object):
    def __init__(self,value1,value2):
        self.data_produjcji=datetime.datetime.now()
        self.model=random.randint(0,10)

    def wiek(self):
        end=datetime.datetime.now()
        return end

my_object_var=Telefon(88,2)
print(my_object_var)
time.sleep(2)

end=datetime.datetime.now()
a=my_object_var.wiek()   #wywołanie przez prypisanie
print(a)
# print(end-start)
print(my_object_var.data_produjcji-end)

