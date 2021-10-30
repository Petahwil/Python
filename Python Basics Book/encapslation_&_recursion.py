import time


def inner_factorial(number):
    if number <= 1:
        return 1
    time.sleep(1)


    def multiply(a, b):
        print(f"multiplying {a} with {b}.")
        time.sleep(1)
        return a * b
    return multiply(number, inner_factorial(number - 1))  # <- change is in here.

    # Using debugging you can see how this program runs and how the encapslated function does recursion. 
    # This program starts by running inner_factorial. There is a Call Stack that runs with the program.
    # The Call Stack is the stack data structure that stores information about the active subroutines 
    # of a computer program. The Call Stack is important because each task can have it’s own separate stack.
    # This means that each function called can be active simultaneously for different tasks doing different things.
    # Another advantage is that a Call Stack supports recursive calls automatically. Python pushes the 
    # inner_factorial ever time it is run till it reaches one onto the Call Stack. The Stack Looks like 2 3 4 5.
    # Once the if statement returns 1 the programs moves on to the recursive call multiply(number, inner_factorial(number - 1)).
    # In this call number is filled with the call stack and inner_factorial(number - 1) is filled with the return of a*b.
    # Python then pops off the stack one at a time. Starting with 2 the program then multiplys 2 with (2-1). The stack then shift up 
    # and recursivly moves through the stack one by one till nothing is left then the program ends. So the next step would be
    # multiply(number(3 popped off the call stack), return 2*1 from multiply (2))
    # multiply(number(4 popped off the call stack), return 3*2 from multiply (6))
    # multiply(number(5 popped off the call stack), return 4*6 from multiply (24))
    # return the last multiplication 5*24 which is the factorial of 5 = 120

# multiplying 2 with 1.
# multiplying 3 with 2.
# multiplying 4 with 6.
# 24

inner_factorial(4)

# The above program is a deep explination of what is happening below.

def factorial(number):
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if number < 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")
    # Calculate the factorial of number
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)


print(factorial(4))
