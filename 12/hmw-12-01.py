#  Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.

import json
import os


def save_phonebook_to_file(file_path_link, phone_book_dict):
    # save the phone book to json file
    with open(file_path_link, "w") as file:
        json.dump(phone_book_dict, file, indent=4)

file_path = "hmw-12-01-file1.json"
phone_book = dict()

# open file with the existing phone book data and write existing data to the dictionary phonebook
if os.path.isfile(file_path):
    with open(file_path, "r") as f:
        existing_data = json.load(f)

    phone_book.update(existing_data)

initial_records = len(phone_book)

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
                    print('Have a nice day!')
                    break
                case _:
                    print('Unknown command, try again')
        case 2:
            match user_input_split[0]:
                case 'delete':
                    if user_input_split[1] in phone_book.keys():
                        del phone_book[user_input_split[1]]
                        save_phonebook_to_file(file_path,phone_book)
                        print(f'The record with the name {user_input_split[1]} is deleted from phone book')
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
                if user_input_split[1] not in phone_book.keys():
                    phone_book.update({user_input_split[1]: user_input_split[2]})
                    save_phonebook_to_file(file_path, phone_book)
                    print(f'Record with the Name {user_input_split[1]} is added to phone book')
                else:
                    print(f' The name \'{user_input_split[1]}\' is already in your phone book')
            else:
                print('Unknown command, try again')
