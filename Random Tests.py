

class CraftingItems:
    def __init__(self, name, description, value, quantity, rarity):
        self.name = name
        self.description = description
        self.value = value
        self.quantity = quantity
        self.rarity = rarity

    def __repr__(self):
        return str(f"{self.quantity} {self.name}")


mouse_tail = CraftingItems(
    name='mouse tail',
    description='A bendable, thin, generally gross attachment located near the rear end of a mouse.',
    value=1,
    quantity=1,
    rarity=1 / 2)

hog_hide = CraftingItems(
    name='hog hide',
    description='The thick skin of a hog may be able to provide valuable defensive properties.',
    value=3,
    quantity=1,
    rarity=1 / 2)

wolf_hide = CraftingItems(
    name='wolf hide',
    description='A wolf hide is both aesthetically pleasing and defensively advantageous',
    value=10,
    quantity=1,
    rarity=1 / 2)


def item_drop(items):
    loot = []
    for item in items:
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



# for i in range(10):
#     item = (item_drop([mouse_tail, hog_hide, wolf_hide]))
#     if item is not None:
#         if item in my_inventory:
#             item.quantity += 1
#         elif item not in my_inventory:
#             my_inventory.append(item)
#     else:
#         print('Item did not drop.')
# for item in my_inventory:
#     print(f'You have {item.quantity} {item.name}s in your inventory.\n'
#           f'Value of each item: {item.value}\n'
#           f'Total value: {item.quantity * item.value}\n')
