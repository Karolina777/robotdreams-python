# Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.

from datetime import datetime


def my_decorator(func):
    def deco_func(*args, **kwargs):
        print(f'Function name is "{func.__name__}" and the time of call is {datetime.now()}')
        return func(*args, **kwargs)
    return deco_func


@my_decorator
def my_func(*args, **kwargs):
    print('This is my function')


my_func('asv', 1)
