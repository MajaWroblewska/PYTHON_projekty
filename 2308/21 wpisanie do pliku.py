a='12345\n67890\n'
print(a*100)
with open("xyz.txt","w") as f: #utworzył nowy plik w pycharm bo nie podaliśmy sieżki pliku
    f.write(a*100000)           # w kasuje poprzednie dane
                                # a dopisuje dane do pliku

a='12345\n67890\n'
print(a*100)
with open("C:\\Users\\LucWr\\Desktop\\xyz.txt","w") as f: #\ -> \\ w pliku
    f.write(a*75000)

