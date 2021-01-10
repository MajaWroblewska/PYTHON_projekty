'''sprawż czy nr tel jest poprawny
poprawne formaty
123456789
+4812356789
004812356789'''


import  re
def is_phone_number(number: str) ->bool:
    pattern = r"(\+48|0048)?\d{9}"  # (?)=jedno z(+48 albo 0048), d=liczby od 0-9, {9}=9 liczb,
                                    # \ = by + traktowany był jak zwykły znak a nie jak znak specjalny
    p = re.compile(pattern)
    # return bool(p.fullmatch(number))
    return bool(re.fullmatch(pattern, number))



print(is_phone_number('123456789')) #True
print(is_phone_number('0049123456789'))   #False
print(is_phone_number('0081234567894'))  #False



print(is_phone_number('0048500500500')) # True
print(is_phone_number('0049500500500')) # False