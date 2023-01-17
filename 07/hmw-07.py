phone_book = dict()

# create the initial phone book
# while True:
#     user_input = input('Enter a phone record "Name Number" (or "stop" to finish creating the phon book): ')
#     user_input_split = user_input.split()
#
#     # print(user_input_split)
#     # print(len(user_input_split))
#     command_length = len(user_input_split)
#
#     match command_length:
#         case 1:
#             match user_input_split[0]:
#                 case 'stop':
#                     print('Phone boom=k is created')
#                     break
#                 case _:
#                     print('Unknown command, try again')
#         case 2:
#             name = user_input_split[0]
#             number = user_input_split[1]
#
#             if not number.isdigit():
#                 print('Phone number should contain only digits')
#                 continue
#             if name not in phone_book.keys():
#                 phone_book.update({name: number})
#             else:
#                 print('This name is already in your phone book, please use unique names')
#                 continue
#         case _:
#             print('Unknown command, try again')

# phone_book ={'Name1': 123,
#              'Name2': 4534,
#              'Name3': 35454,
#              'Name4':345}
# print(phone_book)


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
                    print(f'Record with the Name {user_input_split[1]} is added to phone book')
                else:
                    print(f' The name \'{user_input_split[1]}\' is already in your phone book')
            else:
                print('Unknown command, try again')
