'''ZAD 18
Za pomocą metody groupby napisz funkcję, która zamienia podany ciąg znaków o wielu
powtarzających się literach wg schematu:
baaaallleee -> ba4l3e3
Zwróć uwagę, że pojedynczy element nie ma dopisanej liczby wystąpień.'''

from itertools import groupby
from typing import List #właczenie typownia


print('baaaallleee -> ba4l3e3')
def koder(napis: List[str]) ->List[str]:
    kod=[]
    for name, group in groupby(napis):
        a=len(list(group)) #bo raz wywołana 'list(group)'-> póżniej daje same 0000000
        if a==1:
            # print('*',a)
            nowe=f'{name}'
        else:
            # print('-',a)
            nowe=f'{name}{a}'
        kod.append(nowe)
    # print(kod)
    print(napis,'->',''.join(kod))


koder('baaaallleee')
koder('hhhhhhhfgfee')
koder('dsdssssss')
koder('gggggggtrrrrrrr')
