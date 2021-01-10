#1 zliczanie ilości liter a
napis=input("Napisz coś a policzę ile jest znaków a/A:")
napis.lower()
znak= 'a'
counter=0
for znak in napis.lower():
    #print(znakA)
    if znak== 'a':
        # print('Mam A')
        counter += 1
print('Znak a lub A w napisie', napis, ' występuje: ', counter)


#2 zliczanie ilości dowolnego znaku (+ wielka = mała litera)
napis=input("Podaj napis:")
# print(a.lower())
litera=input('Podaj znak jaki mam policzyć w Twoim napisie:')
# print(litera)    #litera jest str
counter=0
for znak in napis.lower():
    #print(znakA)
    if znak==litera:
        counter += 1
print('Znak ', litera, ' występuje: ', counter)


#3 wypisz wszystkie litery w napisie i ilość ich występowania
napis= 'MajaWroblewska'
napis=napis.lower() #zamiana napisu na małe litery ->(duże to: a.upper() )

napis_set=set(napis)    #zamiana str na unikalny set
print(napis_set)

for znak in napis_set:
    ile=napis.count(znak)
    print(znak,'-',ile)

print('*'*40)

