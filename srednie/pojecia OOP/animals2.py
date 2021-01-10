from AAAabc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self,weight):
        self.weight=weight

    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass

    def live(self): #nie abstrakcyjna klasa łaćy wywołanie metod abstrakcyjnych
        self.move()
        self.make_sound()

class Dog(Animal):
    paw_num=4

    @staticmethod
    def _bark():    #self bo mamy dostęp do pół self a gdy nic metoda nie robi to mozna pominąć self
        print("how how")
    @staticmethod
    def make_sound():   #wymusza stworzeie metody tej samej co w klasie abstrakcyjnej Animal(ABC)
        Dog._bark() #self._bark =Dog(nazwa klasy)._bark
    def move(self):
        if self.weight>30:
            print("człapie")
        else:
            print('Bieg')

    @classmethod
    def print_paw_num(cls):
        print(cls.paw_num)

dog=Dog(50)
dog.make_sound()
dog._bark()
dog.live()
dog.print_paw_num() #classmethod
Dog.print_paw_num() #wywołanie prez nazwę klasy




class Cat(Animal):
    def _bark(self):    #self bo mamy dostęp do pół self a gdy nic metoda nie robi to mozna pominąć self
        print("how how")

    def make_sound(self):   #wymusza stworzeie metody tej samej co w klasie abstrakcyjnej Animal(ABC)
        self._bark()
    def move(self):
        print('idę')


