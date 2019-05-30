# Automate the Boring Stuff with Python
# Chapter 3 - Functions
# 29-May-2019

# Exception Handling

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(1))
print(spam(0))

for i in range (2, 16, 2):
    print(spam(i))


# spam calls in 'try:' block


def spam(divideBy):
  
        return 42/divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0)) # will stop here and not continue on, one it goes to except it does not return to 'try'
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
   
