from dataclasses import dataclass

COMPANY_EQUIPMENT={
    'PC':[],
    'monitor':[],
    'keyboard':[],
    'docking station':[],
}

@dataclass
class Employee:
    name: str
    surname: str
    is_staff: bool = False
    equipment: list = None

    def equipment_generator(self):
        if self.is_staff ==True and self.equipment:
            for i in self.equipment:
                if i in COMPANY_EQUIPMENT.keys():
                    # COMPANY_EQUIPMENT[i].append(''.join({self.name}{self.surname})' #przypisanie Imie do sprzętu
                    COMPANY_EQUIPMENT[i].append(f'{self.name} {self.surname}') #przypisanie Imie do sprzętu
                yield i
        else:
            yield 'Komunikat-osoba nie zatrudniona lub nie ma sprzetu'

#tworzenie konkternych pracowników z danymi
emp1=Employee(name='Maja',surname='Wrob', is_staff=True, equipment=['PC','monitor','car']) # trorzenie pracownika z ekwipunkiem
emp2=Employee(name='Luc',surname='Was', is_staff=True, equipment=['keyboard','monitor'])
# emp3=Employee(name='Wojtek',surname='Mewa', is_staff=True, equipment=['keyboard','docking stasion'])

eq_gen1=emp1.equipment_generator() #wywołanie dzialania f-cji equipment_generator
eq_gen2=emp2.equipment_generator()

employee=[emp2,emp1]
for emp in employee:
    print(emp)

for i in eq_gen1:
    print(i)



print(COMPANY_EQUIPMENT)




