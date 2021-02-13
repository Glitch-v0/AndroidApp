import time as t
import random as r
import pickle

import AdventureRPGKivy
from Exploration import explore_chungus

"""How to change the story variable"""


# def new_print(*arg):
#     print(f"{arg} is type {type(arg)}")
#     AdventureRPGKivy.AdventureText.get_running_app().story += arg
#     return AdventureRPGKivy.AdventureText.get_running_app().story

def load_save():
    file_opener = open('TBA_Save.pickle', 'rb')
    you = pickle.load(file_opener)
    return you


def easy_add_just_text(list_of_strings):
    AdventureRPGKivy.AdventureText.get_running_app().story_chugger(list_of_strings)


#def easy_add_function(list_of_strings, final_function):
   # AdventureRPGKivy.AdventureText.get_running_app().story_chugger(list_of_strings)


def location(area):
    from Characters import you
    # Your rest area
    def rest_time():
        you.current_health = you.max_health
        t.sleep(3)
        easy_add_just_text([f'Your health: {you.current_health}/{you.max_health}\n'])

    if area.capitalize() == "Camp":
        easy_add_just_text(["You are at the camp.\n"])
        AdventureRPGKivy.AdventureText().choice_sequence_function_results(intro='What would you like to do next?\n',
                                                                          choices=['Leave camp', 'Save your progress',
                                                                                   'See your inventory',
                                                                                   'Rest'],
                                                                          result_functions=[location('Wilds: 1'),
                                                                                            location('Save Screen'),
                                                                                            location(
                                                                                                'Inventory Screen'),
                                                                                            location('Rest')],
                                                                          result_text=['', '', '', ''])
    #
    # # Your general non-base area
    # if area == "Wilds: 1":
    #     location(AdventureText.choice_sequence(intro='You are in the wilds.\n',
    #                                            choices=['Look for a fight.', 'Go to camp', 'Explore'],
    #                                            result_functions=['Fight Zone: 1', 'Camp', 'Explore']))
    # if area == 'Explore':
    #     explore_chungus(you.explore_points)
    #     you.explore_points += 1
    #     print(f'Explore points = {you.explore_points}')
    #     location('Wilds: 1')
    #
    # # Rest area
    # if area.capitalize() == 'Rest':
    #     if you.current_health == you.max_health:
    #         print("You are healthy and well. There is currently no need to rest.")
    #     elif 2 / 3 < you.current_health / you.max_health < 1:
    #         print("You decide it would be wise to rest.")
    #         t.sleep(6)
    #         print("You awake feeling healthy and well. That was nice.")
    #         rest_time()
    #     elif 1 / 3 < you.current_health / you.max_health <= 2 / 3:
    #         print("You find your cot and find yourself drifting to sleep...")
    #         t.sleep(6)
    #         print("You awake feeling well rested. You needed that.")
    #         rest_time()
    #     elif you.current_health / you.max_health <= 1 / 3:
    #         print("You crawl to your cot and pass out...")
    #         t.sleep(6)
    #         print("You're tired, but grateful to have survived.")
    #         rest_time()
    #     else:
    #         print("ERROR- check the camp code.")
    #     print('\n')
    #     location('Camp')
    #
    # # Save progress
    # if area == 'Save Screen':
    #     import pickle
    #     pickle_out = open('TBA_Save.pickle', 'wb')
    #     pickle.dump(you, pickle_out)
    #     pickle_out.close()
    #     print('Your stats have been saved.')
    #     location('Camp')
    #
    # # Inventory Screen
    # if area == 'Inventory Screen':
    #     for item in you.inventory:
    #         print(f'{item.quantity} {item.name}')
    #     location('Camp')
    # # Look for a fight
    # if area == "Fight Zone: 1":
    #     enemy_list = ['field mouse', 'wild hog', 'scrawny wolf']
    #     from Fight_Sequence import battle
    #     print("You begin searching for a foe...")
    #     t.sleep(3)
    #     enemy = str(r.choices(enemy_list, [0.85, 0.15, 0.05])).strip('[]')
    #     battle(enemy[1:-1])


def next_step():
    from AdventureRPGKivy import you
    from kivy.clock import Clock
    text = ''

    def clear(*args):
        AdventureRPGKivy.AdventureText.get_running_app().story = ''
        return AdventureRPGKivy.AdventureText.get_running_app().story

    def clear_then_print(*args):
        clear()
        AdventureRPGKivy.AdventureText.get_running_app().story += text
        return AdventureRPGKivy.AdventureText.get_running_app().story

    def nothing(*args):
        return None

    clear()
    easy_add_just_text(
        [f"Greetings, {you.name}. There is truly none like you.\n\n"
         "You are a chosen vessel.\n"
         "Your potential is limitless." + '\n' * 3,
         "You have 3 attributes. Strength, luck, and charisma.\n\n\n"
         "Strength is a determinant of your damage.\n\n"
         "Luck gives a chance to increase your damage and evasion in combat.\n\n"
         "Charisma affects your actions and relations with friend and foe alike.\n\n"
         "Additionally, your health is a representation of how much damage you can take before perishing.\n\n",

         "Your Stats:\n\n"
         f"Strength = {you.strength}\n"
         f"Luck = {you.luck}\n"
         f"Charisma = {you.charisma}\n"
         f"Health = {you.current_health}/{you.max_health}\n",

         'This is where you currently stand.\n'
         "As you gain more experience, you will level up and gain more health.\n"
         "Additionally, you will be able to choose a stat point to increase.\n",
         "You will now be taken to your transient place of rest- the base camp.\n"
         "You may return to camp to rest from your endeavors.\n"])
