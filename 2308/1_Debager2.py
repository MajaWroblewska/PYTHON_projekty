# int('1a') # zły typ bo a nie da sie zamieniać na liczbę
data = [5,8,2,4,7,9,3]
def bubbleSort(alist):
    length = len(alist)
    for i in range(length): #1 (lenght-1) lub #2
        if i ==len(alist):  #2 dopisane by nie wychodzia poza zakres lub
            break            #
        first = alist[i]
        second = alist[i + 1] # pozaa zakres wychodzi
        if first > second:
            a, b = alist.index(first), alist.index(second)
            alist[b], alist[a] = alist[a], alist[b]
    return data # zwracaź alist
print(bubbleSort(data))