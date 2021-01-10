# wyszykanie konkretnej litery w napisie ważna jest wielkosc litery
znak=input('Jaki znak mam sprawdzić obecność w napisie?')
a=input('Wpisz napis ')
if znak in a:
    print('znalazłem',znak)
else:
    print('Nie ma',znak,'w napisie')


x='x' # wyszykanie konkretnej litery w napismi ważna wielkosc litery
# a=input('Wpisz napis ')
if x in a:
    print('znalazłem X')
else:
    print('Nie ma "x" w napisie')