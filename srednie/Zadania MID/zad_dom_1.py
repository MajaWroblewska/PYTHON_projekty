# # 10.1
# sequence = [1, 5, 10, 123]
# mapped = filter(lambda x: x % 5 == 0, sequence)
# print(list(mapped))
#
# # 10.2
# sequence = [(1,2), (2,3), (5,5), (12,0)]
# filtered_seqence = filter(lambda x: (x[0] * x[1]) % 5 == 0, sequence)
# a = map(sum, filtered_seqence)
# print(list(a))
#
# # 10.3
# sl = {'imie': 'Mateusz', 'nazwisko': 'Gorski'}
# sl = [(k, v) for k, v in sl.items()]
# print(list(map(lambda x: f'{x[0].upper()}_{x[1].lower()}', sl)))
#
# # 10.4
# from functools import reduce
# sequence = [11, 3, 8, 7, 5, 4, 3, 11, 1]
# print(reduce(lambda x, y: x + (y if y > 10 else 0), sequence))
# # palindromy
# slowa = ["inni", "kajak", "raDar", "mama"]
# result = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), slowa))
# print(result)


from dataclasses import dataclass, field

@dataclass
class Person:
    weight: int
    height: int
    bmi: float = field(init=False)  #by nie podawać przy wywołaniu a przypisanie domyślnie False

    def __post_init__(self):
        self.bmi = round(self.weight / (0.01 * self.height) ** 2, 1)

    def __call__(self, *args, **kwargs):
        return self.bmi

@dataclass
class Sportsman(Person):
    sex: str = 'unknown'

    def __post_init__(self):
        factor = None
        if self.sex == 'male':
            factor = 0.7
        elif self.sex == 'female':
            factor = 0.8

        super().__post_init__()
        self.bmi = self.bmi if not factor else round(self.bmi * factor, 1)

mateusz = Sportsman(weight=90, height=180, sex='male')  # inicjalizacja
print(mateusz)
mateusz()  # wywołanie -  metoda __call__
print(mateusz())  # wywołanie -  metoda __call__
