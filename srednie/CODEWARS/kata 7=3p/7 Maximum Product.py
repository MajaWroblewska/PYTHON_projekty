# def adjacent_element_product(array):    #Maja
#     lista_of_product=[]
#     for i in range(len(array)):
#         for j in range(len(array)-i-1):
#             element_two=array[j]*array[j+1]
#             lista_of_product.append(element_two)
#             maximum=max(lista_of_product)
#     return maximum
# ####################################################################
def adjacent_element_product(numbers):  #JakubZ !!!!!!!!!!!!!!!!
    print('l0=',numbers)
    list1 = numbers[:len(numbers)-1:]
    print('l1=',list1)
    list2 = numbers[1::]
    print('l2=',list2)
    result = map(lambda x, y: x * y, list1, list2)
    wynik=list(result)
    print('result=', wynik)
    return max(wynik)
# #######################################################################
# def adjacent_element_product(array):
#     return max( a*b for a, b in zip(array, array[1:]) )
# def adjacent_element_product(array):
#     return max(array[i]*array[i+1] for i in range(len(array)-1))
# ##########################################################################
# #Kris
# def adjacent_element_product(array):
#     product_adj_num = []
#     second_num = 1
#     for first_num in array:
#         second_num *= first_num
#         product_adj_num.append(second_num)
#         second_num = first_num
#
#     product_adj_num.pop(0)  # we're getting rid of first result from our list
#     product_adj_num.sort(reverse=True)  # sorting in descending order
#
#     return product_adj_num[0]  # extracting highest product from our sorted list
# #######################################################################################
# from operator import mul
# def adjacent_element_product(array):
#     return max(map(mul, array, array[1:]))
# ########################################################################################
# def adjacent_element_product(array):
#     return max(x * y for x, y in zip(array, array[1:]))
# ######################################################################################
# from itertools import islice
#
# def adjacent_element_product(xs):
#     return max(x * y for x, y in zip(xs, islice(xs, 1, None)))
# ##########################################################################################!!!!!!!!!
# def adjacent_element_product(arr):
#     product = [arr[i]*arr[i+1] for i in range(len(arr)-1)]
#     return max(product)
# #################################################################################!!!!!!!!!!!!!!!
# def adjacent_element_product(array):
#     products = []
#     for i in range(0, len(array) - 1):
#         products.append(array[i] * array[i + 1])
#     return max(products)
# ##################################################################################!!!!!!!!!!!
# def adjacent_element_product(array):
#     max = array[0]*array[1];
#     for i in range(1,len(array)-1):
#         temp = array[i]*array[i+1]
#         if max < temp:
#             max = temp
#     return max
# ###############################################################################
# def adjacent_element_product(arr):
#     return max(arr[i] * n for i, n in enumerate(arr[1:]))
# ##################################################################################
# from collections import Counter
# from itertools import starmap
# from operator import mul
# from typing import List
#
# def adjacent_element_product(array: List[int]) -> int:
#     """ Get the maximum product obtained from multiplying 2 adjacent numbers in the array. """
#     return max(starmap(mul, list(zip(array, array[1:]))))
# #################################################################################################
#
#
print(adjacent_element_product([1, 5, 10, 9]))  #90
print(adjacent_element_product([1,2,3]))    #6
print(adjacent_element_product([3, 6, -2, -5, 7, 3]))   #21
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))    #-14
print(adjacent_element_product([1, 0, 1, 0, 1000])) #0
# #################################################################
#
# '''
# Test.it("Positive numbers")
# Test.assert_equals(adjacent_element_product([5, 8]), 40)
# Test.assert_equals(adjacent_element_product([1, 2, 3]), 6)
# Test.assert_equals(adjacent_element_product([1, 5, 10, 9]), 90)
# Test.assert_equals(adjacent_element_product([4, 12, 3, 1, 5]), 48)
# Test.assert_equals(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)
#
# Test.it("Both positive and negative values")
# Test.assert_equals(adjacent_element_product([3, 6, -2, -5, 7, 3]), 21)
# Test.assert_equals(adjacent_element_product([9, 5, 10, 2, 24, -1, -48]), 50)
# Test.assert_equals(adjacent_element_product([5, 6, -4, 2, 3, 2, -23]), 30)
# Test.assert_equals(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]), -14)
# Test.assert_equals(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)
#
# Test.it("Contains zeroes")
# Test.assert_equals(adjacent_element_product([1, 0, 1, 0, 1000]), 0)
# Test.assert_equals(adjacent_element_product([1, 2, 3, 0]), 6)
# '''