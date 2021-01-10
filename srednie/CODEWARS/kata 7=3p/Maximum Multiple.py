def max_multiple(divisor, bound):   #Maja
    for i in range(1,bound+1):
        if i%divisor==0:
            lista=[]
            lista.append(i)
    return max(lista)
######################################################
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
##########################################################
def max_multiple(divisor, bound):
    return bound // divisor * divisor
#############################################################
def max_multiple(divisor, bound):
    return divisor * int(bound/divisor)
################################################################
def max_multiple(divisor, bound):
    return [x for x in range(divisor*2, bound+1, divisor)][-1]


print(max_multiple(2, 7))   #, 6)
print(max_multiple(3, 10)) #, 9)
print(max_multiple(7, 17))  #, 14)
print(max_multiple(10, 50)) #, 50)
print(max_multiple(37, 200))    #, 185)
print(max_multiple(7, 100)) #, 98)
print("<COMPLETEDIN::>")