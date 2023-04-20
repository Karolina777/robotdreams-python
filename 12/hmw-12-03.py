# В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл

from datetime import datetime


class MyCustomException(Exception):
    def __init__(self, message='Custom exception is occurred'):
        super().__init__(message)
        self.timestamp = datetime.now()
        # Log the exception to a file
        with open("hmw-12-03-error_log.txt", "a") as f:
            f.write(f"Error '{message}' occurred at {self.timestamp}\n")

try:
    raise MyCustomException()
except MyCustomException as e:
    print(e)