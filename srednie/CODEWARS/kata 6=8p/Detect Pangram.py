'''Ignoruj cyfry i znaki interpunkcyjne.
wszystkie litery użyte conajnmiej 1x - mogą być wiele razy'''

import string   #Maja

def is_pangram(sentence):
    alphabet=string.ascii_lowercase
    sentence=sentence.lower()
    if len(set(alphabet).intersection(set(sentence))) == len(set(alphabet)):
        result =True
    else:
        result = False
    print(result)

pangram1 = "The quick, brown fox jumps over the lazy dog!"  #>>True
pangram2 = "The quick, brown fox jumps over the lazy dog123456789 The !" #>>True
pangram3 = "This is not pangram!" #>>False

# is_pangram(pangram1)
# is_pangram(pangram2)
# is_pangram(pangram3)

'''
    Pomoc
    A(set).intersection(B-set) #część wspólna zbiorów set(A) i set(B)
    B(set).intersection(A-set)

    A.differance(B)             #różnica logiczna 2 zbiorów set(A) i set(B) = A-B =! B-A

    A.symmetric_differance(B)   #różnica symetryczna 2 zbiorów set(A) i set(B) =( A-B and B-A )
'''
'''
alphabet=string.ascii_lowercase
print(set(alphabet))
print(len(set(alphabet)))
sentence ="The quick, brown fox jumps over the lazy !"
sentence=sentence.lower()
print(set(sentence))
print(len(sentence))

inter_alf_sent=set(alphabet).intersection(set(sentence))
print(inter_alf_sent)
print(len(inter_alf_sent))

diff_alf_sent=set(alphabet).difference(set(sentence))
print(diff_alf_sent)
'''
#######################################################################################
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())
#####################################################################################
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
#############################################################################
def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False
#############################################################################
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
# issubset -> Zwróć True, jeśli wszystkie elementy zestawu xsą obecne w zestawie y:
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
######################################################################################
import string

def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwhyz'
    for letter in alphabet:
        if letter not in string.lower():
            return False
    return True
#####################################################################################
import string

def is_pangram(s):
    return set(s.lower()) >= set(string.ascii_lowercase)
#########################################################################################
import string
import re

def is_pangram(s):
    return len(set(re.sub( '[^a-z]', '', s.lower() ))) == 26
##############################################################################
import string

def is_pangram(s):
    dict= {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'a':0,'s':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0,}
    s=s.lower()
    for c in s:
        dict[c]=1
    return list(dict.values()).count(0)==0
#######################################################################################
import string                   #!!!!!!!!!!!!!!!!!!!!!!!!

def is_pangram(s):
    t1 = set(s.lower())
    t2 = set(string.ascii_lowercase)
    return (set(t2).issubset(t1))
############################################################################
def is_pangram(s):      #!!!!!!!!!!!!!!!!!!!
    # alp1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alp1=list(string.ascii_lowercase)
    ls=[]
    for i in s.lower():
        if i.isalpha():
            ls.append(i)
    lt=sorted(set(ls))
    if lt==alp1:
        return True
    else:
        return False
##################################################################
def is_pangram(s):   # JANA
    l = []
    for i in set(s.lower()):
        if i.isalpha(): l.append(i)
    return len(l) == 26
######################################################################
import string       #Barbara szama

def is_pangram(s):
    pangram = False
    napis = set([znak for znak in s.lower() if znak>'a' and znak<'z'])
    if len(napis) == 24:
        pangram = True
    else:
        pangram = False
    return pangram
########################################
import string       #Jakub Z


def is_pangram(s):
    a = s.lower()

    litery = set(a)
    b = 0

    for x in litery:
        if x.isalpha():
            b = b + 1
    if b == 26:
        return True
    else:
        return False
###############################################################################
import string       #barosz


def is_pangram(s):
    # zdefiniuj licznik znakow
    num = 0

    # zamien wszystkie litery na male
    lower_s = s.lower()

    # wrzuc je do seta by pozbyc sie powtorzen
    set_lower_s = set(lower_s)

    # utworz set posiadajacy wszystkie znaki alfabetu
    set_ascii = set(string.ascii_lowercase)

    # sprawdz czy znak z pierwszego setu zawiera sie w drugim
    for letter in set_lower_s:
        if letter in set_ascii:
            # jesli tak, dodaj 1 do licznika
            num += 1

    # jesli licznik wskazuje ilosc znakow w alfabecie, zwroc True
    if num == 26:
        return True
    else:
        return False
######################################################################3
import string


def is_pangram(s):
    alphab = [0] * 26

    for char in s:
        low_char = char.lower()
        if 97 <= ord(low_char) <= 122:
            alphab[ord(low_char) - ord('a')] += 1

    if min(alphab) == 0:
        return False
    else:
        return True
###############################################################
import string

def is_pangram(s):
    y = [chr(x) for x in range(ord('a'),ord('z')+1)]
    if(set(y).issubset(set(s.lower()))):
        return True
    else:
        return False
# Metoda chr () zwraca znak (ciąg znaków) z liczby całkowitej (reprezentuje punkt kodu Unicode znaku).
# Metoda chr () zwraca znak (ciąg znaków) z liczby całkowitej (reprezentuje punkt kodu Unicode znaku).
#  ord()funkcja jest odwrotnością funkcji chr () w Pythonie .
##########################################################################################################
def is_pangram(s):
    s = s.lower()
    for x in range(97,123):
        if s.count(chr(x)) == 0:
            return False
    return True
##############################################################################
import string

def is_pangram(s):
    alpha = ''.join(set([i.lower() for i in s if i.isalpha()]))
    return len(alpha) == 26
##################################################################################
import string           #!!!!!!!!!!!!!!!!!

def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    sum_alphabet = list(filter(lambda x: x in s.lower(), alphabet))
    return True if len(sum_alphabet) == 26 else False
#############################################################################
is_pangram=lambda s: set(range(97,123))<set([ord(i) for i in s.lower()])
###############################################################################


print(is_pangram(pangram1))
print(is_pangram(pangram2))
print(is_pangram(pangram3))
