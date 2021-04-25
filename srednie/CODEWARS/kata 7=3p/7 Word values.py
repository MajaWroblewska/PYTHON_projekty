def name_value(my_list):    #Maja
    lista=[]

    for i,slowo in enumerate(my_list):
        # print(i+1,slowo)
        suma=0
        for litera in slowo:
            if litera.isalpha():    # czy litera jest bez spacji itp
                wartosc=ord(litera.lower())-96  # wielkość liter nie ważna
                # print(litera,wartosc, type(wartosc))
                suma=suma+wartosc*(i+1)
        lista.append(suma)
    # print(suma)
    return lista
#############################################################################################
def name_value(l):  #Jana       bez dużych liter
    return [sum(ord(k)-96 for k in j if k.isalpha())*(i+1) for i,j in enumerate(l)]
###################################################################################################
# def nameValue(myList):
#     return [ i*sum(map(lambda c: [0, ord(c)-96][c.isalpha()], w.lower())) for i,w in enumerate(myList,1)]
# ###############################################################################################################
# def name_value(my_list):
#     import string
#     return [(idx + 1) * sum(string.ascii_lowercase.index(x.lower()) + 1 for x in value if x is not ' ') for idx, value in enumerate(my_list)]
# ##################################################################################################
# def name_value(s):  #nie dla dużych liter
#     return [sum(ord(c) - 96 for c in s[i] if c != ' ') * (i + 1) for i in range(0,len(s))]
#
# ###############################################################################################################
# def name_value(my_list):    #?? chyba bez dyżych liter
#     l = []
#     d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
#          'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
#
#     for i in range(len(my_list)):
#         l.append(sum([d[j] for j in my_list[i] if j in d]) * (i+1))
#     return l
# #######################################################################################
# def name_value(my_list):    # bez dyżych liter
#     return [sum(ord(ch) - 96 for ch in word if ch != ' ') * i for i,word in enumerate(my_list, 1)]
# #####################################################################################################
# # bez dyżych liter
# name_value = lambda l: [(i + 1) * sum([(1 + 'abcdefghijklmnopqrstuvwxyz'.index(c) if c in 'abcdefghijklmnopqrstuvwxyz' else 0) for c in list(l[i])]) for i in range(len(l))]

##################################################################################
import string   #KubaZ bez dużych liter

def w_litery(alph):
    if alph not in string.ascii_lowercase:
        return 0
    else:
        for j, x in enumerate(string.ascii_lowercase):
            if x == alph:
                return (j + 1)


def name_value(my_list):
    a = 0
    b = 0
    wartosci = []

    for i, x in enumerate(my_list):
        for a in x:
            b = b + w_litery(a)
        wartosci.append(b * (i + 1))
        b = 0
    return wartosci


print(name_value(["abc","abc","abc","abc"]))    #,[6,12,18,24])
print(name_value(["codewars","abc","xyz"])) #,[88,12,225])
print(name_value(["codewars"])) #,[88])
print(name_value(["a",' ','A'])) #,[1,0,3])


# for i in range(65, 91):
#     litera = chr(i)
#     print(litera)
# print(chr(97))
# print(ord('a')-96)
# print(ord('z')-96)
# print(ord('b')-96)
##################################################################

import string
# my_list=["abc","abc","abc","abc"]
my_list=["codewars","abc","xyz"]

# def name_value(my_list):
#     lista=[]
#     slownik_liter = {}
#     for i,litera in enumerate(string.ascii_lowercase):
#         slownik_liter[litera]=i+1  #zamiana litery z jej indeksem
#
#     suma = 0
#     for i, slowo in enumerate(my_list):  # wypisanie wartosci dla my_list wpisanego
#         for znak in slowo:
#             if znak.isalpha():  # czy znak w my_list jest literą
#                 suma = suma + slownik_liter[znak]
#         lista.append(suma)
#
#     # return suma
#     print(slownik_liter)
#     return  suma, lista
#
# print(name_value(my_list))
#
# def suma_slowa():
#     suma=0
#     for i,znak in enumerate(my_list): #wypisanie wartosci dla my_list wpisanego
#         # print(k[znak])
#         if znak.isalpha(): #czy znak w my_list jest literą
#             suma=suma+k[znak]
#         else:
#             continue
#     return suma