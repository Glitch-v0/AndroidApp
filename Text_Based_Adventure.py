import random
import sys
import time as t
from Characters import Character, Enemies, you
from Events import location, next_step
from Fight_Sequence import fight, battle

# next_step("intro")
# next_step("beginning")

new_or_load = input("Would you like to load a previous save? ('Y' or 'N')")
if new_or_load.upper() == 'Y':
    import pickle
    file_opener = open('TBA_Save.pickle', 'rb')
    you = pickle.load(file_opener)

elif new_or_load.upper() == 'N':
    print('\nStarting a new game...\n')

# print(you.current_stats(), you.level)
location('Camp')
