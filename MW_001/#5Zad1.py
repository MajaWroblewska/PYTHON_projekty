'''Zadanie 1 – rozgrzewka
Do zmiennej sentence przypisz zdanie: „Kurs Pythona jest prosty i przyjemny.”, a następnie:

+Policz wszystkie znaki w napisie
Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
+Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):7,12,-4,37
+Wprowadź do zdania 2 błędy ortograficzne 😉'''


'''
#Policz wszystkie znaki w napisie
sentence = "Kurs Pythona jest prosty i przyjemny."
print('Liczba znaków w zdaniu "{}" jest:\n{}'.format(sentence,len(sentence)))
print('Liczba znaków w zdaniu "{}" jest:\n{:,.3f}'.format(sentence,len(sentence)))
print("Liczba znaków w zdaniu ''%s'' jest:\n' %.8d" %(sentence, len(sentence))) #bez przecinka przed % i w "" nie w ''-jak wypisać ""???, %.8d=całkowite 8 znaków
print("Liczba znaków w zdaniu ''%s'' jest:\n' %.4f" %(sentence, len(sentence))) # %.4f to .=dokładność, 4=4miejsca po przecinku, f=float

length = len(sentence)
print(length, "\n")
#print("Aktualnie %d %s kosztuje %.2f zł" % (us, waluta, pln))


#Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?): 7,12,-4,37
print(sentence)
print('znak  o indeksie 7:', sentence[7])
print('znak  o indeksie 12:', sentence[12])
print('znak  o indeksie -4 czyli 4 od końca:', sentence[-4])
print("znak o indeksie 37 nie istnieje. Zdanie ma 37 znaków numerowane od 0 - 36,"
      "ostatni znak to kropka:", sentence[36], "\n")
#print('znak  o indeksie 37:', sentence[37])

#Wprowadź do zdania 2 błędy ortograficzne
print(sentence.replace('u','ó')) #zamiana u-ó
print(sentence.replace('rz','ż')) #zamiana rz-ż

sentence = sentence.replace("u","ó") #zamiana u-ó  i nadpisanie pod zmienną "sentence"
sentence = sentence.replace("rz", "ż") #zamiana rz-ż i nadpisanie pod zmienną "sentence"
sentence=sentence.replace('h','ch')
print(sentence) #wyświetlenie zdania po 2x nadpisaniu
'''
#Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
sentence = "Kurs Pythona jest prosty i przyjemny."
print(sentence)
print("Pkt2 Szukany napis brzmi:",sentence[18:24])

print('Wyraz to:',sentence.split()[3]) #„split” zachowuje się jak lista wyrazów, najprościej tak:
        # czyli dzielisz napis wg (domyślnej) spacji i wybierasz czwarty wyraz (bo liczysz od zera, stąd trójka).

print(sentence.split()) #dzieli string na wyrazy i zapisuje je w tablicy z []
print(sentence.splitlines()) #zapisuje cały string w tablicy z []

a=sentence.find('prosty')
print(a)
c=sentence[a:a+6] #wypisanie kolejnych 6 znaków w zdaniu po znalezieniu "p" w wyrazu "prosty"czyli wypisanie wyrazu "prosty"
print('Szykany wyraz to:\t',c)

