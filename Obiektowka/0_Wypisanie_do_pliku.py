a='12345\n67890\n'
with open("xyz.txt","w") as f: #'W' utworzył nowy plik w pycharm bo nie podaliśmy sieżki pliku
    f.write(a*2)           # w kasuje poprzednie dane
    f.write("Hejjjjjjj")                                # a dopisuje dane do pliku


#########################################################################
a='12345\n67890\n'
with open("C:\\Users\\LucWr\\Desktop\\xyz.txt","r") as f: #\ -> \\ w pliku na puplicie
    # zawartosc=f.read() [-10]             #dla 'r'       #a dopisuje do pliku nie usówa
    # print(zawartosc)                                            #r do odczytu nie zwpisuje
    zaw=f.readline()[-2]
    print(zaw)
    # dopisek=f.write('HOp awqhop ')          #dla 'w' nadpisuje a dla 'a' dopiesuje tekst
    # print(dopisek)          #wypisuje ilość znaków dopisanych

    # print(f.seek(0))