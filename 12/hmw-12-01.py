#  Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.

import json, os


phone_book = dict()

# create the initial phone book
while True:
    user_input = input('Enter a phone record in the following format: Name Number (or "stop" to finish creating the phon book): ')
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

            if not number.isdigit():
                print('Phone number should contain only digits')
                continue
            if name not in phone_book.keys():
                phone_book.update({name: number})
            else:
                print('This name is already in your phone book, please use unique names')
                continue
        case _:
            print('Unknown command, try again')

# phone_book ={'Name14': 123,
#              'Name16': 4534,
#              'Name17': 35454,
#              'Name18': 345}
# print(phone_book)


# save the phone book to json file
file_path = "hmw-12-01-file1.json"

if os.path.isfile(file_path):
    with open(file_path, "r") as f:
        existing_data = json.load(f)

    phone_book.update(existing_data)  # update phone_book with existing_data

    with open(file_path, "w") as f:
        json.dump(phone_book, f, indent=4)
else:
    # If the file doesn't exist yet, create a new file and write the dictionary to it
    with open(file_path, "w") as f:
        json.dump(phone_book, f, indent=4)
