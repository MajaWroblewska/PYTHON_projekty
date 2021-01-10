
def solution(number):       #Maja
    list35=[]
    for i in range(0,number,3):
        list35.append(i)
    for j in range(0,number,5):
        list35.append(j)
    print(list(set(list35)))
    return (sum(list(set(list35))))
###################################################
def solution(number):       #Bartek
    sum = 0
    for x in range(1, number):
        if (x % 3 == 0 or x % 5 == 0):
            sum += x
    if sum <= 0:
        return 0
    else:
        return sum
#########################################################
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
##########################################################
def solution(number):
    threes = range(3, number, 3)
    fives = range(5, number, 5)
    return sum(list(set(threes + fives)))
########################################################
def solution(number):   #chain!!!!
  import itertools
  return sum(set(itertools.chain(range(0, number, 3), range(0, number, 5))))
########################################################
def solution(number):
  return sum(i for i in range(number) if i%5==0 or i%3==0)
##############################################################



# print("Multiples of 3 and 5")

print(solution(10)) #, 23=3+5+6+9)
print(solution(15)) #, 45=3+6+9+12+5+10)
print(solution(30)) #, 195=3+6+9+12+15+18+21+24+27+5+10+20+25)
print(solution(9)) #, 14=3+6+5)
print(solution(8)) #, 14=3+6+5)
