# def info_arg(*args):
#     print(args)
#     # print(type(args))
#
# info_arg(1)         #
# info_arg(1,2,3)       #zwraza tuple
# info_arg(1,2)
# info_arg()

# Suma dowolnej ilości cyfr
def suma(*dane):            #w *dane są wszystkie wpisane dane do funkcji nie organiczamy sie do ilości deklarowanych zmiennych
    return sum(dane)

print(suma(7,9))
print(suma(1,2))
print(suma())
print(suma(1))
print(suma(1,2,3,4,5,6,7,8,9))
print(suma(1,2,3,4,5,6,7,8,9,10,44,55,87,98))
print('-'*30)
######################################################################
def foo(*imie):
    print(imie)
foo(1,2,3)      #typla
foo('Maja','Iza')
print('-'*30)
#####################################################################
def sumowanie(*dane):
    suma=0
    for i in dane:
        suma=suma+i
    return suma

print(sumowanie(10,2,7))

##################################################################

def sumowanie(dane):        #może być 
    suma=0
    for i in range(dane):
        suma=suma+i
    return suma

print(sumowanie(10))