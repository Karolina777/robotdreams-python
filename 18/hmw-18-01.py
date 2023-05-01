# Створити клас Bot з атрибутом name та методами say_name та send_message.
# send_message має приймати параметри self і message і має друкувати message.
# Метод say_name має друкувати значення атрибуту name.


class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'Class Bot  initialized with the name = {self.name}')

    def send_message(self, message):
        print(f'The messase is "{message}"')


bot_object = Bot('Kew')
bot_object.say_name()
bot_object.send_message(f'my name is {bot_object.name}')
