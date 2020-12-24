from time import sleep
from string import digits, ascii_lowercase
f = open('easypasswords.txt', 'r')


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter')
        return self.__password

    @staticmethod
    def is_num_in_key(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_letter_in_key(password):
        for letter in ascii_lowercase:
            if letter in password:
                return True
        return False

    @staticmethod
    def is_easy_key(password, file):
        lines = file.readlines()
        for line in lines:
            # print(line)
            # print(len(line))
            n = password.find(line[:-1])
            # print(line1[0])
            if n >= 1:
                # print('is inside')
                # print(line[:-1])
                # print(len(line))
                if (len(password) / (len(line)- 1)) < 1.2:
                    # print('слишком просто')
                    # print(line)
                    return True
        return False

    @password.setter
    def password(self, key):
        print('waiting.... we are setting values')
        sleep(1.5)
        if not isinstance(key, str):
            raise ValueError('Password must be str')
        if len(key) > 15:
            raise ValueError('Password must be less then 10')
        if len(key) < 4:
            raise ValueError('Password must be longer then 4')
        if User.is_easy_key(key, f):
            raise ValueError('Password must be more difficult')
        if not User.is_letter_in_key(key):
            raise ValueError('Password must be with letter')
        if not User.is_num_in_key(key):
            raise ValueError('Password must be with num')
        self.__password = key
        print('correct!')


# bob = User('bob', '11doctor')
