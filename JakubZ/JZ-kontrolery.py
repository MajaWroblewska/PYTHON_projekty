class SwearCheck(object):
    def __init__(self):
        self.name = 'kontrola przeklenstw'
        self.niedozwolone = ['krowa', 'pies', 'kot']

    def control(self, filepath):
        with open(filepath, 'r') as file:
            file_content = file.read()
            for i in self.niedozwolone:
                if i in file_content:
                    return False
            return True


class SwearCheck2(object):
    def __init__(self):
        self.name = 'kontrola slow'
        self.niedozwolone = ['slonce', 'trawa']

    def control(self, filepath):
        with open(filepath, 'r') as file:
            file_content = file.read()
            for i in self.niedozwolone:
                if i in file_content:
                    return False
            return True

class FileType(object):
    def __init__(self):
        self.name = 'kontrola typu pliku'

    def control(self, filepath):
        return ('.' + filepath.split('.')[1])

    def control2(self, filepath):
        return filepath[filepath.find('.'):]


class ControlLine(object):
    def __init__(self, control_list):
        self.control_list = control_list

    def run_controllers(self, filepath):
        a = {}
        for i in self.control_list:
            a[i.name] = i.control(filepath)
        return a

    def add_control_list(self, controller):
        self.control_list.append(controller)
        print(self.control_list)


controllll_list = [FileType(), SwearCheck()]
linia = ControlLine(controllll_list)
linia.add_control_list(SwearCheck2())


print(linia.run_controllers("D:\\IT\\PycharmProjects\\SDA_learn_python\\Week_2\\swear_list.txt"))

#print(file1.control("D:\\IT\\PycharmProjects\\SDA_learn_python\\Week_2\\strzelanie_rand.py"))
#print(file1.control2("D:\\IT\\PycharmProjects\\SDA_learn_python\\Week_2\\strzelanie_rand.py"))
