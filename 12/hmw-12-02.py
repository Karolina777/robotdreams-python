# Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику

from datetime import datetime


def my_decorator(func):
    def deco_func(*args, **kwargs):
        with open("hmw-12-02-file_name.txt" , "a") as f:
            f.write(f'Function name is "{func.__name__}"')
        print(f'Function name is written in the txt file and the time of call is {datetime.now()}')
        return func(*args, **kwargs)
    return deco_func


@my_decorator
def my_func(*args, **kwargs):
    print('This is my function')


my_func('asv', 1)