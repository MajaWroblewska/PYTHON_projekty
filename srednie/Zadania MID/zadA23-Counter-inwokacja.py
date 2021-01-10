'zad23'
import os
from collections import Counter

print('jestem tu:\n',os.getcwd())  #gdzie jesteśmy w kataligu
# os.walk()   #
# os.chdir('zadA26-multiplier.py')#inna ścieżka gdzie będziemy się znajdować


# with open("C:\\Users\\LucWr\\Desktop\\inwokacja.txt",'r', encoding="utf-8") as f:     #plik z pulpitu
with open("inwokacja.txt",'r', encoding="utf-8") as f:      #plik z tego samego pliku co kod
    tekst=f.read().lower()  #str
    words=tekst.split() #lista słów
    print('slowa: ->',words)
    for word in words:
        if word.isalpha():
            licznik=Counter(words)
    print('*',licznik)
    print('---'*30)

    for i,j in licznik.items():
        maks=max(licznik.values())
        if j== maks:
            print(f'Najczęściej użyte słowo to: "{i}" i wystąpiło {maks} razy. ')
    print('---'*30)



    # for i, j in licznik.items():
        # if i.isalpha():
        #     print(licznik.values())
            # print({i:j})
            # print(','.join(i))
            # print(i.split())
            # print(j)

        # lista=[]
        # lista.append(j)
        # print(lista)

        # for slowo in i():
        #     maks2=max(licznik.values())
        #     print(maks2)
############################################################################

    # slownik={',':17,'do':5,'dom':2,'aga':20}
    # print(slownik.items())
    # print(sorted(slownik.items(),key=lambda x: x[1]))
    # # print(s)
############################################################################

    # for i, j in slownik.items():    #wyświetlanie klucza dla wartości w słowniku
    #     if j == 17:
    #         print(i)
#########################################################################

    # print(licznik.values())
    # print(licznik.keys() )
    # print([lambda x : (licznik.keys())])
    # print(licznik.get('do'))
    # print(licznik.get('dom','nosek'))

#########################################################################
    # for i in licznik.values():
    #     wartosci=[]
    #     wartosci.append(i)
    # print(wartosci)

#########################################################################


# a=lambda x,y,z: x*2+y-z
# print(a(x=5,z=7,y=1))
# print(a(5,1,7))
