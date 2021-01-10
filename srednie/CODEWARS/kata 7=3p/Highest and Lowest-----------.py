def high_and_low(sting):
    l1=sting.split()
    print('**=',l1)

    new1=[]
    new2=[]
    for i in l1:
        i=int(i)
        new1.append(i)
        new_max=max(new1)
        new_min=min(new1)
        new2=str(new_max)+' '+str(new_min)
    print(new2)
    print(type(new2))


high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")    #>> "542 -214"

# a=[1,2,44]
# print(max(a))
