def shared_bits(a, b):              #Maja
    aa=bin(a)[2:]   #aa-> str
    bb=bin(b)[2:]   #bb-> str
    listA, listB =list(aa), list(bb)
    # print(a,aa,b,bb)
    # print(aa, type(aa))
    # print('aa:',listA)
    # print('bb:',listB)
    maks=max(len(listA),len(listB))
    # print(maks)
    while len(listA)!=len(listB):
        if len(listA)>len(listB):
            listB.insert(0,'0')
        else:
            listA.insert(0,'0')
    # print(listA)
    # print(listB)
    list1=[]
    for i in range(maks):
        if listA[i]=='1' and listA[i]==listB[i]:
            list1.append(i)
    # print(len(list1))
    if len(list1)>1:
        result = True
    else:
        result = False
    # print('indeks powtórzeń 1=',list1)
    return result
###########################################################
def shared_bits(a, b):
    return bin(a & b).count('1') > 1
########################################################
from itertools import zip_longest   #?????????? zip_longest()
def shared_bits(a, b):
    return sum(map(lambda x: int(x[0]) and int(x[1]), zip_longest(bin(a)[2:][::-1], bin(b)[2:][::-1], fillvalue=0)))>1
################################################################
def shared_bits(a, b):
    count = 0
    while a != 0 and b != 0:
        if a % 2 == 1 and b % 2 == 1:
            count += 1
        if count == 2:
            return True
        a //= 2
        b //= 2
    return False
###############################################################
def shared_bits(a, b):
    num = a & b
    count = bin(num).count("1")
    if count >= 2:
        return True
    return False
##############################################################
def shared_bits(a, b):
    return len(bin(a&b).strip('0b0'))>1
###############################################################
def shared_bits(a, b):          #od końca lp bin
    x = list(bin(a)[2:])[::-1]
    y = list(bin(b)[2:])[::-1]
    count = 0

    r = min(len(x), len(y))

    for i in range(r):
        if int(x[i]) == int(y[i]) and int(x[i]) == 1:
            count += 1

    if count >= 2:
        return True
    return False
################################################################
def shared_bits(a, b):
    return sum(map(lambda z: int(z), bin(a & b)[2:])) > 1
###############################################################
def shared_bits(a, b):  #podobne do Maja też wyrównał len() lp binarnych
    a = bin(a)[2:]
    b = bin(b)[2:]
    print(type(a))
    a=a.zfill(len(b))
    b=b.zfill(len(a))
    print(a)
    print(b)
    l = min(len(a), len(b))
    result = 0
    for i in range(l):
        if int(a[i]) and int(b[i]):
            result += 1
    return result > 1


print(shared_bits(1, 2))    #, False)
print(shared_bits(16, 8))   #, False)
print(shared_bits(1, 1))    #, False)
print(shared_bits(2, 3))    #, False)
print(shared_bits(7, 10))   #, False)
print(shared_bits(43, 77))  #, True)
print(shared_bits(7, 15))   #, True)
print(shared_bits(23, 7))   #, True)


