import time as t
import random as r


def choice_sequence(intro, choices, results):
    while True:
        print(intro)
        number_of_choices = len(choices)
        valid_inputs = []
        for i in range(1, number_of_choices + 1):
            print(f"'{i}': {choices[i - 1]}")
            valid_inputs.append(i)
        try:
            user_choice = int(input())
            if user_choice not in valid_inputs:
                print(f'Error! You must enter a number from 1 to {number_of_choices}.')
            else:
                # print(f'Result = {results[user_choice - 1]}.')
                return results[user_choice - 1]
        except ValueError:
            print('Error! You did not enter a number.')


def location(area):
    from Characters import you

    # Your rest area
    def rest_time():
        you.current_health = you.max_health
        t.sleep(3)
        print(f'Your health: {you.current_health}/{you.max_health}')

    if area == "Camp":
        print("You have arrived at your camp.")
        if you.current_health == you.max_health:
            print("You are healthy and well. There is currently no need to rest.")
        elif 2 / 3 < you.current_health / you.max_health < 1:
            print("You decide it would be wise to rest.")
            t.sleep(6)
            print("You awake feeling healthy and well. That was nice.")
            rest_time()
        elif 1 / 3 < you.current_health / you.max_health <= 2 / 3:
            print("You find your cot and find yourself drifting to sleep...")
            t.sleep(6)
            print("You awake feeling well rested. You needed that.")
            rest_time()
        elif you.current_health / you.max_health <= 1 / 3:
            print("You crawl to your cot and pass out...")
            t.sleep(6)
            print("You're tired, but grateful to have survived.")
            rest_time()
        else:
            print("ERROR- check the camp code.")
        t.sleep(3)
        print('\n\n')
        location(choice_sequence(intro='What would you like to do next?\n',
                                 choices=['Leave camp', 'Save your progress'],
                                 results=['Wilds', 'Save Screen']))

    # Your general non-base area
    if area == "Wilds":
        location(choice_sequence(intro='You are in the wilds.\n',
                                 choices=['Look for a fight.', 'Go to camp', 'Explore'],
                                 results=['Fight', 'Camp', 'Wilds']))

    # Save progress
    if area == "Save Screen":
        import pickle
        pickle_out = open('TBA_Save.pickle', 'wb')
        pickle.dump(you, pickle_out)
        pickle_out.close()
        print('Your stats have been saved.')
        location('Camp')

    # Look for a fight
    if area == "Fight":
        enemy_list = ['field mouse', 'wild hog']
        from Fight_Sequence import battle
        print("You begin searching for a foe...")
        t.sleep(3)
        enemy = str(r.choices(enemy_list, [0.85, 0.15])).strip('[]')
        battle(enemy[1:-1])


def next_step(progress):
    if progress == "intro":
        from Characters import you
        print(f"Greetings, {you.name}. There is truly none like you.\n\n"
              f"You are a chosen vessel.\n"
              "Your potential is limitless.\n\n")
        t.sleep(7.5)
        print("You have 3 attributes. Strength, luck, and charisma.\n\n")
        t.sleep(6)
        print("Strength is a determinant of your damage.\n"
              "Luck gives a chance to increase your damage in combat, as well as evade attacks.\n"
              "Charisma affects your actions with friend and foe alike.")
        t.sleep(6)
        print("Additionally, your health is a representation of how much damage you can take before perishing.")
        t.sleep(4)
        you.current_stats()
        t.sleep(4)
        print("\nThis is where you currently stand.\n")
        t.sleep(4)
        print("As you gain more experience, you will level up and gain more health.\n")
        t.sleep(4)
        print("Additionally, you will be able to choose a stat point to increase.\n\n")
        t.sleep(4)
    if progress == "beginning":
        print("You will now be taken to your transient place of rest- the base camp.\n")
        t.sleep(3)
        print("You may return to camp to rest from your endeavors.\n")
        t.sleep(3)
        location('Camp')
