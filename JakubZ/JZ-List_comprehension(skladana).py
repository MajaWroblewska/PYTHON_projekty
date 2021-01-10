# a = [x for x in range(10)]
# b = [x for x in range(10) if x>5]
# c = [x for x in range(10) if not x%2]
# d = [x for x in range(10) if x%2 != 0]
#
# print(a)
# print(b)
# print(c)
# print(d)


def wyciagnij_cyfry():
    znaki = input('podaj ciag znakow: ')
    a = [int(x) for x in znaki if x.isnumeric()]

    print(a)


wyciagnij_cyfry()
#wyciagnij_cyfry('abc')
#wyciagnij_cyfry('abc 127 ade')