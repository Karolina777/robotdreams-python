# Написати кастомний Exception клас, MyCustomException,
# який має повідомляти "Custom exception is occured"

class MyCustomException(Exception):
    print('Custom exception is occurred')


try:
    raise MyCustomException()
except MyCustomException as mce:
    print(f'The exception name is {type(mce).__name__}')
