import string
# def is_pangram(napis):
#     return len(set(string.ascii_lowercase).intersection(napis.lower())) == len(string.ascii_lowercase)
alfabet = string.ascii_lowercase
pangram = input("Wpisz zdanie. Sprawdź czy jest ono ang.PANGRAMEM ")
set_alfabet = set(alfabet)
set_pangram = set(pangram.lower())
# print(set_alfabet)
# print(set_pangram)
diff_al_pan = set_alfabet.difference(set_pangram)  #różnica alfabet-pangram
diff_pan_al = set_pangram.difference(set_alfabet)   # róznica (pangram-alfabet)-zawsze zbiór pusty
# print(diff_al_pan)
# print(diff_pan_al)
if diff_al_pan: #niepusty set=True
    print('Nie jest to pangram')
    print('Nie wykożystałeś' ,diff_al_pan)
else: #pusty set, str, tuple=False
    print('Tak to jest pangram.\t BRAWO!')

'''
Pomoc
A(set).intersection(B-set) #część wspólna zbiorów set(A) i set(B)
B(set).intersection(A-set)

A.differance(B)             #różnica logiczna 2 zbiorów set(A) i set(B) = A-B =! B-A

A.symmetric_differance(B)   #różnica symetryczna 2 zbiorów set(A) i set(B) =( A-B and B-A )
'''
