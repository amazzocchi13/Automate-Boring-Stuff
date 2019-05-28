# Automate the Boring Stuff with Python
# Chapter 2 - Flow Control Statements
# 28-May-2019

# if, elif, and else Statements

print('What is your name?')
name = input()
print('And how old are you?')
age = input()

if name == 'Alice':
    print('Hi, Alice.')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither alice nor a little kid.')

