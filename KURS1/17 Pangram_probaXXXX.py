# czy w str są wszystkiee litery alfabetu wielkośc nie ma znaczenia
import string

napis=input('Podaj napis a ja sprawdzę czy jest on PANGRAMEM-zaiera wszystkie litery alfabetu ')
# alfabet=set(string.ascii_lowercase)    #zamiana na set
# alfabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alfabet = string.ascii_lowercase
# alfabet=('abcdefghijklmnopqrstuvwxyz')
print(len(alfabet),alfabet)
alfabet_set=set(alfabet)

for litera in napis :
    if litera not in alfabet.lower():
        print('Twój napis  jest PANGRAMEM')
    else:
        print('To jest nie PANGRAM')



'''1
import string 
  
alphabet = set(string.ascii_lowercase) 
  
def ispangram(string): 
    return set(string.lower()) >= alphabet 

'''

'''2
import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True'''

