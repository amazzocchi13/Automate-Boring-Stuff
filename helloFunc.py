# Automate the Boring Stuff with Python
# Chapter 3 - Functions
# 29-May-2019

# def statements with and without parameters

# Version 1
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()

# Version 2
def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')
