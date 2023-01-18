# Fibonacci Sequence iterator

class FibonacciIterator:
    def __init__(self):
        self.value1 = 0
        self.value2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.value1
        self.value1, self.value2 = self.value2, self.value1 + self.value2
        return temp


fib_iterator = FibonacciIterator()

num = int(input('Enter the index of Fibonacci number to be printed:  '))
for i in range(num):
    next(fib_iterator)
print(f'The {num}th number in Fibonacci sequence is {next(fib_iterator)}')


