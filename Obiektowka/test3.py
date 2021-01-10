myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)

strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)

str = "my name is James bond";
print (str.title())

print(chr(57))
print(ord('9'))

str = "My salary is 7000";
print(str.isalnum())

str1 = ("moje imię isisis jameis isis bond")
sub = "jest"
print (str1.count (sub, 4))

słowo1 = "PYnative"
print (słowo1 [1: 4], słowo1 [: 5], słowo1 [4:], słowo1 [0: -1], słowo1 [:: - 1])

# aList = ['a', 'b', 'c', 'd']
# a=newList = copy(aList)
# b=newList = aList.copy()
# c=newList.copy(aList)
# d=newList = list(aList)
#
# print(a)
list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))
l = [None] * 10
print(len(l))

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)
sampleList.clear()
print(sampleList)

sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])
print(aList[1][3])

my_list = ["Hello", "Python"]
print("-".join(my_list))

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

aList = ['a', 'b', 'c', 'd']
newList = list(aList)
print(newList)
newList = aList.copy()
print(newList)



set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print(set1.issubset(set2))
print(set2.issuperset(set1))

sampleSet = {"Żółty", "Pomarańczowy", "Czarny"}
sampleSet.discard ("Niebieski")
print (sampleSet)

aSet = {1, 'PYnative', ('abc', 'xyz'), True}
print(aSet)

aSet = {1, 'PYnative', ['abc', 'xyz'], True}
print (aSet)