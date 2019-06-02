# Automate the Boring Stuff with Python
# Chapter 4 - Lists
# 2-June-2019

# Naming and Checking Pets

myPets=['Zophie', 'Pooka','Fat-tail']
print('Enter pet name:')
name=input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')

# Advanced interation - independent of what is asked in book

# Entering Pet Info
myPets=[]
while True:
    print('Enter a pet name ' + str(len(myPets)+1) + ' (or enter nothing to stop):')
    name=input()
    if name =='':
        break
    myPets=myPets + [name]

# Checking to see if name has been used
print('Check a pet name:')
name=input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')

    
