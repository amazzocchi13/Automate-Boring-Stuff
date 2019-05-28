# Automate the Boring Stuff with Python
# Chapter 2 - Ending a Program Early 
# 28-May-2019

import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
