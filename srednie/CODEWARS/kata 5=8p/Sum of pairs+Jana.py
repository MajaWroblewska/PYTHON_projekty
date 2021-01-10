##############################################################
'''
def sum_pairs(ints, s):     #Maja - skrócić bo czas za długi
    # print('----------')
    # print(ints, s)
    lista_sum=[]
    for i in range(len(ints)):
        for j in range(len(ints)-i-1):
            # print(i, i+j+1)
            suma=ints[i]+ints[i+j+1]
            lista_sum.append(suma)
            if suma==s:
                if not ints[i]==ints[i+j+1] or ints[0]==ints[i]:    # or ints[0]==ints[i+j+1]
                    result = [ints[i], ints[i + j + 1]]
    # print('*',lista_sum)
                    return result
'''
##############################################################################################
def sum_pairs(ints, s):     #Maja za długo sie wykonuje
    a=[[ints[i], ints[i + j + 1]] for i in range(len(ints)) for j in range(len(ints)-i-1) if ints[i]+ints[i+j+1]==s and (not ints[i]==ints[i+j+1] or ints[0]==ints[i]) ]

    return a[0] if len(a)!=0 else None
################################################################################
def sum_pairs(ints, s):     #Maja - skrócić bo czas za długi
    if s % 2:
        ints = list(set(ints))      #Dodane od Jane
    for i in range(len(ints)):
        for j in range(len(ints)-i-1):
            # suma=ints[i]+ints[i+j+1]
            if ints[i]+ints[i+j+1]==s:
                if not ints[i]==ints[i+j+1] or ints[0]==ints[i]:
                    return [ints[i], ints[i+j+1]]
#########################################################################
def sum_pairs(ints, s): #Jana
    if s%2:
        ints = list(set(ints))
    lst = []
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == s:
                lst.append([ints[i], ints[j]])
                ints = ints[:j]
                break
    return lst[-1] if lst else None
############################################################################
def sum_pairs(ints, s):
    if len(ints) < 1000:
        return iterator(ints, s)
    else:
        return big_iterator(ints, s)

def iterator(ints, s):
    return_dict = {}
    while len(ints) > 1:
        iterations = 0
        first = ints.pop(0)
        for second in ints:
            if first + second == s:
                if iterations in return_dict:
                    iterations += 1
                return_dict[iterations] = [first, second]
            iterations += 1
    iterations = 0
    if return_dict:
        i = min(return_dict, key=return_dict.get)
        return return_dict[i]

def big_iterator(ints, s):
    if s % 2 == 0 and s / 2 in ints:
        ints = list(dict.fromkeys(ints))
        return iterator(ints, s)
    else:
        ints = list(set(ints))
        return iterator(ints, s)
###################################################################################
from collections import Counter
def sum_pairs(ints, s):
    if len(ints) > 1000000:
        ints = list(dict.fromkeys(ints).keys())
    for i in range(1, len(ints)):
        for j in range(len(ints)-i):
            if ints[i+j]+ints[j] == s:
                return [ints[j],ints[i+j]]
    return None
###########################################################################################
def sum_pairs(lst, s):  #??
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
#######################################################
def sum_pairs(nums, sum_value): #ciekawe
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
##################################################
def sum_pairs(ints, s):
  num_dic = {}
  for num in ints:
    if num in num_dic:
      return [num_dic[num], num]
    else:
      num_dic[s - num] = num
###################################################################
def sum_pairs(ints, s):
    seen=[]
    for item in ints:
        if s-item in seen: return [s-item, item]
        if item not in seen: seen+=[item]
    return None
######################################################################
def sum_pairs(ints, s):
    found = set()
    needed = set()
    for i in ints:
        found.add(i)
        if i in needed:
            return [s-i, i]
        needed.add(s-i)
#####################################################
def sum_pairs(ints, sum):
    iterated_ints = set()
    for i in shorten_list(ints):
        if sum - i in iterated_ints:
            return [sum - i, i]
        iterated_ints.add(i)

def shorten_list(ints):
    seen_once, seen_twice = set(), set()
    for i in ints:
        if i not in seen_once:
            seen_once.add(i)
            yield i
        elif i not in seen_twice:
            seen_twice.add(i)
            yield i
###############################################################
def sum_pairs(ints, s):     #@??????????????? coś nie fra zwraca None
    bla = set()
    try: return filter(lambda x: x != None ,[[s-x, x] if s-x in bla else bla.add(x) for x in ints])[0]
    except: return None
#####################################################



l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs(l1, 8))     # == [1, 7],    "Basic: %s should return [1, 7] for sum = 8" % l1)
print(sum_pairs(l2, -6))    # == [0, -6],   "Negatives: %s should return [0, -6] for sum = -6" % l2)
print(sum_pairs(l3, -7))    # == None,      "No Match: %s should return None for sum = -7" % l3)
print(sum_pairs(l4, 2))     # == [1, 1],    "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
print(sum_pairs(l5, 10))    # == [3, 7],    "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
print(sum_pairs(l6, 8))     # == [4, 4],    "Duplicates: %s should return [4, 4] for sum = 8" % l6)
print(sum_pairs(l7, 0))     # == [0, 0],    "Zeroes: %s should return [0, 0] for sum = 0" % l7)
print(sum_pairs(l8, 10))    # == [13, -3],  "Subtraction: %s should return [13, -3] for sum = 10" % l8)
print(sum_pairs([4, 3, 2, 3, 4], 6))    #[4,2]

