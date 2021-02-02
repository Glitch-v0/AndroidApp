import random as r

# Consumables
soothing_salve = {'soothing salve': 1 / 3}
balm_of_gilead = {'healing touch': 2 / 3}
cup_overflows = {'my cup overflows': 1}
# consumable_dict = {soothing_salve, balm_of_gilead, cup_overflows}

# Weapons
branch = 2
dull_axe = 4
regular_axe = 8
sharpened_axe = 12
# weapon_dict = {branch, dull_axe, regular_axe, sharpened_axe}

# Armor
hog_leather = 2
reinforced_hog = 4


# armor_dict = {hog_leather, reinforced_hog}


class Crafting_Items:
    def __init__(self, name, description, value, rarity, quantity):
        self.name = name
        self.description = description
        self.value = value
        self.rarity = rarity
        self.quantity = quantity

    def __str__(self):
        print(f'{self.quantity} {self.name}')



mouse_tail = Crafting_Items(
    name='mouse tail',
    description='A bendable, thin, generally gross attachment located near the rear end of a mouse.',
    value=1,
    rarity=1,
    quantity=1)

hog_hide = Crafting_Items(
    name='hog hide',
    description='The thick skin of a hog may be able to provide valuable defensive properties.',
    value=3,
    rarity=1 / 2,
    quantity=1)

wolf_hide = Crafting_Items(
    name='wolf hide',
    description=" A wolf's furry hide has value both in defending from attacks and bolstering your presence.",
    value=3,
    rarity=1 / 2,
    quantity=1)
