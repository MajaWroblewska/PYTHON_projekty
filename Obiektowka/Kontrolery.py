class Przeklenstwa(object):
    def __init__(self):
        self.name='Kontroler Przeklenstw'
        self.niedozwolone=['mysz','pies','kot']

    def control(self,filepath):  #wej: ściezka pliku
        with open(filepath, 'r') as file:
            zawartosc_pliku = file.read()  # wpisaniu pliku do zmiennej
            for i in self.niedozwolone:
                if i in zawartosc_pliku:  #pierw odczytać plik
                    print('W pliku sa wyrazy nidozwolone')
                    return False
                # else:     #bez elsa bo return źle działa
            print('Plik bez przekleństw')
            return True   #musi sie wydazyc kiedy przejdziecały for


class Przeklenstwa2(object):
    def __init__(self):
        self.name='Kontroler słów'
        self.niedozwolone=['trawa','drzewo','slon']

    def control(self,filepath):  #wej: ściezka pliku
        with open(filepath, 'r') as file:
            zawartosc_pliku = file.read()  # wpisaniu pliku do zmiennej
            for i in self.niedozwolone:
                if i in zawartosc_pliku:  #pierw odczytać plik
                    print('W pliku sa wyrazy nidozwolone')
                    return False
                # else:     #bez elsa bo return źle działa
            print('Plik bez przekleństw')
            return True   #musi sie wydazyc kiedy przejdziecały for

filepath='C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\2308\\test.txt'   # \ -> \\ i w ""

przeklenstwa_instance1=Przeklenstwa()
print(przeklenstwa_instance1.control(filepath))
###########################################################################

class String(object):
    def __init__(self):
        self.name = 'Kontroler istnienia Stringu w 1 lini'

    def control(self, filepath):
        with open(filepath, 'r') as file:
            zawartosc_pliku = file.readline()  # wpisaniu pliku do zmiennej

###########################################################################

# class Istnienie(object):
#     def __init__(self):
#         self.nazwa = 'Istnienia #!/bin/sh w pliku *.sh'
#
#     def control(self,filename):
#         print(filepath.split('.')[1])
#         print
#         for i in filepath:
#             if filepath[i]=='.':
#                 return()


class FileType(object):
    def __init__(self):
        self.name = 'kontrola typu pliku'

    def control(self, filepath):
        return ('.' + filepath.split('.')[1])

    def control2(self, filepath):
        return filepath[filepath.find('.'):]

file_instance1 = FileType()

###########################################################################

class Tabulacja(object):
    def __init__(self):
        self.name = 'Kontroler Tabulacji w pliku'

    def control(self, filepath):
        with open(filepath) as file:
            return "\t" in file.read()


###########################################################################
#linia kontrolna

class LiniaKontrolna(object):
    def __init__(self,control_list):
        self.control_list=control_list                #wpada kolekcje=lista kontrolerów

    def run_controlers(self,filepath):
        a={}
        for i in self.control_list:
            # print(i.control(filepath))
            a[i.name]=i.control(filepath)
            print(a)
        return a

    def add_control_line(self,controller):
        self.control_list.append(controller)
        print(self.control_list)


chack1=przeklenstwa_instance1
chack2=file_instance1
control_list=[chack1,chack2 ]  #lista z instancjiami

linia=LiniaKontrolna(control_list)
linia.add_control_line(Przeklenstwa2())

# linia_add_control=LiniaKontrolna()
print(linia.run_controlers('C:\\Users\\LucWr\\Dysk Google_Maja\\PYTHON\\_PYTHON projekty\\2308\\test.txt'))



