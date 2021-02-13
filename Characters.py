import time as t
import random as r
from Items import *


class Character:
    def __init__(self, level, strength, luck, charisma, current_health, max_health, experience_to_level, current_exp,
                 gold, inventory, name, gender, attacks, weapon, armor, explore_points):
        self.strength = strength
        self.luck = luck
        self.charisma = charisma
        self.current_health = current_health
        self.max_health = max_health
        self.level = level
        self.experience_to_level = experience_to_level
        self.current_exp = current_exp
        self.gold = gold
        self.inventory = inventory
        self.name = name
        self.gender = gender
        self.attacks = attacks
        self.weapon = weapon
        self.armor = armor
        self.explore_points = explore_points

    def current_stats(self):
        ["Your Stats:",
        f"Strength = {self.strength}",
        f"Luck = {self.luck}",
        f"Charisma = {self.charisma}",
        f"Health = {self.current_health}/{self.max_health}"]

    def level_up(self):
        self.max_health += 5
        self.current_health = self.max_health
        self.level += 1
        print(f"\nYour character is now level {self.level}!\n"
              f"You have gained 5 max hitpoints.\n\n")
        t.sleep(3)
        stat_to_increase = input("What stat would you like to increase?\n"
                                 "Type 'S' for Strength, 'L' for Luck, or 'C' for Charisma.\n\n")
        if stat_to_increase.upper() == 'S':
            self.strength += 1
            print(f"You have gained 1 point in strength. You now have {you.strength} strength.\n")
        elif stat_to_increase.upper() == 'L':
            self.luck += 1
            print(f"You have gained 1 point in luck. You now have {you.luck} luck.\n")
        elif stat_to_increase.upper() == 'C':
            self.charisma += 1
            print(f"You have gained 1 point in strength. You now have {you.charisma} charisma.\n")
        self.current_exp -= self.experience_to_level
        self.experience_to_level = round((self.experience_to_level * 1.07) + 5)
        print(f"You currently have {self.current_exp}/{self.experience_to_level} experience needed to level.")


class Enemies:
    def __init__(self, level, strength, luck, charisma, current_health, max_health, exp, gold, items,
                 name, gender, attacks):
        self.strength = strength
        self.luck = luck
        self.charisma = charisma
        self.current_health = current_health
        self.max_health = max_health
        self.level = level
        self.exp = exp
        self.gold = gold
        self.items = items
        self.name = name
        self.gender = gender
        self.attacks = attacks

    def gold_drop(self, odds, amount_range):
        gold_chance = r.sample(range(1, odds), 1)
        if 1 in gold_chance:
            self.gold += r.randint(amount_range[0], amount_range[1])
            return self.gold

    # Enemy Lists
    def enemy_creation(self):
        if self == "field mouse":
            field_mouse = Enemies(level=1, strength=1, luck=3, charisma=5,
                                  max_health=4, current_health=4,
                                  exp=5, gold=0, items=[mouse_tail],
                                  name="a common field mouse", gender="it",
                                  attacks=['bit', 'gnawed'])
            # 1/3 chance (4), 1-2 gold
            Enemies.gold_drop(field_mouse, 4, (1, 2))
            return field_mouse
        if self == "wild hog":
            wild_hog = Enemies(level=3, strength=3, luck=2, charisma=4,
                               max_health=16, current_health=16,
                               exp=15, gold=0, items=[hog_hide],
                               name="a wild hog", gender="it",
                               attacks=['charged', 'stabbed'])
            # 1/3 chance (4), 2-4 gold
            Enemies.gold_drop(wild_hog, 4, (2, 4))
            return wild_hog
        if self == "scrawny wolf":
            scrawny_wolf = Enemies(level=5, strength=4, luck=3, charisma=3,
                                   max_health=25, current_health=25,
                                   exp=25, gold=0, items=[wolf_hide],
                                   name="a scrawny wolf", gender="it",
                                   attacks=['bit', 'chomped', 'charged'])
            # 1/4 chance (5), 4-12 gold
            Enemies.gold_drop(scrawny_wolf, 5, (4, 12))
            return scrawny_wolf


you = Character(strength=1, luck=1, charisma=1,
                current_health=25, max_health=25,
                experience_to_level=25, current_exp=0, level=1,
                gold=0, inventory=[], name="Nathan", gender="M",
                attacks=['punched', 'kicked'],
                weapon=0, armor=0, explore_points=0)
