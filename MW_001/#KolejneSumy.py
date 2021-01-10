suma=0
print("wpisz liczbę")
x = input()
while True:
    if x=='':
        break
    else:
        print("wpisz liczbę")
        x = input()
        suma += int(x)
        print("kolejna suma to")
        print(suma)
