'zad 7 \
Przygotuj funkcję wypisującą dane skazańca wg schematu: \
    Imię Nazwisko \
    Czy jest aresztowany? (domyślnie True) \
    Cecha: wartość \
    Cecha: wartość \
    Cecha: wartość \
    (dowolna ilość nazwanych cech)'

def skazaniec(name, surname, arrested=True, **other):
    print(f'Imię i nazwisko: {name} {surname}')
    print(f'Aresztowany: {arrested}')
    for key, value in other.items():   # bo argument f-cji "**other" to słownik wieć iterowanie po słowniku
        print(f'{key}:{value}')

skazaniec('Maja','Wroblewska', age=55, arrested=False, waga=88)
print("*"*30)
skazaniec(surname='Kot', name='Adam',wzrost=180, wiek=38)
print("*"*30)
skazaniec(name='Luc', age=55, surname='Bolek', hight=180, arrested=False)
print("*"*30)
#####################################################


#zad iteracja prze z słowniki

prepared_dict = {
    'name':'Majusia',
    'surname':'Wrobelek',
    'age':83,
                }
for key, value in prepared_dict.items():
    print(f'{key} : {value}')


