lista=[9,8,7,6,5,4,3,2,1,0]  #test
length = len(lista)
print(lista)
print(length)
# sort=[]
# for passnum in range(len(alist)-1,0,-1):

def bubble_sort(lista):
    index=1
    for index,znak in enumerate(lista):
        print(index, znak)
        # print('typ index',type(index))  #index=int
        # print('typ znak',type(znak))   #znak=int
        # znak(index)
        # if index<len(lista):
        #     first = lista[index]
        #     second = lista[index +1]
        #     if first>second:
        #         print(first)
        #         temp=first
        #         first=second
        #         second=temp
        #         # first, second = second, first

lista=[9,8,7,6,5,4,3,2,1,0]  #test
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(lista)
print(lista)




# print(first)
    # print(second)
''' # print(second)
    if first<second:
        continue
    else:
        
        first, second = second, first
        print(first)
        print(second)
    print(lista)

    a, b = alist.index(first), alist.index(second)
    alist[b], alist[a] = alist[a], alist[b]'''