'''
Moduł oblicza MBI
'''
print('podaj wzrost w metrach-\n\t(użyj kropki zamiast przecinka)')
a=input()
wzrost=float(a)

print("podaj wagę w kilogramach")
b=input()
waga=float(b)

BMI=(waga)/(wzrost**2)

print()
print("Zakresy wartosci BMI: \nn<16              - wygłodzenie \
\nn=<16-16.99>      - wychudzenie \
\nn=<17-18.49>      - niedowaga \
\nn=<18.5-24.99>    - wartosc prawidlowa \
\nn=<25-29.99>      - nadwaga \
\nn=<30-34.99>      - I stopien otylosci \
\nn=<35-39.99>      - II stopien otylosci \
\nn>40              - skrajna otylosc")
print()
print("Twoje BMI to:",BMI)
