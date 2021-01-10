array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]
def count_sheeps(sheep):
    # TODO May the force be with you
    counter=0
    for i in sheep:
        if i==True:
            counter+=1
    print(counter)

count_sheeps(array1)    #>>17
