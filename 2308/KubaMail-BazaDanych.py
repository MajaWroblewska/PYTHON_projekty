class UserDb(object):  #klasa bazy danych
    def __init__(self):
        self.users_data = {}
    def add_user(self, user):
        self.users_data[user.name] = user

    def identify_user(self,user_name): #wejscie nazwa uzytkow w wyjscie email
        print(self.users_data[user_name])
        print(self.users_data[user_name].email)
        return self.users_data[user_name].email





class User(object):
    def __init__(self, name, password, email, database=None):
        self.name = name
        self.password = password
        self.email = email
        self.database = database #odwołanie do bazy danych
        self.database.add_user(self) # odwołanie do dodania użytkownika

    def send_massange(self,user_name,msg):  #msg= massenger(tresc wiadomosci)
        print('FROM: NoReply@sda.pl')
        print(f'TO: {self.database.identyfy_user(user_name)}')
        #odwołanie do bay danych->adres odbiorcy
        print(f'CC: {self.email}')   #adres użytkownika nadawcy
        print(f'{msg}')   #treść wiadomosci
        # print(f'')  #login nadawcy


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

print(data_instance1.identify_user('Tadeusz'))
print(user1.send_massange(user_name,msg))