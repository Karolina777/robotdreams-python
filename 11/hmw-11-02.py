# Написати кастомний Exception клас, MyCustomException,
# який має повідомляти "Custom exception is occured"

class MyCustomException(Exception):
    def __init__(self, message='Custom exception is occurred'):
        super().__init__(message)


try:
    raise MyCustomException()
except MyCustomException as e:
    print(e)
