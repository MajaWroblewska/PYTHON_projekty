def find_outlier(integers):
    # print(integers)
    even_list=[]    #2
    odd_list=[]     #1
    for i in integers:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
        if len(even_list)==1:
            result = even_list[0]
        elif len(odd_list)==1:
            result = odd_list[0]
    return result
###################################################################3
def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]
#######################################################################
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
########################################################################
def find_outlier(integers):
    even = list(filter(lambda x: x % 2 == 0, integers))
    odd = list(filter(lambda x: x % 2 == 1, integers))
    # print(even)
    # print(odd)
    # print(list(set(integers) - set(even)))
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]

################################################################################

print(find_outlier([2, 4, 6, 8, 10, 3]))  #, 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  #, 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))   #, 160)