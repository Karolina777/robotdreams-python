# Fibonacci Sequence with generator

def gen_fibonacci(item_index):
    value1 = 0
    value2 = 1
    for item in range(item_index + 1):
        yield value1
        value1, value2 = value2, value1 + value2


num = int(input('Enter the index of Fibonacci number to be printed:  '))
gen_fib = gen_fibonacci(num)
print(f'The {num}th number in Fibonacci sequence is {list(gen_fib)[num]}')


