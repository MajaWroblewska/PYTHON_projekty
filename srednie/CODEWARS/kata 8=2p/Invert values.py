def invert(lst=None):
    rew=[]
    for i in lst:
        rew.append(-1*i)
    return rew
################################################################
def invert(lst):
    return [-x for x in lst]


print(invert([1,2,3,4,5]))  #[-1,-2,-3,-4,-5]
print(invert([1,-2,3,-4,5]))    # [-1,2,-3,4,-5]
print(invert([])) #[]