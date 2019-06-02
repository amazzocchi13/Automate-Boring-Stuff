# Automate the Boring Stuff with Python
# Chapter 4 - Lists
# 2-June-2019

# Collecting pet information to store
# Uses concepts from chp 4 but is not a given task

# Import pandas as pd
import pandas as pd

# Import numpy as np
import numpy as np

# Create the Dataframe

while True:
    print('Enter pet name (or enter nothing to stop):')
    name=input()
    print('Enter pet species:')
    species=input()
    print('Enter pet age:')
    age=input()
    if name=='':
        break
    petNames = petNames + [name]
    petSpecies = petSpecies + [species]
    petAges = petAges + [age]

myPets=pd.DataFrame({"Names": petNames,"Species":petSpecies,"Age":petAges})
    
        
        
        
        
    

