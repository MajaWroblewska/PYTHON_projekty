'''
content         = pojemność pojemnika początkowa
evap_per_day    = dzienna procentowa utrata pojemności
threshould      = procentow pojemność poniżej której produkt jest nieprzydatny
'''
from functools import reduce



def evaporator(content, evap_per_day, threshold):
    end=content*threshold/100

    print(f'{content}ml -stan początkowy')
    print(f'{evap_per_day}% -dzienna utrata')
    print(f'{threshold}% = {end}ml -stan końcowy')

    start=[content]
    n=0
    # na=[]

    for i in range(500):
        product = reduce((lambda x,y: x*(1-evap_per_day/100)),start)
        start.append(product)

        if start[-1] >= end:
            n+=1
            # na.append(n)

    # return na[-1]
    return n
###################################################################
def evaporator(content, evap_per_day, threshold):                   #kris
    counter = 0
    threshold_ml = content * threshold * 0.01
    while content >= threshold_ml:
        # if content == threshold_ml:
        #     return counter

        content = content - (content * evap_per_day * 0.01)
        counter += 1
    else:
        return counter
######################################################################
def evaporator(content, evap_per_day, threshold):
    n = 0
    current = 100
    percent = 1 - evap_per_day / 100.0
    while current > threshold:
        current *= percent
        n += 1
    return n
###########################################################################
import math

def evaporator(content, evap_per_day, threshold):
    return math.ceil(math.log(threshold / 100.0) / math.log(1.0 - evap_per_day / 100.0))
########################################################################################
def evaporator(content, evap_per_day, threshold):
    thres = content * threshold/100
    count = 0
    while content > thres:
        content = content - content * evap_per_day/100
        count += 1
    return count
######################################################################################
def evaporator(content, evap_per_day, threshold):
    p=100
    d=0
    while p >= threshold:
        p = p - p * (evap_per_day/100)
        d = d + 1
    return d
#####################################################################
def evaporator(content, evap_per_day, threshold):
    days = 0; full = content; limit = full * (threshold/100)
    while content > limit: content = content - content * (evap_per_day/100); days+=1
    return days
##########################################################################


print(evaporator(10, 10, 10))   #, 22