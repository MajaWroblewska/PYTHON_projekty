def count_bits(n):
    bina=bin(n)[2:]
    lista = []
    for znak in bina:
        lista.append(int(znak))
    result = sum(lista)
    return result
##########################################
# print(bin(84)[2:], type(bin(2)))
####################################################
def countBits(n):
    return bin(n).count("1")
####################################################
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
###################################################
def countBits(n):
    return bin(n)[2:].count('1')
#####################################################
count_bits = lambda n: bin(n).count('1')
###################################################
def count_bits(n):  #Bartek
    sum = 0
    for b in bin(n)[2:]:
        sum += int(b)
    return sum
###############################################################




print(count_bits(0))    #, 0)
print(count_bits(4))    #, 1)
print(count_bits(7))    #, 3)
print(count_bits(9))    #, 2)
print(count_bits(10))   #, 2)