# До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX

import re


phone_book = dict()

# Regular expression to match phone numbers
phone_number_pattern = r"^(?:\+?38)?(?:0|\(0\))?\d{9}$"

# create the initial phone book
while True:
    user_input = input('Enter a phone record "Name Number" (or "stop" to finish creating the phon book): ')
    user_input_split = user_input.split()

    command_length = len(user_input_split)

    match command_length:
        case 1:
            match user_input_split[0]:
                case 'stop':
                    print('Phone boom=k is created')
                    break
                case _:
                    print('Unknown command, try again')
        case 2:
            name = user_input_split[0]
            number = user_input_split[1]

            match = re.match(phone_number_pattern, number)

            if not match:
                print(f"Number {number} is not Ukrainian valid number")
                continue
            if name not in phone_book.keys():
                phone_book.update({name: number})
            else:
                print('This name is already in your phone book, please use unique names')
                continue
        case _:
            print('Unknown command, try again')

print(phone_book)