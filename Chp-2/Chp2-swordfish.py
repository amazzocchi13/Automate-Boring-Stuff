# Automate the Boring Stuff with Python
# Chapter 2 - Flow Control Statements
# 28-May-2019

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe, What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')
