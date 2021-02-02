import time as t
import random
import sys

from Characters import Enemies, you
from Events import choice_sequence
from Items import *


def fight(foe):
    foe_name_proper = str(foe.name).capitalize()

    def item_drop(foe):
        loot = []
        for item in foe.items:
            rarity_roll = r.random()
            if rarity_roll >= 1 - item.rarity:
                loot.append(item)
        return loot

    def add_to_inventory(loot):
        for item in loot:
            if item in you.inventory:
                item.quantity += 1
            else:
                you.inventory.append(item)
        print(f"{str(foe.name).capitalize()} dropped {item.name}!")

    def victory():
        if foe.current_health <= 0:
            from Events import location
            print(f"You have defeated {foe.name}!")
            you.current_exp += foe.exp
            you.gold += foe.gold
            if foe.gold > 0:
                if foe.gold == 1:
                    print(f"{foe_name_proper} dropped a single gold coin.")
                else:
                    print(f"You have looted {foe.gold} gold coins.")
            add_to_inventory(item_drop(foe))
            print(f"You have gained {foe.exp} experience.\n"
                  f"{you.current_exp}/{you.experience_to_level} experience.\n\n")
            t.sleep(3.5)
            if you.current_exp >= you.experience_to_level:
                you.level_up()
            return location('Wilds: 1')

    def defeat():
        if you.current_health <= 0:
            print("You have died. Game over.")
            sys.exit()

    def your_turn():
        # -Critical Hit Chance-
        weapon = you.weapon
        luck_roll = random.sample((range(1, 101)), you.luck)
        miss_roll = random.sample((range(1, 101)), foe.luck)
        damage_randomness = round((you.strength + weapon) * random.randint(80, 120) / 100)
        # -Displaying your damage-
        # --Enemy Dodges--
        if 100 in miss_roll and 100 not in luck_roll:
            print(f"You would have {random.choice(you.attacks)} {foe.name},"
                  f" but {foe.gender} moved out of the way at just the right time.\n")
        # --Enemy tries to dodge, but your luck comes in to play--
        elif 100 in miss_roll and 100 in luck_roll:
            foe.current_health = round(foe.current_health - damage_randomness)
            print(f"You nearly powerfully {random.choice(you.attacks)} {foe.name}. "
                  f"{foe.gender} nearly dodged,"
                  f"but you luckily hit {foe.gender} for {damage_randomness} damage."
                  f" HP: {foe.current_health}/{foe.max_health}\n")
        # --Critical hit--
        elif 100 not in miss_roll and 100 in luck_roll:
            damage_randomness *= 3
            foe.current_health = round(foe.current_health - damage_randomness)
            print(f"You luckily {random.choice(you.attacks)} {foe.name} for {damage_randomness} damage."
                  f" HP: {foe.current_health}/{foe.max_health}\n")
        # --Normal hit--
        elif 100 not in miss_roll and 100 not in luck_roll:
            foe.current_health = round(foe.current_health - damage_randomness)
            print(f"{you.name} {random.choice(you.attacks)} {foe.name} for {damage_randomness} damage."
                  f" HP: {foe.current_health}/{foe.max_health}\n")
        victory()
        t.sleep(1)

    def foe_turn():
        damage_randomness = round(foe.strength * random.randint(80, 120) / 100)
        luck_roll = random.sample((range(1, 101)), foe.luck)
        miss_roll = random.sample((range(1, 101)), you.luck)
        # --Dodge--
        if 100 in miss_roll and 100 not in luck_roll:
            print(f"{foe_name_proper} almost {random.choice(foe.attacks)} {you.name}, \n"
                  f"but {you.name} luckily avoided it at just the right time.\n")
        # --Luck cancels dodge--
        elif 100 in miss_roll and 100 in luck_roll:
            you.current_health = round(you.current_health - damage_randomness)
            print(f"{foe_name_proper} nearly {random.choice(foe.attacks)} {you.name} for more damage!"
                  f"As {you.gender} was about to dodge,\n"
                  f"{foe.gender}'s attack still luckily connected, but for normal damage."
                  f" HP: {you.current_health}/{you.max_health}\n")
        # --Critical hit--
        elif 100 not in miss_roll and 100 in luck_roll:
            damage_randomness *= 3
            you.current_health = round(you.current_health - damage_randomness)
            print(
                f"{foe_name_proper} powerfully {random.choice(foe.attacks)} {you.name} for {damage_randomness} damage!"
                f" HP: {you.current_health}/{you.max_health}\n")
        # --Normal hit--
        elif 100 not in miss_roll and 100 not in luck_roll:
            you.current_health = round(you.current_health - damage_randomness)
            print(f"{foe_name_proper} {random.choice(foe.attacks)} {you.name} for {damage_randomness} damage."
                  f" HP: {you.current_health}/{you.max_health}\n")
        defeat()
        t.sleep(1)

    def tactical_turn():
        choice = choice_sequence(intro='Make your next decision.',
                                 choices=['Fight', 'Run'],
                                 results=['F', 'R'])
        # decision = input("What now? 'F' for Fight or 'R' for Run.")
        if choice == 'R':
            from Events import location
            print('\nYou look for the best way of escape...\n')
            foe_turn()
            print('Found it! Time to go.\n')
            return location('Wilds: 1')
        elif choice == 'F':
            print('\n')
            your_turn()

    fight_choice = choice_sequence(
        intro=f"\nYou have encountered {foe.name}! (Lvl: {foe.level}, HP: {foe.current_health})\n",
        choices=['Run away', 'Auto-fight', 'Tactical Fight'],
        results=['Wilds: 1', 'Auto', 'Tactical'])
    if fight_choice == 'Wilds: 1':
        from Events import location
        print('You look for the best route of escape.\n')
        foe_turn()
        print('Found a way out! Time to go.\n')
        return location('Wilds: 1')
    else:
        print(f'You decide to take on {foe.name}.\n')
        auto, turns = True, 0
        if fight_choice == 'Auto':
            auto = True
        elif fight_choice == 'Tactical':
            auto = False
        while True:
            if auto is False:
                if turns == 0:
                    your_turn()
                    foe_turn()
                    turns += 1
                elif turns > 0:
                    tactical_turn()
                    foe_turn()
                    turns += 1
            else:
                if auto is True:
                    your_turn()
                    foe_turn()
    # print(f"\nYou have encountered {foe.name}! (Lvl: {foe.level}, HP: {foe.current_health})\n")
    # run_or_fight = input("Do you wish to fight, or run away? Type 'F' for Fight or 'R' for Run.\n")
    # if run_or_fight.upper() == 'R':
    #     from Events import location
    #     print('You look for the best route of escape.\n')
    #     foe_turn()
    #     print('Found a way out! Time to go.\n')
    #     location('e')
    # if run_or_fight.upper() == 'F':
    #     print(f'You decide to take on {foe.name}.\n')
    #     auto_or_turn_based = input("Auto fight? 'Y' or 'N'.\n")
    #     if auto_or_turn_based.upper() == 'Y':
    #         auto = True
    #         # print('You will automatically attack your foe throughout the battle.')
    #     elif auto_or_turn_based.upper() == 'N':
    #         auto = False
    #         # print('You will approach this battle a bit more tactically.')
    #     else:
    #         auto = False
    #         print("You did not type 'Y' or 'N'. I will choose 'N' for you.")
    # t.sleep(1)
    # The fight loop
    # turns = 0
    # while True:
    #     if auto is False:
    #         if turns == 0:
    #             your_turn()
    #             foe_turn()
    #             turns += 1
    #         elif turns > 0:
    #             tactical_turn()
    #             foe_turn()
    #             turns += 1
    #     else:
    #         if auto is True:
    #             your_turn()
    #             foe_turn()


# Function created for shortened form of what is seen below
def battle(foe):
    return fight(Enemies.enemy_creation(foe))
