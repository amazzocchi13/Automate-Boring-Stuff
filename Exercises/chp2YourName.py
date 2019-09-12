# Automate the Boring Stuff with Python
# Chapter 2 - Flow Control Statements
# 28-May-2019

# while Loops

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# break Statements
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print ('Thank you!')


