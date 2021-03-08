def iq_test(numbers):
    numbers=numbers.split(' ')
    print(numbers)
    for i in range(len(numbers)):
        odd=[]  #3
        even=[] #2
        print(numbers.index(str(7)))
        # print(i,numbers[i])

        # if numbers[i]%2==0:
        #     print(i)
            # even.append(i)
            # print(even)
        # else:
        #     odd.append(i)
        #     print(odd)



print(iq_test("2 4 7 8 10")) #,3
# print(iq_test("1 2 2"))  #, 1

'''
a=[2,3,4,6,33]
b=[33]
print(a.index(b[0])+1)
for i in range(len(a)):

    if a[i]%2==0:
        print('tak')
    else:
        print('nie')
'''