# Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.

from datetime import datetime


def my_decorator(func):
    def deco_func():
        print(f'Function name is "{func.__name__}" and the time of call is {datetime.now()}')
        func()

    return deco_func


@my_decorator
def my_func():
    print('This is my function')


my_func()
