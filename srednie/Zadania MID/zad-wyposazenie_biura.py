
from dataclasses import dataclass
from itertools import count

COMPANY_EQUIPMENT = {
    'PC': [],
    'monitor': [],
    'keyboard': [],
    'docking station': [],
}
@dataclass
class Employee:
    name: str
    surname: str
    is_staff: bool = False
    equipment: list = None
    _ids=count(0)

    # def __init__(self,name, surname,is_staff, equipment): #bez tego też działa bo jest: @dataclass
    #     self.name=name
    #     self.surname=surname
    #     self.is_staff=is_staff
    #     self.equipment=equipment
    #     self.id=next(self._ids)

    def print_name(self):
        print(self.name)

    def equipment_generator(self):
        if self.is_staff and self.equipment:
            for item in self.equipment:
                if item in COMPANY_EQUIPMENT.keys():
                    COMPANY_EQUIPMENT[item].append(f'{self.name} {self.surname}')
                # else:
                # 	COMPANY_EQUIPMENT[item] = [f'{self.name} {self.surname}']   #dodaje nowy element do COMPANY_EQUIPMENT na "car"
                yield item
        else:
                yield 'This person is not employed or has no equipment'

mateusz = Employee(
    name='Mateusz',
    surname='G',
    is_staff=True,
    equipment=['monitor', 'PC', 'car'],
)
grzes = Employee(
    name='Grzes',
    surname='A',
    is_staff=True,
    equipment=['PC'],
)
maja = Employee(
    name='Maja',
    surname= 'Wrob',
    is_staff= False,
    # equipment=['PC','docking station']
)
employees = [mateusz, grzes,maja]
for employee in employees:
    gen = employee.equipment_generator()
    for _ in gen:
        pass
print(COMPANY_EQUIPMENT)
print(maja)
# print((Employee._ids))
# print(Employee.print_name(grzes))