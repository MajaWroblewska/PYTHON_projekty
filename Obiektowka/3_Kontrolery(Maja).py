class ControlerSwear(object):
    def __init__(self):
        self.name= 'Kontroler brzydkich słów:'    #nazwa kontrolera
        self.curse=['dupa', 'sraka', 'kurwa']         #lista szukanych słów
    def control(self,path):
        '''
        Metoda sprawdza plik czy zawiera słowa z listy CURSE, inicjowana powyżej
        True - nie zawiera
        False - zawiera
        :parametry : path - śceżka pliku
        :return:
        '''
        with open (path,'r') as file:                   #odczytujemy tylko "r"
            zawartosc_pliku=file.read().lower()         #wypisanie pliku do zmiennej zawartosc_pliku
                                                        # wielkość liter nie ma znaczenia (.lower() )
            for i in self.curse:
                if i in zawartosc_pliku:        # pierw odczytać plik
                    # print("W pliku są wyrazy niedozwolone")   #opcjonalnie do sprawdzenia
                    return False
                # else:     #bez elsa bo return źle działa i sprawdzi tylko jedno słowo
            # print('Plik nie posiada wyrazów niedozwolonych')  #opcjonalnie do sprawdzenia
            return True             # musi sie wydazyc kiedy przejdzie cały for

# path="C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"   # \ -> \\ i w ""

# Wywołanie klasy przez przypisanie do zmiennej cs
cs=ControlerSwear()

#wypisanie nazwy kontrolera i sprawdzenie pliku metoda control()
# print(cs.name, cs.control('PlikTestowy.txt'))   #tylko nazwa pliku, gdy plik sprawdzany obok pliku pytona- w tym samym folderze
# print(cs.name, cs.control(path))                # path jako zmienna przypisana
# print(cs.name,cs.control("C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"))
# print('-'*30)
########################################################################################################################
# coś nie tak z wypisaniem 1-go znaku 1lini -> wypisuje ('"',)????

# class ControlerFirstLineString(object):
#     def __init__(self):
#         self.name='Kontroler istnienia stringu w pierwszej lini:'
#
#     def control(self,path):
#         with open(path,'r') as file:        #odczytujemy tylko "r"
#             first = file.readline()[0],      #wypisze pierwszy znak 1 lini
#             last= first[-1]                              #ostatni znak 1 lini bo enter to też znak ([-1] to enter)
#             if first=='"' and  last=='"':
#                     # first=='"' or last=="'" or last=='"':
#                 print(first)
#                 print(last)
#                 return True
#             else:
#                 print(first)
#                 print(last)
#                 return False
#
# path="C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"   # \ -> \\ i w ""
# cfls=ControlerFirstLineString()
# print(cfls.name,cfls.control(path))
# print('-'*30)
#######################################################
# działa!!!!!!!!!

class ControlerFirstLineString(object):
    def __init__(self):
        self.name='Kontroler istnienia stringu w pierwszej lini:'

    def control(self,path):
        '''
        Metoda sprawdza plik czy pierwsza linia pliku jest stringiem-jest w apostrofach
        'abc' -True
        abc   -False
        :parametry : path - śceżka pliku
        :return:
        '''
        with open(path, 'r') as file:  # odczytujemy tylko "r"
            line=file.readline()        # 1linia jako zmienna bo...
            first = line[0]             # 1x zczytana linia zostawia kursor na końcu więc last=file.readline()[-2] da nam ostatni zank 2 lini
            last = line[-2]             # wypisze pierwszy znak 1 lini
                                        # dlatego odwołuje sie do 1 lini=line i ostatniego znaku (dlatego [-2] bo...)
                                        # last = line[-2]  # ostatni znak 1 lini bo enter to też znak, ([-1] to enter)
            # print(first)  #opcjonalnie do sprawdzenia
            # print(last)   #opcjonalnie do sprawdzenia

            if (first == '"' and last == '"') or (first == "'" and last == "'"):  #na dla mieszanych "string' (jak zrobić?)
                # print('Tak')  #opcjonalnie do sprawdzenia
                return True
            else:
                # print('Nie')  #opcjonalnie do sprawdzenia
                return False

# path="C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"   # \ -> \\ i w ""
cfls=ControlerFirstLineString()
# #print(cfls.name,cfls.control(path))
# #print('-'*30)

#######################################################

# DZIALA !!!!!
# z ustawieniem kursora
# 1x zczytana linia zostawia kursor na końcu więc last=file.readline()[-2] da nam ostatni zank 2 lini

