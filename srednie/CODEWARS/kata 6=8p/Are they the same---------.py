def comp(array1, array2):
    mapped=map(lambda x: x*x, array1)
    if set(mapped)==set(array2):
       out=True
    else:
        out=False
    return out
##############################################################
def comp(array1, array2):
    # print('a1=',array1)
    # print('a2=',array2)
    # a=[i*i for i in array1]
    # print('*',a)
    for ee in array1:
        if (ee**2)in array2:
            return (True)
    # return {i*i for i in array1}==set(array2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# a1=[]
print(comp(a1, a2)) #, True)

# w=[1,2,3]
# e=[3,2,1]
# print('*',set(w)==set(e))