
class API:
    @classmethod
    def get_data(cls):
        return "0mk20"

    def __init__(self):
        self.zmienna = 5

def get_only_numbers():
    numbers = []
    for line in API.get_data(): # odwołanie do klacy API.get_data - pobranie z return
        digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
        numbers.extend(digits)

    return '|'.join(numbers)

print(get_only_numbers())  #>>> 0|2|0

'''
class API:
    @classmethod #metoda działa bez tworzenia obiektu na klasie nie moe być zmiennych obiektu i metod obiektu
    def get_data(cls):
        return open('aa').readlines()
    def get_only_numbers():
        numbers=[]
        for line in API.get_data():
            digit=[x.strip() for x in line.split(",") if x.strip().isdigit()]
            numbers.extend(digit)
        return '|'.join(numbers)
'''