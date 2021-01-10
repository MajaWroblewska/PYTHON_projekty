num = input('Podaj liczbę:')
# BEZ BREAK:
while int(num) > 9:
    sum = 0
    for i in str(num):
        sum += int(i)
    num = sum
print(num)

# Z BREAK:
while 1:
    sum = 0
    for i in str(num):
        sum += int(i)
    num = sum
    if num < 10:
        break
print(num)