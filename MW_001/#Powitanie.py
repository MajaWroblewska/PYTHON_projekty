# Powitanie imienne

print("Powitanie")
name=input('Podaj imię\n')

def hello(name):
    if not name:
        print( 'Hello, Nieznajomy!')
    else:
        print( f'Hello, {name[0].upper()}{name[1:].lower()}!')

def greet1(name):
    if not name:
        print('Hello, Nieznajomy!')
    else:
        print( f'Hello, {name.capitalize()} how are you doing today?')
    return

def greet2(name):
    if not name:
        print('Hello, Nieznajomy!')
    else:
        print( f'Hello, {name[0].upper()}{name[1:].lower()} how are you doing today?')
    return

hello(name)
greet1(name)
greet2(name)




'''greet.maja
name = input('Jaki serial chcesz obejrzec? ')
print("Serial {} otrzymał ocenę {}".format(name, serials[name]))
'''
