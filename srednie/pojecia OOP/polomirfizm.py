'''Bonusowe zadanie dla chętnych - zabawa z dataclass:\
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
Tip: Obiekty powinny byc callable (wywyoływalny - metoda __call__) i w wyniku wykonania - zwracać wartosc indeksu BMI
Zad BMI'''

from dataclasses import dataclass, field

@dataclass
class Person:
    weight: int
    height: int
    bmi: float = field(init=False)      #by nie podawać przy wywołaniu a przypisanie domyślnie False

    def __post_init__(self):    #metoda magiczna __post_init__ -> po inicjacji sie wykona
        self.bmi= round(self.weight / (0.01*self.height) ** 2, 2)  #zaokrąglenie do 2 miejsca po przecinku\
                                            # - 0.01  bo zamiana wzrostu z cm -> m
    def calculate_bmi(self):
        return round(self.weight/((0.01*self.height)**2),2)

@dataclass
class Sportsman(Person):
    sex: str = "unknow"

    def calculate_bmi(self):
        factor=None
        if self.sex == "man":
            factor=0.7
        elif self.sex == 'woman':
            factor=0.8

        super().__post_init__()     # by dziedziczyć pola z Person
        self.bmi = self.bmi if not factor else round(self.bmi * factor, 2)
        return self.bmi


mateusz=Sportsman(weight=95, height=180,sex='man',)
marcin=Person(weight=95, height=180,)
print(mateusz.calculate_bmi())
print(marcin.calculate_bmi())

'''Polimorfizm= metoda "calculate_bmi" jest wywoływana na różnych obiektach róznej klasy-np marcin czy mateusz'''
