# До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX

import re
import json


# Regular expression to match phone numbers
phone_number_pattern = r"(\s|^)(?:\+?380|0)\d{9}(\s|$)"
file_name = 'phone_book2.json'
try:
    with open(file_name, 'r') as file:
        phone_book_json = file.read()
        # Load the phone book into a dictionary variable
        phone_book = json.loads(phone_book_json)
        print(phone_book)
except FileNotFoundError:
    print("Phone book file not found, creating empty phone book")
    phone_book = dict()




flag_to_create_new_file = False

# work with created phone book
while True:
    user_input = input('\nWhat do you want to do with your phone book?'
                       '\nEnter command from the list (stats, add <name phone>, delete <name>, list, show <name>, or stop to finish): ')

    user_input_split = user_input.split()
    command_len = len(user_input_split)

    match command_len:
        case 1:
            match user_input_split[0]:
                case 'stats':
                    print(f'Your phone book has {len(phone_book)} records')
                case 'list':
                    for key in phone_book.keys():
                        print(key)
                case 'stop':
                    if flag_to_create_new_file == True:
                        with open(file_name, 'w') as file:
                            json.dump(phone_book, file)
                            print("The phone book was changed and thus the file was rewritten")
                    else:
                        print("The phone book was NOT changed")
                    print('Have a nice day!')
                    break
                case _:
                    print('Unknown command, try again')
        case 2:
            match user_input_split[0]:
                case 'delete':
                    if user_input_split[1] in phone_book.keys():
                        del phone_book[user_input_split[1]]
                        print(f'The record with the name {user_input_split[1]} is deleted from phone book')
                        flag_to_create_new_file = True
                    else:
                        print(f' The name \'{user_input_split[1]}\' is NOT in your phone book')
                case 'show':
                    if user_input_split[1] in phone_book.keys():
                        print(f'Name is {user_input_split[1]} and phone number is {phone_book[user_input_split[1]]}')
                    else:
                        print(f' The name \'{user_input_split[1]}\' is NOT in your phone book')
                case _:
                    print('Unknown command, try again')
        case 3:
            if user_input_split[0] == 'add':
                match = re.match(phone_number_pattern, user_input_split[2])

                if not match:
                    print(f"Number {user_input_split[2]} is not Ukrainian valid number")
                    continue

                if user_input_split[1] not in phone_book.keys():
                    phone_book.update({user_input_split[1]: user_input_split[2]})
                    print(f'Record with the Name {user_input_split[1]} is added to phone book')
                    flag_to_create_new_file = True
                else:
                    print(f' The name \'{user_input_split[1]}\' is already in your phone book')
            else:
                print('Unknown command, try again')

