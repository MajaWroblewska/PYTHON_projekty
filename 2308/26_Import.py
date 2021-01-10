import math
# print(math.pi)

'''import datetime
a=datetime.date.today().strftime("%B %d, %Y")

b=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")  #data godzina, dzeiń tyg

import time
print(time.ctime())
print(time.time()) #sekundowe

print(a)
print(b)'''
# losowanie
import random
losowanie=random.randint( 0 , 10)
print(losowanie)
if losowanie<10 and losowanie>5:
    print('Tak')
else:
    print('Nie')