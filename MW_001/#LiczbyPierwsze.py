#liczby pierwsze
for i in range(2,50):
    j=2
    counter=0
    while j<i:
        if i%j == 0:
            counter = 1
            j=j+1
        else:
            j=j+1
    if counter==0:
        print(str(i) + " -jest liczbą pierwszą")
    else:
        counter=0


