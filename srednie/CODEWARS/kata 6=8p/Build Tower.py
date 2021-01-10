def tower_builder(n_floors):    #Maja 1
    tree=[]
    for i in range(n_floors):
        a=('*'+(2*i)*'*').center(2*n_floors-1)
        tree.append(a)
    return tree
        ############################################
def tower_builder(n_floors): #Maja 2
    return [('*' + (2 * i) * '*').center(2 * n_floors - 1) for i in range(n_floors)]

########################################################
def tower_builder(n_floors):  # Maja 3 + print
    a= [('*' + (2 * i) * '*').center(2 * n_floors - 1) for i in range(n_floors)]
    for flor in a:
        print(flor)
    return '|'.center(2*(n_floors)-1)

###################################################
def tower_builder(n):return [f'{"*"*i:^{n*2-1}}' for i in range(1,n*2,2)]   #Jana

######################################################
def tower_builder(n_floors):    #Bartek
    return_list = []
    i = 0
    space = n_floors
    for floor in range(1, n_floors + 1):
        return_list.append((' ' * (space - 1)) + "*" * (floor + i) + (' ' * (space - 1)))
        i += 1
        space -= 1
    return return_list
######################################################################
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
########################################################################
def tower_builder(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]
###########################################################################


print(tower_builder(1)) #, ['*', ])
print(tower_builder(2)) #, [' * ', '***'])
print(tower_builder(3)) #, ['  *  ', ' *** ', '*****'])
print(tower_builder(4)) #, ['  *  ', ' *** ', '*****'])
print(tower_builder(5)) #, ['  *  ', ' *** ', '*****'])
print(tower_builder(6)) #, ['  *  ', ' *** ', '*****'])
print(tower_builder(7)) #, ['  *  ', ' *** ', '*****'])
print(tower_builder(8)) #, ['  *  ', ' *** ', '*****'])
# print(tower_builder(28)) #, ['  *  ', ' *** ', '*****'])
'''
pietro=n
szerokość=2n-1
ilość "*"=1+2+2+2+...   (+2)
odstepy przed i po '*'=n-1)-i(pietro)
    *       5-1 - 
   ***      3-3
  *****     2-5
 *******    1-7
*********   0-9

  *  
 ***
*****

'''