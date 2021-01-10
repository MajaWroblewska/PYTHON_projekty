class UserDb(object):
    def __init__(self):
        self.users_data = {}

    def add_user(self, user):
        self.users_data[user.name] = user


class User(object):
    def __init__(self, name, password, email, database=None):
        self.name = name
        self.password = password
        self.email = email
        self.database = database
        self.database.add_user(self)


# name = input('Podaj nazwe uzytkownika: ')
# password = input('nadaj haslo: ')
# email = input('podaj adres e-mail: ')
data_instance1 = UserDb()

print(data_instance1.users_data)
user1 = User('Tadeusz', "Drozda", 'smiesznie@wp.pl', data_instance1)
print(data_instance1.users_data)
user2 = User('Mateusz', 'Morawiecki', 'pies@zrzadu.pl', data_instance1)
print(data_instance1.users_data)
#print(data.users_data)

#print(data.users_data)

#print(data.users_data)




