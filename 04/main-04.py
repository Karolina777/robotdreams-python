user_input = input('Please, input something here: ')

if user_input.isdigit():
    if int(user_input) % 2 == 0:
        print('Your input is an even number')
    else:
        print('Your input is an odd number')
elif ' ' in user_input:
    print('You have entered neither number, nor a word')
else:
    print(f'You have entered a string with the length of {len(user_input)} symbols')
