text = input('Input some text here: ')

i = 0
while i < len(text):
    if text[i].isdigit():
        print(f'\"{text[i]}\" is a number')
    elif text[i].isalpha():
        print(f'\"{text[i]}\" is a letter')
    #elif text[i] == ' ':
    #    print('\" \" is a symbol')
    else:
        print(f'\"{text[i]}\" is a symbol')
    i += 1
