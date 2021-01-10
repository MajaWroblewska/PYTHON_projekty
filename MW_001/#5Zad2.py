'''Zadanie 2
Utwórz skrypt, który zapyta użytkownika o imię, nazwisko i numer telefonu, a następnie:

Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
Użytkownicy bywają leniwi. Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich
Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
Zakładając, że twoi użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą
Połącz dane w jeden ciąg personal za pomocą spacji
Policz liczbę wszystkich znaków w napisie personal
Podaj liczbę tylko liter w napisie personal
 Podpowiedź – weź pod uwagę, że numery telefonów w Polsce są 9-cyfrowe'''

'''"""

name = input("Imię: ")
surname = input("Nazwisko: ")
number = input("Numer telefonu: ")

print("Czy imię składa się tylko z liter?", name.isalnum())
print("Czy nazwisko składa się tylko z liter?", surname.isalnum())
print("Czy numer telefonu składa się z cyfr", number.isdigit())

print(name, surname)
name = name.capitalize()
surname = surname.capitalize()
print(name, surname)

print(number)
number = number.replace(" ", "").replace("-","")
print(number)

print("Imię kobiece:", name.endswith("a"))

personal = name + " " + surname + " " + number
print(personal)
print(len(personal))

letters = len(personal) - personal.count(" ") - 9
print(letters)
print (len(name + surname)) #sprawdzenie'''