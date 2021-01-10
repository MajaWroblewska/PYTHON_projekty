def special_number(number):
    if number > 0:
        for i in str(number):
            # l1,l2 = [], []
            # l1 =[]
            l2=[]
            # print(i, type(i))
            if int(i) not in range(6):
                l2.append(int(i))
                # l1.append(int(i))
                # print(l1)
            # else:
            #     l2.append(i)
            if len(l2)>0:
                result='NOT!!'
            else:
                result="Special!!"
    else:
        result = "NOT!!"

    return result
#################################################################


print(special_number(2))    #, "Special!!")
print(special_number(5))   #, "Special!!")
print(special_number(9))    #, "NOT!!")
print(special_number(7))    #, "NOT!!")
print(special_number(23))   #, "Special!!")
print(special_number(79))   #, "NOT!!")
print(special_number(39))   #, "NOT!!")
print(special_number(55))   #, "Special!!")

print(special_number(513))  #, "Special!!")
print(special_number(709))  #, "NOT!!")
print(special_number(970569))   #, "NOT!!")
print(special_number(11350224))    #, "Special!!")
print(special_number(11350224))    #, "Special!!")
print(special_number(-11350224))    #, "NOT!!")