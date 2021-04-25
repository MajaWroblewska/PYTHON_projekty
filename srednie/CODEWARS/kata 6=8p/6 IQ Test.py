'''Zwraca pozycję na której jest liczba ina niż wszystkie np. parzysta gdy reszta jest nieparzysta i na odwrót'''
def iq_test(numbers):
    numbers=numbers.split()
    print(numbers)
    parz=[]
    nieparz=[]
    for i in range(len(numbers)):
        a=i+1
        if int(numbers[i])%2==0:
            # print(i+1, numbers[i], type(numbers[i]))
            parz.append(numbers[i])
        else:
            nieparz.append(numbers[i])
    if len(parz)==1:
        result=numbers.index(parz[0])+1
    else:
       result=numbers.index(nieparz[0])+1
    return result
####################################################################
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    # print(e)
    # print('liczna tak:',e.count(True))

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
########################################################################
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1
#################################################
def iq_test(numbers):
    nums = map(int, numbers.split(" "))
    evens, odds = 0, 0
    for i, n in enumerate(nums):
        if n % 2 == 0:
            evens += 1
            ei = i
        else:
            odds += 1
            oi = i

    if evens == 1:
        return ei + 1
    return oi + 1
#####################################################
def iq_test(numbers):
  digits = [int(x) for x in numbers.split()]
  print(digits)
  even = [x % 2 for x in digits]    #lista reszt z dzielenia przez 2
  print(even)
  print(sum(even))
  if sum(even) == 1:

    return even.index(1) + 1
  else:
    return even.index(0) + 1
  ############################################################
def iq_test(numbers):
  a=list(map(lambda x : int(x)%2,numbers.split(' ')))
  print(a)
  return 1+(a.index(0) if (a.count(0)) == 1 else a.index(1))
#################################################
def iq_test(numbers):
    even = []
    odd = []
    for i, num in enumerate(map(int, numbers.split()), start=1):
        if num % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return min(even, odd, key=len)[0]
#######################################################


print(iq_test("2 4 7 8 10")) #,3
print(iq_test("1 2 2"))  #, 1
print(iq_test('7 5 33 2'))  #4


