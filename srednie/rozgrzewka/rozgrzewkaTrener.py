from dataclasses import dataclass
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
	def equipment_generator(self):
		if self.is_staff and self.equipment:
			for item in self.equipment:
				if item in COMPANY_EQUIPMENT.keys():
					COMPANY_EQUIPMENT[item].append(
						f'{self.name} {self.surname}')
				# else:
				# 	COMPANY_EQUIPMENT[item] = [f'{self.name} {self.surname}']
				yield item
		else:
			yield 'This person is not employed or has no equipment'
mateusz = Employee(
	name='Mateusz',
	surname='g',
	is_staff=True,
	equipment=['monitor', 'PC', 'car'],
)
grzes = Employee(
	name='Grzes',
	surname='A',
	is_staff=True,
	equipment=['PC'],
)
employees = [mateusz, grzes]
for employee in employees:
	gen = employee.equipment_generator()
	for _ in gen:
		pass
print(COMPANY_EQUIPMENT)