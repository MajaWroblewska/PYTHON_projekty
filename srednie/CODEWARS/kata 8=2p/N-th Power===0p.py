'''
To kata pochodzi z czeku py.checkio.org

Otrzymujesz tablicę z liczbami dodatnimi i liczbą N. Powinieneś znaleźć N-tą potęgę elementu w tablicy o indeksie N. Jeśli N jest poza tablicą, zwróć -1. Nie zapominaj, że pierwszy element ma indeks 0.

Spójrzmy na kilka przykładów:

tablica = [1, 2, 3, 4] i N = 2, to wynik to 3 ^ 2 == 9;
tablica = [1, 2, 3] i N = 3, ale N jest poza tablicą, więc wynik to -1.
'''

# def index(array, n):
#     for i in range(len(array)):
#         for j in range(len(array)-i-1):
#             if 0 < n < len(array):
#                 result=array[n]**n
#             else:
#                 result= -1
#     return result

def index(array, n):
    if n<len(array):
        result = array[n]**n
    else:
        result = -1

    return result
#############################################################
# def index(array, n):
#     try:
#         return array[n]**n
#     except:
#         return -1
# ################################################################
# def index(array, n):
#     return array[n]**n if n < len(array) else -1
# ####################################################################
# def index(array, n):
#     if n < len(array):
#         return (array[n])**n
#     else:
#         return -1
# ###################################################################
# def index(array, n):
#     return -1 if n >= len(array) else array[n] ** n
# ####################################################################


# print(index([1,2,3,4],2))   #9
# print(index([1, 3, 10, 100], 3)) #100 00 00
# print(index([1, 3, 10, 100], 9)) #-1
print(index([1, 3, 10, 11], -1)) #0.090909??? =)
print(index([1, 3, 10, 11], 0)) #1 )


