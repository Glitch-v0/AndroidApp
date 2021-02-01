import time as t
import random as r


class Character:
    def __init__(self, level, strength, luck, charisma, current_health, max_health, experience_to_level, current_exp,
                 gold, items, name, gender, attacks):
        self.strength = strength
        self.luck = luck
        self.charisma = charisma
        self.current_health = current_health
        self.max_health = max_health
        self.level = level
        self.experience_to_level = experience_to_level
        self.current_exp = current_exp
        self.gold = gold
        self.items = items
        self.name = name
        self.gender = gender
        self.attacks = attacks

    def current_stats(self):
        print(f"\nYour Stats:")
        print(f"Strength = {self.strength}")
        print(f"Accuracy = {self.luck}")
        print(f"Evasion = {self.charisma}")
        print(f"Health = {self.current_health}/{self.max_health}")

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

    # Enemy Lists
    def enemy_creation(self):
        if self == "field mouse":
            # 1/3 chance to drop a gold coin
            gold_chance = r.sample(range(1, 4), 1)
            field_mouse = Enemies(level=1, strength=1, luck=2, charisma=5,
                                  max_health=4, current_health=4,
                                  exp=5, gold=0, items="",
                                  name="a common field mouse", gender="it",
                                  attacks=['bit', 'gnawed'])
            if 1 in gold_chance:
                field_mouse.gold += r.randint(1, 2)
            return field_mouse
        if self == "wild hog":
            # 1/3 chance to drop 1-4 gold coins
            gold_chance = r.sample(range(1, 4), 1)
            wild_hog = Enemies(level=3, strength=3, luck=1, charisma=4,
                               max_health=16, current_health=16,
                               exp=15, gold=0, items="",
                               name="a wild hog", gender="it",
                               attacks=['charged', 'stabbed'])
            if 1 in gold_chance:
                wild_hog.gold += r.randint(1, 4)
            return wild_hog


you = Character(strength=1, luck=1, charisma=1,
                current_health=25, max_health=25,
                experience_to_level=25, current_exp=0, level=1,
                gold=0, items="", name="Nathan", gender="M",
                attacks=['punched', 'kicked'])
