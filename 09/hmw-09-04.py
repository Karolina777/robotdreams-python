# Factorial with recursion

def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return factorial_recursion(n - 1) * n


num = int(input('Enter the index of Fibonacci number to be printed:  '))


# check if the number of terms is valid
if num <= 0:
    print("Please enter a natural number")
else:
    print(f'{num}! =  {factorial_recursion(num)}')
