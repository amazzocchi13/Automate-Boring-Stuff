# Automate the Boring Stuff with Python
# Chapter 4 - Lists
# 2-June-2019

# Project 1
# Comma Code

# Write a fxn that takes a list value as an argument and returns a string with all the items separated by a comma and a space with and inserted before the last item.


def rewrite(someList):
    for i in range(len(someList)):
        if i == 0:
            reprint = someList[i]
        elif i <= len(someList)-2:
            reprint = reprint + ', ' + someList[i]
        else:
            reprint = reprint + ', and ' + someList[-1]
    print(reprint)
    

spam = ['A', 'B', 'C', 'D']
rewrite(spam)

    
        
        
    
