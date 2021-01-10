#wypisanie kwadratów liczb od 0-100
b=[x**2 for x in range(100)]
print(b)

#wartośc numeryczna ascii str 'Powerslave'
wynikKoncowy=[80,111,119,101,114,115,108,97,118,101]
a=[ord(x) for x in 'Powerslave' ]
print(a)

#wypisanie kwadratów liczb od 0-100 wypisanie jak set
b=[x for x in range(10)]
print(set(b))  #dana wyj jest set ale przze wywołanie f-cji

#wypisanie kwadratów liczb od 0-100 wypisanie jak set
b={x for x in range(10)} #dana wyj set prze zamiana nawiasów
print(b)

#wypisanie kwadratów liczb od 0-100 wypisanie jak set
a='DowolnyNapis'
b={x:ord(x) for x in a} #dana wyj dict prze zamiana nawiasów wstawiś :::::
print(b)

