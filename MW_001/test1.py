print("wpisz liczbę")
x=input()
x=int(x)
if x>5:
    print("Większe od 5")
else:
    print("mniejsze od 5")

#1
y = 5>6
print(type(y))
if y:
    print("tak")
else:
    print("nie")

#2
y = "0"
print(type(y))
if bool(y):
    print("tak")
else:
    print("nie")

#3
y = input()
y=int(y)
print(type(y))
if bool(y):
    print("tak")
else:
    print("nie")