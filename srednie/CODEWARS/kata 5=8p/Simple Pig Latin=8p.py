'''
Przenieś pierwszą literę każdego słowa na jego koniec, a następnie dodaj „ay” na końcu słowa.
Pozostaw znaki interpunkcyjne nietknięte.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    word_list=text.split()
    # print(word_list)
    alpha_list=[wordx[1:]+wordx[0]+'ay' for wordx in word_list if wordx.isalpha()]
    space_list=[x for x in word_list if not x.isalpha()]
    # print(alpha_list)
    # print(space_list)
    new=alpha_list+space_list
    # print(new)
    return ' '.join(new)
##########################################################################
def pig_it(text):   #maja wzrujac sie na poniżej
    word_list=text.split()
    new_list=[word[1:]+word[0]+'ay' if word.isalpha() else word for word in word_list]
    return ' '.join(new_list)
##########################################################################
def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
####################################################################################33
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
################################################################################3
def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)
###############################################################################
import re   #Regex !!!!!!!!!!!!!!!!!!!!!!!!!!!!

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)
############################################################################
import re   # #Regex !!!!!!!!!!!!!!!!!!!!!!!!!!!!
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)
##############################################################
def pig_it(text):       #Kris
    new_txt = ''
    for word in text.split():
        if word.isalpha():
            new_txt += (word[1::] + word[:1] + 'ay' + ' ')
        else:
            new_txt += (word[1::] + word[:1] + ' ') #????
    return new_txt[:-1]

# print(pig_it('Pig latin is cool'))  #,'igPay atinlay siay oolcay')
# print(pig_it('This is my string'))  #,'hisTay siay ymay tringsay')
print(pig_it('This is : / my , string . ?'))  #,'hisTay siay ymay tringsay')