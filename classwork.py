
class ContactOne:
    def __init__(self, name):
        self.name = name
        self.phone_number = []


class ContactTwo:
    def __init__(self, name):
        self.__name = name
        self.__phone_number = []

    def contact_info(self):
        print(f"Contact name {self.__name}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if str(name).isalpha() and len(name) > 2:
            self.__name = name
            return self.__name


contact_one = ContactOne('Joomart')
contact_two = ContactTwo('Jide')
print(contact_one.name)
print(contact_two.name)

contact_one = 'Arthur'
print(contact_one.name)

contact_two = 'Arthur'
print(contact_two.name)


class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__heart = 120
        self.__kidney = 80
        self.__eyes = 'blue'
        self.__skin = 'white'
        self.__lips = 'red'
        self.__brain = True
        self.__legs = 'short'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if str(name).isalpha() and len(name) >= 2:
            self.__name = name
        return self.name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if type(age) == int and 150 >= age >= 0:
            self.__age = age

    @property
    def eyes(self):
        return self.__eyes

    @property
    def skin(self):
        return self.__skin

    @property
    def lips(self):
        return self.__lips

    @property
    def legs(self):
        return self.__legs

    def current_heart_beat(self):
        print(self.__heart)

    def current_kidney_beat(self):
        print(self.__kidney)

    def davlena(self):
        from random import randint
        heart_beat = randint(130, 200)
        kidney_beat = randint(50, 100)
        self.__heart = heart_beat
        self.__kidney = kidney_beat
        self.__brain = False
        self.__eyes = 'red'

    def drug(self):
        self.__heart = 120
        self.__kidney = 80
        self.__eyes = 'blue'
        self.__brain = True

