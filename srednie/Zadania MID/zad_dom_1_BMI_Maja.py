'Bonusowe zadanie dla chętnych - zabawa z dataclass:\
1-Należy stworzyć klasę (na bazie dataclass oczywiscie) osoby, ktora bedzie posiadac 3 pola \
odzwierciedlające następujace wartości (zachęcam oczywiscie do anglojęzycznych nazw):\
 :masa ciala, wzrost, indeks BMI. \
Masa ciała i wzrost mają byc przekazane w konstruktorze, a indeks BMI musi być polem obliczonym. \
(tip: metoda magiczna __post_init__)\
2-Potem należy stworzyć klasę sportowca (dziedziczmy!), która zawiera dodatkowe pole: płeć. \
 I w zależności od tego, czy osoba jest mężczyzną, czy kobietą, współczynnik BMI powinien być mnożony przez odpowiednio:\
 0.7 lub 0.8 (wiem wiem, duze uproszczenie :slightly_smiling_face: )\
3-Obiekty powinny byc porownywalne na bazie indeksu BMI, \
tzn. jeśli mateusz i andrzej są instancjami klas z punktów 1 i/lub 2, \
to powinno być możliwe porównanie mateusz > andrzej itp. \
Tip: Obiekty powinny byc callable (wywyoływalny - metoda __call__) i w wyniku wykonania - zwracać wartosc indeksu BMI'

from dataclasses import dataclass, field



@dataclass
class Person:
    weight: int
    height: int
    bmi: float = field(init=False)      #by nie podawać przy wywołaniu a przypisanie domyślnie False

    def __post_init__(self):    #metoda magiczna __post_init__ -> po inicjacji sie wykona
        self.bmi= round(self.weight / (0.01*self.height) ** 2, 2)  #zaokrąglenie do 2 miejsca po przecinku\
                                            # - 0.01  bo zamiana wzrostu z cm -> m

    def __call__(self, *args, **kwargs):    #magiczna metoda __call__ -> do wyołaniu przy inicjacji instancji
        return self.bmi

@dataclass
class Sportsman(Person):
    sex: str = "unknow"

    def __post_init__(self):
        factor=None
        if self.sex == "man":
            factor=0.7
        elif self.sex == 'woman':
            factor=0.8

        super().__post_init__()     # by dziedziczyć pola z Person
        self.bmi = self.bmi if not factor else round(self.bmi * factor, 2)


maja=Person(weight=65,height=172)   #inicjalizacja osoby klasy Person
print('maja-obiekt Person:',maja)   # cały obiekt
print('BMI',maja.bmi)
print('wykonanie metody __call__=bmi', maja())  #to co w call
print("---"*30)

xxx=Person(weight=65,height=172)   #inicjalizacja osoby klasy Person
print('xxx-obiekt Person:',xxx)
print('BMI',xxx.bmi)
print('wykonanie metody __call__=bmi', xxx())
print("---"*30)

luc=Sportsman(weight=65,height=172,) #inicjalizacja os.klasy Sportsman dziedziczona z Person
print('luc-obiekt Sportsman:', luc)
print('BMI',luc.bmi)
print('wykonanie metody __call__=bmi', luc())
print("---"*30)

inga=Sportsman(weight=65,height=172,) #inicjalizacja os.klasy Sportsman dziedziczona z Person
print('inga-obiekt Sportsman:', inga)
print('BMI',inga.bmi)
print('wykonanie metody __call__=bmi', inga())
print("---"*30)

jaga=Sportsman(weight=65,height=172,sex='woman') #inicjalizacja os.klasy Sportsman dziedziczona z Person
print('jaga-obiekt Sportsman:', jaga)
print('BMI',jaga.bmi)
print('wykonanie metody __call__=bmi', jaga())
print("---"*30)

hugo=Sportsman(weight=65,height=172,sex='man') #inicjalizacja os.klasy Sportsman dziedziczona z Person
print('hugo-obiekt Sportsman:', hugo)
print('BMI',hugo.bmi)
print('wykonanie metody __call__=bmi', hugo())
print("---"*30)

print('luc==inga:', luc==inga)  # bo oba sa Sportsman
print('maja==luc:', maja==luc)  # bo sa różnych klass
print('maja==xxx:', maja==xxx)  # bo oba sa Person
print('inga==hugo:', inga==hugo)    # bo mają różne BMI mino że sa tych samych klass

