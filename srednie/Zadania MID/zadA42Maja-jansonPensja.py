'''zad 42
Skopiuj listę pracowników z zadania 41 i wklej ją do pliku. Wczytaj plik i oblicz średnią pensję dla
pracowników w ﬁrmie.
Dołącz wyliczoną pensję do obiektu (do każdej ﬁrmy) i zapisz tak zmienione dane jako JSON w
innym pliku.'''

import json
from pprint import pprint
from statistics import mean

with open("../JSON cwiczenia/file.json", encoding='utf-8') as json_file:
    data = json.load(json_file)


# with open("save.json", "w", encoding='utf-8') as json_file:
#     json.dump(avg_salaries, json_file, ensure_ascii=False)

pensja = []
for shop,epmpoyees in data.items():
    # print(shop,epmpoyees)
    for dane in epmpoyees:
        # print(dane)
        pensja.append(dane['salary'])
        sr_pensja=mean(pensja)
    print(pensja)
    print(sr_pensja)

    # print(f'{shop}: {pensja}, sr:{sr_pensja}')

# print(data)
    #for zmienna,wartosc in dane.items():
        # print(zmienna)
        # print(wartosc)
            #
            # if zmienna=="salary":
            #     print(wartosc)
                # pensja.append(wartosc)
                # print(pensja)

with open("../JSON cwiczenia/save.json", "w", encoding='utf-8') as json_file:  # wsadzanie dopliku save.json
    json.dump(sr_pensja, json_file, ensure_ascii=False)  # (ensure_ascii=False)=można zapisać polskie znaki

    # data_json=json.dumps(data)
    # json.dumps(data_json,json_file)
