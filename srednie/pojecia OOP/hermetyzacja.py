#ukrywanie pewnych rzeczy

class Computer:
    def __init__(self):
        self.__max_price=900

    def get_max_price(self):
        return self.__max_price
    def set_max_price(self,price):
        self.__max_price=price

    @property #staje się geterem bo jest property-własność
    def max_price(self):
        return self.__max_price

    @max_price.setter
    def max_price(self,price):
        self.__max_price=price
c=Computer()
c.max_price=1200
print(c.max_price)

print(c.max_price)  # do property ukrycie metody  by widziano to jako atrybut bo normalnie wywołanie metory to nazaw()


print(c.get_max_price())
c.set_max_price(1200)   #dostanie się do zastrzeżaonej pola przez
print(c.get_max_price())



# print(c.Computer.__max_price)
# print(dir(c))
# c.max_price=1200

# print(c.__max_price)


