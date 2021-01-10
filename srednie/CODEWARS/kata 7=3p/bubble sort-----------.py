def bubble(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
        # print (lista)
    return lista
#######################################################################################
def bubble(lista):
    out=[]
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print ('*',lista)
                out.append(lista)
    # print (lista)
    return out

######################################################################

l1=[1,2,4,3]    #>> sol=[[1,2,3,4]]

l2=[2,1,4,3]    #>> sol=[[1,2,4,3],[1,2,3,4]]

l3=[1,4,3,6,7,9,2,5,8]  #>>
'''
sol=[[1, 3, 4, 6, 7, 9, 2, 5, 8],
    [1, 3, 4, 6, 7, 2, 9, 5, 8],
    [1, 3, 4, 6, 7, 2, 5, 9, 8],
    [1, 3, 4, 6, 7, 2, 5, 8, 9],
    [1, 3, 4, 6, 2, 7, 5, 8, 9],
    [1, 3, 4, 6, 2, 5, 7, 8, 9],
    [1, 3, 4, 2, 6, 5, 7, 8, 9],
    [1, 3, 4, 2, 5, 6, 7, 8, 9],
    [1, 3, 2, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]]
'''

print(bubble(l1))
print(bubble(l2))
# print(bubble(l3))

def bubble(lista):
    new=[]
    for i in range(len(lista)):
#         print(lista)
        for j in range(len(lista)-i-1):
#             print(lista)
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]= lista[j+1], lista[j]
                new.append(lista)
    return(new)