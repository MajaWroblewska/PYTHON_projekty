'''Ile jest liczb nieparzystych od 0 do N'''
def odd_count(n):     #Maja mało wydajny
    count=0
    while n%2==1:
        continue
        count+=1
    n-=1
    return count

def odd_count(n): #Maja - szybki
    return int(n/2) #liczb nieparztstych jest połowa z l.p n zaokragajac w dół lub bez przecinków
#########################################
def odd_count(n):
    return len(range(1, n, 2))
##########################################
def odd_count(n):
    return(n // 2)
###########################################
def odd_count(n):
    return n>>1
#############################################
def odd_count(n):
    return n/2
###############################################
odd_count=lambda n:len(range(1,n,2))
###############################################
def odd_count(n):
    print(n)
    return (n-1)/2 if not n % 2 == 0 else n/2
################################################
odd_count = lambda _: _//2

print(odd_count(15))    #>>7