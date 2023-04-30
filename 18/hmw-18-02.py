# Створити клас TelegramBot, який має бути унаслідуваний від Bot та має містити:
# власні атрибути url, chat_id (None за замовчуванням)
# методи send_message, set_url та set_chat_id.


class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'My name is {self.name}')

    def send_message(self, message):
        print(f'The message is "{message}"')


class Telegrambot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.chat_id = None
        self.url = None

    def set_url(self, url):
        self.url = url
        # print(f'My url is set to {self.url}')

    def set_chat_id(self, chat_id = None):
        self.chat_id = chat_id
        # print(f'My chat_id is set to {self.chat_id}')

    def send_message(self, message):
        print(f'I am the Telegrambot object with chat_id "{self.chat_id}" and url = {self.url} \nAnd I send you this message: {message}')


tgbot = Telegrambot('Kew')
tgbot.say_name()
tgbot.set_url('google.com')
tgbot.set_chat_id('not none')
tgbot.send_message('Hello world')