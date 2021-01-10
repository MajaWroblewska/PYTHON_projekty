#wyciąganie cyfr z napisu
string=input('podaj dowolny napis:')
lista=[] # list()
for znak in string:
    if znak >='0' and znak<='9': #sprawdzenie czy jest numer wg ASCII

        lista.append(znak)  # lista.append(znak)- nie zwraca nic
print('Cyfry w napisie to:',lista)

print('*'*30)

# wyciągnij cyfry z napisu
string=input('podaj dowolny napis:')
lista=[] # list() -deklaracja pusta list

for znak in string:
    if znak.isnumeric():
        lista.extend(znak)
print(lista)
