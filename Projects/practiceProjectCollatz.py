# Automate the Boring Stuff with Python
# Chapter 3 - Functions
# 29-May-2019

# Practice Project - The Collatz Sequence

# Collatz Calculation
def collatz(number):
    if number == 1:
        print('My work is done here! We are finally at 1!')
    elif number % 2 == 0:
        print(int(number // 2))
        collatz(number // 2)
    else:
        print (int(3 * number + 1))
        collatz(3 * number + 1)
        
# Input Validation
try:
    collatz(int(input('Enter a counting number:')))
except ValueError:
    print('Counting number please, no strings or floats!')


# Extended Version - Counting iterations, not printing

def collatz(number):
    if number > 1:
        iteration = 0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                iteration += 1
            else:
                number = 3 * number + 1
                iteration += 1
        print('Collatz finished in ' + str(iteration) + ' iterations.')
    else:
        print('You started at 1!')

# Input Validation
try:
    collatz(int(input('Enter a counting number:')))
except ValueError:
    print('Counting number please, no strings or floats!')
        
