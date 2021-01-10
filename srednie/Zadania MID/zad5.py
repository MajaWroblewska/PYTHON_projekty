'zad5 \
Przygotuj słownik  prepared_dict , który pozwoli wywołać funkcję za pomocą polecenia print_greeting(**prepared_dict)'

def print_greeting(name, surname, age,kolejka ):
    print(f"Hi {name} {surname}. You are {age} years old. Jesteś {kolejka} w kolejce.")

prepared_dict = {'name':'Maja', 'surname':'Wroblewska', 'age':83, 'kolejka':5} #mój słownik
print_greeting(name='Mateusz',age=33, surname='War', kolejka=88)    #wyw.funkcji z nazwaniem(przypisaniem) zmiennych- dowolna kolejność
print_greeting('Lukasz','Opat', 55,0) #wyw. funkcji z pokolei zmiennymi- wazna kolejność
print_greeting(**prepared_dict) #wywołanie z gotowego słownika musi byc 3 elementowy słownik bo wej funkcja bierze 3 argumenty
print("*"*30)

'Rozpakowywanie w wywołaniu funkcji'

def get_next_person_from_database():
    return "Jan", "Kowalski", 23    # to jest tuple

def print_greeting(name, surname, age):
    print(f"Hi {name} {surname}. You are {age} years old.")

person = get_next_person_from_database()
print_greeting(*person)  #oooooo!
print("*"*30)

'Z pomocą przychodzi operator *. Wszystkie obiekty, które dadzą się rozpakować do dokładnie trzech elementów \
prawidłowo wywołają funkcję print_greeting.\
Aby rozpakować słownik, należy użyć operatora **. Klucze w słowniku muszą odpowiadać nazwom argumentów funkcji.'
##################################################################################################################

'Rozpakowywanie argumentów funkcji \
Czasami nie wiemy ile argumentów ma przyjąć funkcja lub chcemy zapewnić elastyczność i \
możliwość wywoływania z dowolną liczbą parametrów. Deﬁnicja funkcji może składać się \
argumentów POZYCYJNYCH i NAZWANYCH. Przyjęło się, żeby nazywać je *args i **kwargs.'

def fun_args(*args):
    # ta funkcja pozwoli na przyjęcie dowolnej liczby parametrów pozycyjnych
    print('*args=',args)

def fun_kwargs(**kwargs):
    # ta funkcja pozwoli na przyjęcie dowolnej liczby parametrów nazwanych
    print('**kwargs=',kwargs)

def fun_kwargs2(arg1,*args, kwarg1="Default value", **kwargs):
    # możemy mieszać rodzaje argumentów, jednak kolejność jest ważna
    print('arg1=',arg1)
    print('*args=',args)
    print('kwasrg1=',kwarg1)
    print('**kwargs=',kwargs)

fun_args(2,5,8)
fun_kwargs(z=3,x=6,c=9)
print("*"*30)

fun_kwargs2(2,5,8,kwarg1=[2,5,9], g=6,a=3)    #kolejność wywołania jest ważna
print("*"*30)





