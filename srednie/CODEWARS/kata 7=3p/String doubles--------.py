from itertools import groupby
from typing import List #właczenie typownia
'''
print('Zliczacz = Zliczanie powtórzonych liter')
print('przykładz:   baaaallleee -> ba4l3e3')

def zliczacz(napis: List[str]) ->List[str]:
    kod=[]
    for name, group in groupby(napis):
        gr=list(group)  #musi być przypisane bo raz wywołana 'list(group)'-> póżniej daje same 000
        # print(name,gr)
        a=len(gr) #bo raz wywołana 'list(group)'-> póżniej daje same 00
        kod.append(name)
        if a!=1:
            kod.append(str(a))
            # kod.append(str(len(gr)))
    # print(kod)
    # return (''.join(kod))
    return (napis,'->',''.join(kod))

print(zliczacz('baaaallleee'))     #ba4l3e3
print(zliczacz('hhhhhhhfgfee'))    #h7fgfe2
print(zliczacz('dsdssssss'))       #dsds6
print(zliczacz('gggggggtrrrrrrr')) #g7tr7

print('-------'*15)
'''
###############################################################################
'''
print('Koder = Usówanie powtarzajacych sie znaków')
print('przykład:    baaaallleee -> bale')

def koder(napis: List[str]) ->List[str]:
    kod=[]
    for name, group in groupby(napis):
        gr=list(group)
        # print(name,gr)
        # a=len(list(group))
        a=len(gr) #bo raz wywołana 'list(group)'-> póżniej daje same 0000000
        kod.append(name)
    # print(kod)
    # return napis,'->',''.join(kod)
    return ''.join(kod)


print(koder('baaaallleee'))     #bale
print(koder('hhhhhhhfgfee'))    #hfgfe
print(koder('dsdssssss'))       #dsds
print(koder('gggggggtrrrrrrr')) #gtr
'''
#########################################################################
print('-------'*15)

def doubles(napis):
    while True:
        kod=[]
        for i in range(len(napis)+1):
            for name, group in groupby(napis):
                gr=list(group)  #musi być przypisane bo raz wywołana 'list(group)'-> póżniej daje same 000
                # print(name,gr)
                a=len(gr) #bo raz wywołana 'list(group)'-> póżniej daje same 00
                # print(a)
                if a%2==1:
                    kod.append(name)

            # return (''.join(kod))
            return (napis,'->',''.join(kod))

##########################################################
def doubles(napis):
    for i in range(len(napis)):
        for j in range(len(napis)-i):
            print(i,j)
            for name, group in groupby(napis):
                gr=list(group)  #musi być przypisane bo raz wywołana 'list(group)'-> póżniej daje same 000
                # print(name,gr)
                a=len(gr) #bo raz wywołana 'list(group)'-> póżniej daje same 00
                # print(a)
                kod=[]
                if a%2==1:
                    kod.append(name)
        if kod[i]==kod[i+1]:
            kod.pop(i)
        # print(kod)
        # return (''.join(kod))
    return (napis,'->',''.join(kod))

# print(doubles('abbbzz'))    #,'ab')
# print(doubles('zzzzykkkd'))    #,'ykd')
# print(doubles('abbcccdddda'))   #,'aca')
# print(doubles('vvvvvoiiiiin')) #,'voin')
# print(doubles('rrrmooomqqqqj')) #,'rmomj')
# print(doubles('xxbnnnnnyaaaaam'))  #,'bnyam')
print(doubles('abba'))  #,'')
# print(doubles('wabbae'))  #,'we')

#########################################################
# def doubles(s):
#     if s.isalpha:
#         litery=[]
#         for znak in s:
#             litery.append(znak)
#             # for i in range(len(s)+2):
#             if znak[0]==znak[1]:
#                 del znak[0]
#         # litery=set(litery)
#         # litery=list(litery)
#         print(''.join(litery))
#         # print(litery)

# doubles('aaaaaaasssd') #>>>'asd'
# string='aaadeewwwt'
# A=list(string)
# print(A)
# for a in range(len(A)+1):
#     # print(a)
#     # zlicz=A.count(A[a])
#     print(f'zlicz {A[a].upper()}:',zlicz)
#     # print(type(zlicz))
#     if A.count(A[a])>1:
#         # print('1')
#         A[a]='0'
#         if A[a]=='0':
#             A.remove('0')
#             print('hej',A)

            # A.remove('0')

################################################################
        # for i in A:
        #     if A[a] != '0':
        #         nowe=[]
        #         nowe.append(A[a])
        #         print('nowe',nowe)
# if A[a]=='0':
# print(','.join(nowe))
    # for a in range(A.count(None)):
    #     A.remove(None)


# for znak in string:
#     print(znak)




# a=list(string)
# print(''.join(string))
# del a[0]
# del a[0]
# print('string',string)
# for i in enumerate(5):
#     print(i)
###############################################################################
