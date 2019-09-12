# Automate the Boring Stuff with Python
# Chapter 3 - Functions
# 29-May-2019

# Local and Global Variables with the Same Name

# Version 1

def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'


eggs = 'global'
bacon()
print(eggs) # prints 'local'

# Version 2

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# Version 3

def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is the local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)

# Version 4

def spam():
    global eggs # by adding this line, the error is corrected, take out and there will be an error
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()

