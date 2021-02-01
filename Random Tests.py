import random


def choice_counter(number):
    # List of pets
    pets = ["cat", "dog", "bird", "lizard", "snake"]

    # Odds of getting a pet
    def choose_a_pet_weighted():
        choice = random.choices(pets, [40, 35, 15, 8, 2])
        return choice[0]

    # Variables to count
    cat, dog, bird, lizard, snake = 0, 0, 0, 0, 0

    # The count process
    for count in range(number):
        choose = choose_a_pet_weighted()
        if type(choose) != str:
            print("Error! Pets list must only contain typed out names. No numbers or special characters.")
        if choose == "cat":
            cat += 1
        if choose == "dog":
            dog += 1
        if choose == "bird":
            bird += 1
        if choose == "lizard":
            lizard += 1
        if choose == "snake":
            snake += 1

    # Shows the totals
    print(f"cats = {cat}, dogs = {dog}, birds = {bird}, lizards = {lizard}, snakes = {snake}")

    # Gets the most common and uncommon counts
    choose_the_biggest = [cat, dog, bird, lizard, snake]
    choose_the_biggest.sort()
    print(f"The most uncommon occurence: {choose_the_biggest[0]}")
    print(f"The most common occurence: {choose_the_biggest[-1]}")


# choice_counter(100)

def equation_study():
    hits = 0
    misses = 0
    luck = 10
    accuracy_recordings = []
    for i in range(10 ** 2):
        luck_roll = random.sample((range(1, 101)), luck)
        print(luck_roll)
        if 100 in luck_roll:
            hits += 1
            # print("You scored a CRITICAL HIT!")
        elif 100 not in luck_roll:
            misses += 1
        else:
            print("ERROR")
    print(f"{hits} hits, {misses} misses")


def choice_sequence(intro, choices, destinations):
    while True:
        print(intro)
        number_of_choices = len(choices)
        valid_inputs = []
        for i in range(1, number_of_choices + 1):
            print(f"'{i}': {choices[i - 1]}")
            valid_inputs.append(i)
        try:
            user_choice = int(input())
            result = destinations[user_choice - 1]
            if user_choice not in valid_inputs:
                print(f'Error! You must enter a number from 1 to {number_of_choices}.')
            else:
                vowels = ['a', 'e', 'i', 'o', 'u']
                if result[0] in vowels:
                    print(f'Wow! That was an {result} fart.')
                    return result
                else:
                    print(f'Wow! That was a {result} fart.')
                    return result
        except ValueError:
            print('Error! You did not enter a number.')


# choice_sequence(intro='What would you like to do next?\n',
#                 choices=['Cat', 'Dog', 'Bird'],
#                 destinations=['hairball machine', 'poop eater', 'squawking menace'])

choice_sequence(intro='How would you like your fart to sound?\n',
                choices=['Meepy-squeaky', 'Resonant', 'Short burst', 'elongated', 'Wet', 'Haunting'],
                destinations=['boinky', 'deep', 'perky', 'impressive', 'juicy', 'ethereal'])

choice_sequence(intro='You have arrived at your camp.\n',
                choices=['Look for a fight.', 'Save your progress', 'Explore'],
                destinations=['Fight', 'Save Screen', 'Wilds'])
