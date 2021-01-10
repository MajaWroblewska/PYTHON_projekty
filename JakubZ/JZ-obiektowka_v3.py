class UserDb(object):
    def __init__(self):
        self.users_data = {}

    def add_user(self, user):
        self.users_data[user.name] = user

    def email_by_name(self, user_name):
        #print(self.users_data[user_name])
        #print(self.users_data[user_name].email)
        return self.users_data[user_name].email



class User(object):
    def __init__(self, name, password, email, database=None):
        self.name = name
        self.password = password
        self.email = email
        self.database = database
        self.database.add_user(self)

    def send_msg(self, user_name, msg='Ziobro, Ty _____ ______! \nprzestan mi rodzine przesladowac!'):
        print('FROM: NoReply@noreply.sda.pl')
        print(f'  TO: {self.database.email_by_name(user_name)}')
        print(f'  CC: {self.email}')
        print(msg)


data_instance1 = UserDb()

#print(data_instance1.users_data)
user1 = User('Zbigniew', "Ziobro", 'z.ziobro@gov.pl', data_instance1)
#print(data_instance1.users_data)
user2 = User('Zbysiu', 'Stonoga', 'z.stonoga@.pl', data_instance1)
#print(data_instance1.users_data)

print(data_instance1.email_by_name('Zbysiu'))
user2.send_msg("Zbigniew")
