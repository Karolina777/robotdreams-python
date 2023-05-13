# Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери
# справжньої адреси, а весь інший текст має бути замінений на *.
# Кількість * необовʼязково має відповідати кількості замінених символів


import re

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, 'r') as file:
        file_contents = file.read()

        emails = re.findall(r'\S+@\S+', file_contents)

        # replace each email with X***@****X
        for email in emails:
            first, *middle, last = email
            middle = ''.join('*' for _ in middle)
            file_contents = file_contents.replace(email, f"{''.join(first)}{middle}@{middle}{''.join(last)}")

        print(file_contents)

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
