slownik={',':17,'do':5,'dom':2,'aga':20}
# print(slownik.items())

for i, j in slownik.items():    #wyświetlanie klucza dla wartości w słowniku
    maksymalna_wartosc=max(slownik.values())
    if j == maksymalna_wartosc:
        print(f'max wartosc: "{maksymalna_wartosc}" jest dla klucza: "{i}"')

print('slownik jaki tuple: ->',slownik.items())
print('posortowane wg wartości słownika (czyli 2 elementy krotki): ->',sorted(slownik.items(),key=lambda x: x[1]))
print('posortowane wg klucza słownika (czyli 1 elementy krotki): ->',sorted(slownik.items()))
                                                #domyślnie -> key=lambda x: x[0])





