#lista składana wyciąganie cyfr z napisu -
napis=input('Podaj napis: ')
print([znak for znak in napis if znak.isnumeric()])
print('-'*30)

napis=input('Podaj napis: ')
a=[znak for znak in napis if znak.isnumeric()]
print(a)
print('-'*30)

a'refdfdw33r'
b=[int(x)**2 for x in a if x.isdigit()]  # pierwsze x jest ostatecznie wyświetlana
print=(b)

a='refdfdw33r'
b=[1 for x in a if x.isdigit()]  # pierwsze x jest ostatecznie wyświetlana
print(b)

# a='refdfdw33r'   #blad
# b=[x for x in enumerate(a) if x.isdigit()]
# print(b)

a='refdfdw33r'
b=[x for i,x in enumerate(a) if x.isdigit()]  #
print(b)

#?????
a='refdfdw33r'
b=[[index,x] for x in enumerate(a) if x.isdigit()]
print(b)








# lista=[] # list()
# for znak in string:
#     if znak >='0' and znak<='9': #sprawdzenie czy jest numer wg ASCII
#
#         lista.append(znak)  # lista.append(znak)- nie zwraca nic
# print('Cyfry w napisie to:',lista)
#
# print('*'*30)
#
# # wyciągnij cyfry z napisu
# string=input('podaj dowolny napis:')
# lista=[] # list() -deklaracja pusta list
#
# for znak in string:
#     if znak.isnumeric():
#         lista.extend(znak)
# print(lista)