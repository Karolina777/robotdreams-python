# Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*

import re

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, 'r') as file:
        file_contents = file.read()

        emails = re.findall(r'\S+@\S+', file_contents)

        for email in emails:
            file_contents = file_contents.replace(email, '*@*')

        print(file_contents)

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

