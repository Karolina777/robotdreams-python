# Написати власний менеджер контексту, задачею якого буде друкувати "==========" –
# 10 знаків дорівнює перед виконанням коду та після виконання коду,
# таким чином виділяючи блок коду символами дорівнює.
#
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте
# програма не має завершити своєї роботи.
# Написати з допомогою try ... except

# Написати з допомогою конструкції try ... except ... else ... finally

try:
    print('=' * 10)
    option = input('Type 1 if you\'d like an error to occur: ')
    if option == '1':
        print(1/0)
except Exception as e:
    print(f'The error with the name "{type(e).__name__}" occurred')
else:
    print('Program continued without error')
finally:
    print('=' * 10)