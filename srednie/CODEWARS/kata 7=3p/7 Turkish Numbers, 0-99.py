dictionaty = {
    '0' : 'sıfır',
    '1' : 'bir',
    '2' : 'iki',
    '3' : 'üç',
    '4' : 'dört',
    '5' : 'beş',
    '6' : 'altı',
    '7' : 'yedi',
    '8' : 'sekiz',
    '9' : 'dokuz',
    '10' : 'on',
    '20' : 'yirmi',
    '30' : 'otuz',
    '40' : 'kırk',
    '50' : 'elli',
    '60' : 'altmış',
    '70' : 'yetmiş',
    '80' : 'seksen',
    '90' : 'doksan',
    }


#########################################################
def get_turkish_number(num):    #Maja
    a = num-num%10  #dziesiatki
    b = num%10      #jendostki
    if a!=0 :
        result=f'{dictionaty[str(a)]} {dictionaty[str(b)]}'
    else:
        result=f'{dictionaty[str(b)]}'
    if b==0:
        result=f'{dictionaty[str(a)]}'
    return result
#######################################################################
# def get_turkish_number(num):    #Maja coś nie tak
#     a = num-num%10  #dziesiatki
#     b = num%10      #jendostki
#     a= f'{dictionaty[str(a)]} {dictionaty[str(b)]}' if a!=0 else f'{dictionaty[str(b)]}'
#     b= f'{dictionaty[str(a)]}' if b==0 else f'{dictionaty[str(b)]}'
#     return a , b

#########################################################################
def get_turkish_number(num):    #Jana
    units = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
    tens = ['on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
    if num < 10:
        return units[num % 10]
    if num % 10 == 0:
        return tens[num // 10 - 1]
    return f'{tens[num // 10 - 1]} {units[num % 10]}'
########################################################################################
def get_turkish_number(num):    #ok
    db = 'sıfır bir iki üç dört beş altı yedi sekiz dokuz on yirmi otuz kırk elli altmış yetmiş seksen doksan'.split()
    return f'{num>9 and db[num//10+9] or ""} {num%10>0 and db[num%10] or ""}'.strip() or db[num]

#############################################################################
UNITS = ' bir iki üç dört beş altı yedi sekiz dokuz'.split(' ')
TENS  = ' on yirmi otuz kırk elli altmış yetmiş seksen doksan'.split(' ')

def get_turkish_number(n):
    return f'{ TENS[n//10] } { UNITS[n%10] }'.strip() or 'sıfır'
#########################################################################
turk_dict = {0: 'sıfır', 1: 'bir', 2: 'iki', 3: 'üç', 4: 'dört', 5: 'beş', 6: 'altı', 7: 'yedi', 8: 'sekiz', 9: 'dokuz', 10: 'on', 20: 'yirmi', 30: 'otuz', 40: 'kırk', 50: 'elli', 60: 'altmış', 70: 'yetmiş', 80: 'seksen', 90: 'doksan'}

def get_turkish_number(num):
    if num < 10 or num%10 == 0:
        return turk_dict[num]
    else:
        return f"{turk_dict[(num//10)*10]} {turk_dict[num%10]}"
##########################################################################################
get_turkish_number = lambda n: """\
sıfır;bir;iki;üç;dört;beş;altı;yedi;sekiz;dokuz;on;on bir;on iki;on üç;on \
dört;on beş;on altı;on yedi;on sekiz;on dokuz;yirmi;yirmi bir;yirmi \
iki;yirmi üç;yirmi dört;yirmi beş;yirmi altı;yirmi yedi;yirmi sekiz;yirmi \
dokuz;otuz;otuz bir;otuz iki;otuz üç;otuz dört;otuz beş;otuz altı;otuz \
yedi;otuz sekiz;otuz dokuz;kırk;kırk bir;kırk iki;kırk üç;kırk dört;kırk \
beş;kırk altı;kırk yedi;kırk sekiz;kırk dokuz;elli;elli bir;elli iki;elli \
üç;elli dört;elli beş;elli altı;elli yedi;elli sekiz;elli \
dokuz;altmış;altmış bir;altmış iki;altmış üç;altmış dört;altmış beş;altmış \
altı;altmış yedi;altmış sekiz;altmış dokuz;yetmiş;yetmiş bir;yetmiş \
iki;yetmiş üç;yetmiş dört;yetmiş beş;yetmiş altı;yetmiş yedi;yetmiş \
sekiz;yetmiş dokuz;seksen;seksen bir;seksen iki;seksen üç;seksen dört;seksen \
beş;seksen altı;seksen yedi;seksen sekiz;seksen dokuz;doksan;doksan \
bir;doksan iki;doksan üç;doksan dört;doksan beş;doksan altı;doksan \
yedi;doksan sekiz;doksan dokuz""".split(";")[n]
########################################################################################
def get_turkish_number(n):
    U = ['']+'bir iki üç dört beş altı yedi sekiz dokuz'.split()
    T = ['']+'on yirmi otuz kırk elli altmış yetmiş seksen doksan'.split()
    return f'{T[n//10]} {U[n%10]}'.strip() if n else 'sıfır'
########################################################################################
DIGITS = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
TENS = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

def get_turkish_number(num):
    q, r = divmod(num, 10)
    return "{} {}".format(TENS[q], DIGITS[r]).strip().replace(" sıfır", "")
##########################################################################################
ones = {'j': '', '0': 'sıfır', '1': 'bir', '2': 'iki', '3': 'üç', '4': 'dört', '5': 'beş', '6': 'altı', '7': 'yedi',
        '8': 'sekiz', '9': 'dokuz'}
tens = {'0': '', '1': 'on', '2': 'yirmi', '3': 'otuz', '4': 'kırk', '5': 'elli', '6': 'altmış', '7': 'yetmiş',
        '8': 'seksen', '9': 'doksan'}
import re


def get_turkish_number(num):
    a, b = tuple(str(num).zfill(2))
    return re.sub(' sıfır', '', f'{tens[a]} {ones[b]}'.strip())
#############################################################################################
#########################################################################################

print(get_turkish_number(1))    #, "bir")
print(get_turkish_number(13))   #, "on üç")
print(get_turkish_number(27))   #, "yirmi yedi")
print(get_turkish_number(38))   #, "otuz sekiz")
print(get_turkish_number(77))   #, "yetmiş yedi")
print(get_turkish_number(94))   #, "doksan dört")
print(get_turkish_number(70))   #, "doksan dört")