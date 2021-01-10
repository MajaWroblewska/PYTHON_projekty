print("start-wypisz cyfry od 1 do 10")
i=0
while i <=9:
    i += 1
    print(i)
print("koniec")

# range1
print('*'*30,'range1')
for i in range(10,-20,-6):
    print(i)
    i+=1
print('koniec')

# range2
print('*'*30,'range2')
for i in range(10,0,-1):
    print((i))
    i+=1

# range3
print('*'*30,'range3')
for i in range(0,11,1):
    print(i)
    i+=1
print('koniec')

print('*'*30)
# empty range
print('Pusta lista:',list(range(0)))

# using range(stop)
print('Lista range(10)',list(range(10)))

# using range(start, stop)
print('Lista range(1,10):',list(range(1, 10)))
print('Lista range(2,10,2):',list(range(2, 10,2)))
print('Lista range(10,1,-2):',list(range(10,1,-2)))