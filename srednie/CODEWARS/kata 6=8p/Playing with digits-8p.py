#(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n *k

def dig_pow(n, p):
    # print(f'{n} - {p}')
    lw = []
    suma=0
    for j in str(n):
        lw.append(int(j))
        suma += int(j)**p
        p+=1
    k=suma/n
    # print('k=',k)
    if suma%n !=0:
        result = -1
    else:
        result = int(k)

    # print(lw)
    # print(len(lw))
    # print('suma=',suma)

    return result
###################################################################
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
  # return int(s/n) if s%n==0 else -1
########################################################################
def dig_pow(n, p):  #divmod ???????????
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
######################################################################
def dig_pow(n, p):
  t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)) )
  return t//n if t%n==0 else -1
#######################################################################
def dig_pow(n, p): #jak Maja
    # your code
    n_list = [int(i) for i in str(n)]
    n_sum = 0
    # p_i = p
    for n_i in n_list:
        n_sum = n_sum + n_i**p
        p = p+1
    if n_sum%n == 0:
        return n_sum/n
    else:
        return -1
################################################################
def dig_pow(n, p):  #jak Maja
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
########################################################
def dig_pow(n, p):  # ???
    nums = map(int, str(n))
    exps = range(p, p+len(nums))
    result = sum([x**y for x, y in zip(nums,exps)])
    return result / n if result % n == 0 else -1
##################################################################
def dig_pow(n, p):  #Kris
    result = 0
    for digit in str(n):
        result += int(digit)**p
        p += 1
    if result%n == 0:
        return int(result/n)
    else:
        return -1
############################################################
print(dig_pow(89, 1))   #k= 1)
print(dig_pow(92, 1))   #k= -1)
print(dig_pow(46288, 3))    #k= 51)
print(dig_pow(123, 3))    #k= -1)
print(dig_pow(695, 2))    #k=2 )
print('*'*30)

