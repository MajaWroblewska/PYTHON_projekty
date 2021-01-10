def create_phone_number(n):
    # print(n)
    n=str(n)
    n=n.replace(' ','')
    n=n.replace(',','')
    n=n.replace('[','')
    n=n.replace(']','')
    # print(n, type(n), len(n))

    # result='('+n[0:3]+')'+' '+n[3:6]+'-'+n[6:]
    result= f'({n[0:3]}) {n[3:6]}-{n[6:]}'
    return result
################################################################
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
##############################################################
def create_phone_number(n): #Kris
    n = str(n).replace(',','').replace(' ','').replace('[','').replace(']','')
    return f"({n[:3]}) {n[3:6]}-{n[6::]}"
#################################################################################
def create_phone_number(n):
    n=''.join(map(str,n))
    return '({i}) {j}-{k}'.format(i=n[:3],j=n[3:6],k=n[6:])
#####################################################################################
def create_phone_number(n): #coś podobnego robiłam na początku
    n = "".join([str(x) for x in n] )
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))
#####################################################################################
create_phone_number = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
################################################################################################
from functools import reduce

def create_phone_number(n):
    return reduce( lambda a,c: a.replace('x',c, 1), list(map(str,n)), '(xxx) xxx-xxxx')
###############################################################################################

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  #, "(123) 456-7890")
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  #, "(111) 111-1111")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  #, "(123) 456-7890")
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))  #, "(023) 056-0890")
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  #, "(000) 000-0000")