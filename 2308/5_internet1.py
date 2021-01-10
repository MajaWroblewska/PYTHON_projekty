# def bubbleSort (lista):
#     for kolumna in range(len(lista) - 1, 0, -1):  #dlaczego musi być od końca
#         print('kolumna',kolumna)
#         for wiersz in range(kolumna):   #why?
#             print('wiersz', wiersz)
#             print('-'*30)
#             if lista[wiersz] < lista[wiersz + 1]:   #>sort od małych, <sort od wielkich
#                 lista[wiersz],lista[wiersz+1] = lista[wiersz+1], lista[wiersz]  #zamiana w lot
#                 # temp = lista[wiersz]    #zamiana przez dodatkową zmienną temp |
#                 # lista[wiersz] = lista[wiersz + 1]
#                 # lista[wiersz + 1] = temp
#
# lista = [54, 26, 93, 3, 77, 1, 44, 55, 20]
# bubbleSort(lista)
# print(lista)
# # print(len(lista))
# '''
# # lista=[9,8,7,6,5,4,3,2,1,0]
# bubbleSort(lista)
# print(lista)
#******************************************************
def bubbleSort2 (lista):
    for kolumna in range(1, len(lista), 1):  #dlaczego musi być od końca
        #print('kolumna', kolumna)
       for wiersz in range(kolumna):   #why
         #   print('wiersz', wiersz)
         #   print('-'*30)
            if lista[wiersz] > lista[wiersz + 1]:
                lista[wiersz], lista[wiersz+1] = lista[wiersz+1], lista[wiersz]  #zamiana w lot
                # temp = lista[wiersz]    #zamiana przez dodatkową zmienną temp |
                # lista[wiersz] = lista[wiersz + 1]
                # lista[wiersz + 1] = temp
                # print(sorted(lista))
lista = [54, 260, 93, 3, 77, 1, 44, 55, 20]
bubbleSort2(lista)
print(lista)
#print(lista)
#print(len(lista))
#*******************************************************
# list = [54, 100, 93, 3, 77, 1, 44, 55, 20]
# print(sorted(list))
# print(sorted(list,reverse=True))
#
# for i in sorted(list):
#     print(i)