# class ControlerFirstLineString(object):
#     def __init__(self):
#         self.name='Kontroler istnienia stringu w pierwszej lini:'
#
#     def control(self,path):
#         with open(path, 'r') as file:   # odczytujemy tylko "r"
#             first= file.readline()[0]   #zczyrujemy 1 linie
#             file.seek(0)                # ustawiamy kursor na pozycje 0
#             last= file.readline()[-2]   #[-2] bo [-1] to ostatnie to znak enter a [-2] to widzialny znak
#
#             print(first)
#             print(last)
#
#             if (first == '"' and last == '"') or (first == "'" and last == "'"):  #na dla mieszanych "string' (jak zrobić?)
#                 print('Tak')
#                 return True
#             else:
#                 print('Nie')
#                 return False
#
# path="C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"   # \ -> \\ i w ""
# cfls=ControlerFirstLineString()
# # print(cfls.name,cfls.control(path))
# # print('-'*30)
########################################################################################################################
class ControlerTxt(object):
    def __init__(self):
        self.name='Kontroler rozszerzenia TXT:'
    '''
    Metoda sprawdza plik czy ma rozszerzenia .txt
    path.txt'   -True
    path.inne   -False
    :parametry : path - śceżka pliku
    :return:
    '''

    def control(self, path):
        file_extension=path.split('.')
        if file_extension[-1]=='txt':
            # print(file_extension[-1])         #opcjinalnie do sprawdzenia
            return True
        else:
            # print(file_extension[-1])         #opcjinalnie do sprawdzenia
            return False


# path = "C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"  # \ -> \\ i w ""
ctxt=ControlerTxt()
# print(ctxt.name, ctxt.control(path))
# print('-'*30)
########################################################################################################################
# coś nie tak - nie wyświetla True/False ani print('toooo')

# class ControlerSh(object):
#     def __init__(self):
#         self.name='Kontroler istnienia "#!/bin/sh" w pliku .sh :'
#         '''
#         Jeżeli plik jest .sh to skontroluj istnienie w nim stringa "#!/bin/sh" '
#         istnieje -True
#         nie ma   -False
#         :parametry: path
#         :return:
#         '''
#     def control(self,path):
#         with open (path) as file:
#             file_extension = path.split('.')
#             if file_extension[-1] == 'sh':
#                 print('plik sh')
#
#                 firstline = file.readline()
#                 print(firstline)
#                 if firstline == '#!/bin/sh':
#                     print('toooo')
#                     return True
#                 else:
#                     print('inne')
#                     return False
#
# path = "C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikSH.sh"  # \ -> \\ i w ""
# csh=ControlerSh()
# print(csh.name, csh.control(path))

####################################################
# wyświetla False mimo ze "#!/bin/sh" jest  pliku .sh w 1 lini:
class ControlerSh(object):
    def __init__(self):
        self.name = 'Kontroler istnienia "#!/bin/sh" w pliku .sh :'

    def control(self, path):
        with open(path) as file:
            return '"#!/bin/sh' in file.readline()


# path = "C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikSH.sh"  # \ -> \\ i w ""
csh = ControlerSh()
# print(csh.name, csh.control(path))

########################################################################################################################
class ControlerTab(object):
    def __init__(self):
        self.name='Kontroler istnienia Tab w plikach:'
        '''
        Metoda sprawdza czy plik zawiera tabulacje
        True - zawiera
        False - nie zawiera
        :parametry: path
        :return:
        '''
#???????????????? nie dzała
    def control(self,path):
        with open(path, 'r') as file:
            return  '\t' in file.read()

# path = "C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"  # \ -> \\ i w ""
ctab=ControlerTab()
# print(ctab.name, ctab.control(path))

########################################################################################################################
# ????????????????????????????/
#linia kontrolna
class ControlerList(object):
    def __init__(self):
        self.name = 'Lista Kontrolerów'
        self.controlers = controlers
    '''
    Matoda uruchamia wszystkie kontrolery
    :parametry: path
    :return:
    '''
    def control_on (self,path):          #metoda włączania wzystkich kontrolerów
        dictionary = {}  # stworzenie póstego słownika

        for i in controlers:
            dictionary[i.name]=[i.control(path)]    #do każdego kontrolera wpisz w słównik
                                                    # klucz=nazwa kontrolera(pole klasy -name)
                                                    # wartość= metoda uruchamiająca kontroler ze ścieżką pliku (np cs.control(path) )
        return dictionary
    def add_controler(self,controler):
        self.controlers.append(controler)


# Dane:
path="C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\Obiektowka\\PlikTestowy.txt"   # \ -> \\ i w ""
controlers=[cs,cfls]                   #lista kontrolerów

#wywołannire
cl=ControlerList()                    # cl to stworzony obiekt klasy ControlerList()

cl.add_controler(ctxt)                # dodawanie kontrolera (ctxt) do listy (controlers) -> zamieana na słównik
cl.add_controler(csh)                 # dodawanie kontrolera (csh) do listy (controlers) -> zamieana na słównik
cl.add_controler(ctab)

print(cl.control_on(path))            # wywołanie działania metody ( control_on(path) ) -> utworzene słownika kontrolerów w klasie ControlerList()
                                      # uruchomienie wszystkich kontrolerów
# print(cl.controlers)
# print(cl.control_on.dictionary[cs])     # jak dostać się do 1 klucza słownika dictionary by wypisal wartość??????????????????????


