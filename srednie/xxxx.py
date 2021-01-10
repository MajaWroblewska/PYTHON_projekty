# # numbers=[0,4,5,3]
# # lista=[i**2 for i in numbers]
# # result=sum(lista)
# # print(result)
# ##############################################################
#
# a=[3,2,1,2]
#
# def flip(d, a):
#     if d=="R":
#         result=sorted(a)
#     elif d=='L':
#         result=sorted(a, reverse=True)
#     return result
# print(flip('L',a))
# print(flip('R', [3, 2, 1, 2])) #     =>  [1, 2, 2, 3]
# print(flip('L', [1, 4, 5, 3, 5])) #  =>  [5, 5, 4, 3, 1]
#
# #
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add('vik', )
# print('a1=',sampleSet)
# #
# x = 36 / 4 * (3 +  2) * 4 + 2
# print('a2=',x)
# #
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
#
# calculate(5, 6)
# #
# var = "James" * 2  * 3
# print(var)
# #
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
#
# print(listOne == listTwo)
# print(listOne is listTwo)
# #
# var= "James Bond"
# print(var[2::-1])
# #
# for i in range(10, 15, 1):
#   print( i, end=', ')
# print()
# #
# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, )
# print('a18=',sampleList)
# #
# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )
# #
#
# import numpy
# for i in numpy.arange(-0.3,3.1,0.3):
#     print(i)
# #
# import numpy as np
#
# print("Float Range Using linspace()\n")
#
# print("range from 2.5 to 12.5")
# for i in np.linspace(2.5, 12.5, num=7, endpoint=True):
#     print(round(i,3), end=', ')     #round(i,3) zakraglenie do 3 miejsc
#
# print("\n Without including stop number in the result")
# print("range from 2.5 to 12.5")
# for i in np.linspace(2.5, 12.5, num=7, endpoint=False):
#     print(round(i,3), end=', ')
#
# #
# print()
# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))
# print(type(aTuple[0]))
# print(type(aTuple[1]))
# print(type(aTuple[2]))
# print(type({}))
# #
# x = 50
# def fun1():
#     global x ##
#     x=20
#     # your code to assign global x = 20
# fun1()
# print(x) #>>it should print 20 not 50
#
