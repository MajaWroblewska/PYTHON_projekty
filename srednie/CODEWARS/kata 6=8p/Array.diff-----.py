# a.pop() #usówanie ostatniego z listy
# a.pop(0) #usówanie 0-eg elem  z listy
'''
A=set(a)
B=set(b)
# A.differance(B)
r=A.difference(B)
print(list(r))
'''

# def array_diff(a, b):
    print(f'{a} - {b}')
    print('*',len(a)-1)
    # if len(a):
    #     for i in range(len(a)):
            print('i=',i)
            # for j in a:
                print('?',j)
                # if a[i] in b:
                    print('*',a[i])
                    # a.pop(i)
    # return (a)


# def array_diff(a, b):

print(array_diff([2], [1, 2]))  #, [], "a was [2], b was [1,2], expected []")

print(array_diff([1, 2], [1]))  #, [2], "a was [1,2], b was [1], expected [2]")
# print(array_diff([1, 2, 2], [1]))   #, [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
# print(array_diff([1, 2, 2], [2]))   #, [1], "a was [1,2,2], b was [2], expected [1]")
# print(array_diff([1, 2, 2], []))    #, [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
# print(array_diff([], [1, 2]))  #, [], "a was [], b was [1,2], expected []")

# w=[1,2,7]
# w.pop(2)
# w.remove(0)
# print(w)