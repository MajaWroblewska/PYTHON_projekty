# Zlicza ile wystąpień jest cyfr w podanych liczbach w kolejności od 0 -9
def paint_letterboxes(start, finish):
    result=[]
    for liczba in range(start,finish+1):
        liczba=str(liczba)  #int -> str
        # print('liczby sprawdzana:',liczba)
        a=('-'.join(liczba))    #podział liczba łącznikiem "-"
        # print('a=', a, type(a))
        b=a.split('-') #podział na b=listę cyfr wg łacznika "-"
        # print(b)
        result=result+ b #sklejanie list kolejnych liczb
    # print('result',sorted(result))
    odp=[]
    for a in range(0,10):
        # print(a)
        # print(result.count(str(a)))
        odp.append(result.count(str(a)))
    return (odp)

def paint_letterboxes(start, finish):
    result=[]
    odp=[]
    for liczba in range(start,finish+1):
        for i in str(liczba):
            result.append(i)
    # print(result)
    for num in '0123456789':
        odp.append(result.count(num))
    return odp

'''
################################################
def paint_letterboxes(start, finish):
    xs = [0] * 10
    for n in range(start, finish+1):
        for i in str(n):
            xs[int(i)] += 1
    return xs
######################################################
from collections import Counter

def paint_letterboxes(s, f):
    a = Counter("".join(map(str, range(s, f+1))))
    return [a[x] for x in "0123456789"]
#############################################################
def paint_letterboxes(start, finish):
    return [''.join(map(str, range(start,finish+1))).count(str(i)) for i in range(10)]
#################################################################################
def paint_letterboxes(start, finish):
    s = ''.join([str(x) for x in range(start,finish+1)])
    return [s.count(str(i)) for i in range(10)]
#############################################################################
def paint_letterboxes(start, finish):
    list = [0 for i in range(10)]

    for num in range(start, finish + 1):
        for n in str(num):
            list[int(n)] += 1

    return list
##############################################################################3
def paint_letterboxes(start, finish):
    num_str = ''.join([str(i) for i in range(start, finish +1)])
    return [num_str.count(str(num)) for num in range(0, 10)]
############################################################################
def paint_letterboxes(start, finish):
    new = sorted([int(j) for i in [str(i) for i in range(start, finish+1)] for j in i])
    test = {0: 0, 1: 0, 2: 0, 3: 0, 4:0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in new:
        if i in test:
            test[i] += 1
        else:
            test[i] = 1
    return [i for i in test.values()]
##############################################################################
def paint_letterboxes(start, finish):
    # your code
    rakam={str(i):0 for i in range(10)}
    for i in range(start,finish+1):
        for j in list(str(i)):
            rakam[j]+=1
    return list(rakam.values())
######################################################
'''
print(paint_letterboxes(125, 132))  # [1, 9, 6, 3, 0, 1, 1, 1, 1, 1]