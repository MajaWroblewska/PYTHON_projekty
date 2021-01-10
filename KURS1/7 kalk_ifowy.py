# zad8 kalkulator

a=float(input('Podaj a:'))
b=float(input('Podaj b:'))
znak=input('Podaj działanie jakie mam wykonać na tych liczbach!')

if znak == '+':
    print('Suma to:', a+b)
elif znak =='-':
    print('Różnica to:', a-b)
elif znak == '*':
    print('Iloczyn to:', a*b)
elif znak==':' or znak=='/': #bez znak=='/' każdy znak wpisany spowoduje dzielenie
    print('Iloraz to:', a/b)
elif znak =="%":
    print('Reszta z dzielenia a/b to:',a%b)

else:
    print('błędny znak')