'ignorowanie danych'
name, *_ = ("Jan", "Kowalski", 23)
print(f"Hi {name}")
print("*"*30)

*name_and_surname, age = ("Jan", "Kowalski", 23)
print(f"You are {age} years old")
print('nieistotne dane z *args wypakowane do listy:',name_and_surname)

print("*"*30)

'2zad-\
Przy pomocy rozpakowywania przypisz do osobnych zmiennych pierwsze dwa i 5 ostatnich elementów \
będących wynikiem wywołania funkcji range(1000)'

def fun():
    return range(1000)

print("liczby lp 1,2 i 5 ostatnich: przez funkcję")
a1,a2,*_,aa,ab,ac,ad,ae= fun()
print(a1,a2,aa,ab,ac,ad,ad)
print(list(fun()))
print("*"*30)

###########################################

a,b,*_,c,d,e,f,g=range(1000)
print('lub:')
print(a,b,c,d,e,f,g)
print("*"*30)
###############################################
