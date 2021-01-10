# Enkapsulacja
class Computer:
	def __init__(self):
		self.__max_price = 900
	def set_max_price(self, price):
		self.__max_price = price
	@property
	def max_price(self):
		return self.__max_price
	@max_price.setter
	def max_price(self, price):
		self.__max_price = price
c = Computer()
print(c.max_price)
c.max_price = 1200  # use case dla @max_price.setter
print(c.max_price)