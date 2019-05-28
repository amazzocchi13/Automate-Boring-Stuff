# Automate the Boring Stuff with Python
# Chapter 1 - First Program Example
# 28-May-2019

# This program says hello and asks for my name.

print('Hello world!')

# Name syntax
print('What is your name?') # asking user their name
myName = input()
print('It is nice to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)))

# Age syntax
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
