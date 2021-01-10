def title_case(tytul, minor_words=''):  #Maja
    a=tytul.lower().split()
    b=minor_words.lower().split()
    # print('a=',a)
    # print('b=',b)
    new=[]
    for i in range(len(a)):
        if a[i] in b and i!=0:
            # print('jest',a[i])
            new.append(a[i].lower())
        else:
            # print('nie')
            a[i]=a[i].title()
            new.append(a[i])
            # print(a[i])
    return ' '.join(new)
###############################################################################
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
################################################################################
def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)
###############################################################################
def title_case(title, minor_words=''):
    return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))
###############################################################################
def title_case(title, minor_words="none"):
    title = title.lower()
    lista = title.split()
    minor_words = minor_words.lower()
    words = minor_words.split()
    if title != "":
        lista[0] = lista[0].title()
        for a in lista:
            if a not in words:
                lista[lista.index(a)] = a.title()
                print(lista)

    return ' '.join(lista)
###################################################################################
def title_case(name, words=''):     #Jana
    n = name.lower().split()
    l = [n[1:].index(i)+1 for i in words.lower().split() if i in n[1:]]
    n = [i.title() for i in n]
    for i in l:
        n[i] = n[i].lower()
    return ' '.join(n)
########################################################################################
import string   #Bartek
def title_case(title, minor_words=''):
    if minor_words:
        title_list = title.lower().capitalize().split()
        for index, word in enumerate(title_list):
            if not word.lower() in minor_words.lower().split():
                title_list[index] = word.capitalize()
        return ' '.join([str(word) for word in title_list])
    else:
        return string.capwords(title)
################################################################################



print(title_case('a clash of KINGS', 'a an the of'))    #, 'A Clash of Kings')
print(title_case('THE WIND IN THE WILLOWS', 'The In')) #, 'The Wind in the Willows')
print(title_case('the quick brown fox'))    #, 'The Quick Brown Fox')