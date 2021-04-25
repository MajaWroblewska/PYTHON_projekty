def high_and_low(sting):
    l1=sting.split()
    # print('**=',l1)

    new1=[]
    new2=[]
    for i in l1:
        i=int(i)
        new1.append(i)
        new_max=max(new1)
        new_min=min(new1)
        new2=str(new_max)+' '+str(new_min)
    return(new2)
######################################################################
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
##################################################
def high_and_low(numbers):         # musi być sorted
    n = sorted(map(int, numbers.split(' ')))
    return str(max(list(n))) + ' ' + str(min(list(n)))
###########################################################
def high_and_low(numbers):
    n = sorted(map(int, numbers.split(' ')))
    print(list(n))
    print(min(list(n)))
    return "{} {}".format(max(list(n)), min(list(n)))
################################################################
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])
##################################################################
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"
#########################################################
def high_and_low(numbers):
    numbers = sorted(map(int, numbers.split()), reverse=True)
    return '{} {}'.format(numbers[0], numbers[-1])
######################################################################


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) #"542 -214");
print(high_and_low("1 -1"))   # "1 -1");
print(high_and_low("1 1"))   #"1 1");
print(high_and_low("-1 -1")) #"-1 -1");
print(high_and_low("1 -1 0")) #"1 -1");
print(high_and_low("1 1 0")) #"1 0");
print(high_and_low("-1 -1 0")) #"0 -1");
print(high_and_low("42")) #"42 42");

# a=[1,2,44]
# print(max(a))
