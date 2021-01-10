napis3= 'Ciaskto czekoladowe'
napis4= "babeczka z kremem "
print(len(napis3))
print(len(napis4))

print("*"*20)
print(len(napis3 + napis4)) #długość napisów

print(len(napis3) + len(napis4))

print("*"*20)
print(napis3[0]) #wypisanie kolejnych znaków napisu
print(napis3[1])
print(napis4[-1])
print(napis4[-2])
#print(napis2[-10])  # wymuszenie nieistniejącego znaku - IndexError: string index out of range

print("*"*20)
napis3 = napis3[0] + 'w' + napis3[2:] #zamiana litery i->w
print(napis3)
print(napis3.replace("i","w"))  #zamina i na W

print("*"*20)
print(napis3[1:4])  #od 2litery do 4
print(napis3[4:10]) #od 5litery do 10litery

print("*"*20)
print(napis4)
print(napis4[1:]) #zwraca od pos 1 do końca

print(napis4[:10]) #zwraca od początku do pos 10

print("*"*20)
print('zwaca od początku bez 2 ostatnich:\n',napis4[:-2]) #zwaca od początku bez 2 ostatnich
print(napis4[-15:]) #zwaca od końca 15 ostatnich znaków i spacji i \n

print("*"*20)

napis3= "Ala"
napis4= "wróblewska"
print(napis3 + " " + napis4) # sklejenie napisów
print(len(napis3)) # długość napisu
print(len(napis4))
print(len(napis3) + len(napis4))

txt="hello"
print(txt[0],txt[1],txt[2]+txt[3]) # poszczególne litery w txt
print(txt[-1])      # osatnia litera txt

print(napis4)
print(len(napis4))
print(napis4[1:])   # od 2znaku do końca
print(napis4[1:4])  # od 2 do 4 znaku włącznie!!!
print(napis4[:8])   #od początku 8 znaków
print(napis4[:-2])  # od początku do 2 od końca
print(napis4[-2:])  # od końca ostatnie 2 znaki
print(napis4[-5:-2])   #od kończa od 5-2 znaki

'''print(napis2)                # w spak ?????
i=len(napis2)
print(i)
for litera in napis2:
    if i=10:
        print(litera[i])
    i=i-1
    print(i)'''

print("--".join("abrakadabra hokus pokus")) #łączenie wysazu wg. separatora "--"(konkatenacja) wyrazów w napisie seq
                                            # w jeden napis, według separatora/stringu na jakim wywołujemy metodę

import string  #inportowanie metod stringu
print(string.ascii_lowercase)    #alfabet małymi literami (string.ascii_uppercase -
print(string.ascii_uppercase)
