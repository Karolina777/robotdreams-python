# Fibonacci Sequence with recursion

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


num = int(input('Enter the index of Fibonacci number to be printed:  '))


# check if the number of terms is valid
if num <= 0:
    print("Please enter a natural number")
else:
    print(f'The {num}th number in Fibonacci sequence is {fibonacci_recursion(num)}')
