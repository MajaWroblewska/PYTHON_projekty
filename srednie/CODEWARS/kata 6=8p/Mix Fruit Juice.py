from statistics import mean     #Maja

for5=[ 'banana', 'orange', 'apple', 'lemon', 'grapes']
for7=["avocado", 'strawberry', 'mango']
for9=[]
slownik={'banana':5, 'orange':5, 'apple':5, 'lemon':5, 'grapes':5,'avocado':7, 'strawberry':7, 'mango':7}

def mix_fruit(arr):
    arr1=[fruit.lower() for fruit in arr]
    price=[]
    for i in arr1:
        if i in slownik:
            price.append(slownik[i])
        else:
            price.append(9)
        out=mean(price)

    # return (arr1, price,round(out))
    return (round(out))
########################################################################
def mix_fruit(arr):     #Maja2
    arr1=[fruit.lower() for fruit in arr]
    out1=[slownik[i] for i in arr1 if i in slownik]  #else slownik[i]=9 ]
    out2=[9 for i in arr1 if i not in slownik]
    out=out1+out2
    # return (arr1, price,round(out))
    return (round(mean(out)))
#################################################################################
def mix_fruit(arr):     #Maja3
    arr1=[fruit.lower() for fruit in arr]
    out=[slownik.get(i,9) for i in arr1]
        # return (arr1, price,round(out))
    return (round(mean(out)))
################################################################################
def mix_fruit(arr):     #Maja4
    out=[slownik.get(i.lower(),9) for i in arr]
    # return (arr1, price,round(out))
    return (round(mean(out)))
############
def mix_fruit(arr):     #Maja5
    return round(mean([slownik.get(i.lower(),9) for i in arr]))

######################################################################################
# costs = { 'banana': 5, 'orange': 5, 'apple': 5, 'lemon': 5, 'grapes': 5,
#            'avocado': 7, 'strawberry': 7, 'mango': 7 }
#
# def mix_fruit(arr):
#     return round( sum( costs.get(fruit.lower(), 9) for fruit in arr ) / len(arr) )
###########################################################################
# mix_fruit=lambda arr: round(sum(5 if f.lower() in ["banana","orange","apple","lemon","grapes"] else 7 if f.lower() in ["avocado","strawberry","mango"] else 9 for f in arr)/float(len(arr)))
#############################################################################
def mix_fruit(arr):
    d1 = {x:5 for x in 'banana, orange, apple, lemon, grapes'.split(', ')}
    # print(d1)   #tworzy słowniki z 5
    d2 = {x:7 for x in 'avocado, strawberry, mango'.split(', ')}
    # print(d2)   #tworzy słowniki z 7
    res = sum(d1.get(x.lower(), d2.get(x.lower(), 9)) for x in arr)
    return round(res/len(arr))
##################################################################################
def mix_fruit(arr): ###!!!!!!!!!!!!!!!!!!!!!!!
    regular = ["banana", "orange", "apple", "lemon", "grapes"]
    special = ["avocado", "strawberry", "mango"]
    return round(sum(5 if fruit.lower() in regular else (7 if fruit.lower() in special else 9) for fruit in arr)/len(arr))
#######################################################################################
PRICES = dict(banana=5, orange=5, apple=5, lemon=5, grapes=5, avocado=7, strawberry=7, mango=7)
# print(PRICES)

def mix_fruit(fruits):
    return round(sum(PRICES.get(fruit.lower(), 9) for fruit in fruits) / len(fruits))
########################################################################################
def mix_fruit(arr): # zwykłe!!!!!!!!!!!!!!!
    arr = [x.lower() for x in arr]
    total = 0
    total_number_of_fruits = len(arr)
    for fruit in arr:
        if fruit in ['banana', 'orange', 'apple', 'lemon', 'grapes']:
            total += 5
        elif fruit in ['avocado', 'strawberry', 'mango']:
            total += 7
        else:
            total += 9

    answer = round(total / total_number_of_fruits)
    return answer
#######################################################################################
def mix_fruit(arr): #takie moje proste
    Regular = ['banana', 'orange', 'apple', 'lemon', 'grapes']
    Special = ['avocado', 'strawberry', 'mango']
    cost = []
    for fruit in arr:
        fruit = fruit.lower()
        if fruit in Regular:
            cost.append(5)
        elif fruit in Special:
            cost.append(7)
        else:
            cost.append(9)
    return round(sum(cost)/len(cost))
########################################################################################
from collections import defaultdict         # defaultdict !!!!!!!!!!!
from statistics import mean

prices = defaultdict(lambda: 9)
prices.update(dict.fromkeys(['banana', 'orange', 'apple', 'lemon', 'grapes'], 5))
prices.update(dict.fromkeys(['avocado', 'strawberry', 'mango'], 7))

def mix_fruit(arr):
    return round(mean(prices[fruit.lower()] for fruit in arr))
##########################################################################
def mix_fruit(arr):     #generator !!!!!!!!!!!!!!!!!!!
    standard = ["apple", "banana", "orange", "lemon", "grapes"]
    special = ["avocado", "strawberry", "mango"]

    def sum_gen(fruits):
        for fruit in fruits:
            standard_case = fruit.lower()
            if standard_case in standard:
                yield 5
            elif standard_case in special:
                yield 7
            else:
                yield 9

    return round(sum(sum_gen(arr)) / len(arr))


print(mix_fruit(["banana", "mango", "avocado"]))    #, 6)
print(mix_fruit(["melon", "Mango", "kiwi"]))   #, 8)
print(mix_fruit(["watermelon", "cherry", "avocado"]))   #, 8)
print(mix_fruit(["watermelon", "lime", "tomato"])) #, 9)
print(mix_fruit(["blackBerry", "coconut", "avocado"]))  #, 8)
print(mix_fruit(["waterMelon", "mango"]))  #, 8)
print(mix_fruit(["watermelon", "pEach"]))  #, 9)
print(mix_fruit(["watermelon", "Orange", "grapes"]))   #, 6)
print(mix_fruit(["watermelon"]))   #, 9)
print(mix_fruit(["BlACKbeRrY", "cOcONuT", "avoCaDo"])) #, 8)