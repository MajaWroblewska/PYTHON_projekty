'Rozpakowywanie w wyrażeniach'
people = [("Jan", "Kowalski", 44), ("Eliza", "Kowalska", 53), ("Henryk", "Nowak", 34)]
for name, surname, age in people:   #tu przypisujemy nazwy kolejnym zmiennym z listy
    print(f"Hi {name} {surname}. You are {age} years old.")

print("*"*30)

'3zad \
Za pomocą rozpakowywania i list comprehensions zamień listę krotek na słownik \
    prices = [("apples", 5.50), ("oranges", 6.30), ("bananas", 3.44)]\
    prices_dict = { <uzupełnij> }'

prices=[('apples',5.50),('ornge',6.30),('bananas',3.44)]
prices_dict=print('dict(list):\t\t\t',dict(prices))
prices_dict=print('comprehensions dict:',{x:y for x,y in prices})
prices_dict=print('comprehensions dict:',{name:price for name, price in prices})
print("*"*30)
######################################


