import time as t

from Characters import you

shopkeeper = False


def explore_chungus(points):
    if points == 0:
        print('You look around, trying to find something useful...\n')
        t.sleep(3)
        print('You find a sturdy branch. This could make for a basic weapon.')
        from Items import branch

        you.weapon = branch
        print(f'Your combined strength: {you.strength + you.weapon}\n')
    if points == 1:
        print('You notice a smoke column off in the distance.\n'
              'If you pursue it, you may find someone or something.\n')
    if points == 2:
        print('Using the smoke column like a compass, you find yourself getting closer and closer.\n')
        t.sleep(3)
        print('With each step, your anticipation of the unknown grows.\n')
        t.sleep(3)
        print('You hear a hammering sound, as of someone hitting metal.\n'
              'You find the end of where the trail has led you: well-kept shack.'
              'A furnance periodically spews smoke into the air. You hear a man coughing.\n')
        print('You knock on the door. Slence.\n')
        t.sleep(3)
        print('You knock again. The door slowly creaks open, and you see a bow pointed at your face.\n')
        print("Unknown man: Who are you?\n")
        t.sleep(2)
        print(f"You: I'm {you.name}. Please don't shoot.\n")
        t.sleep(2)
        print("Unknown man:'Why are you here?")
        t.sleep(2)
        print(f"You:'I've been exploring, and hoping I could find help by coming here.'\n")
        t.sleep(2)
        print("Unknown man:'Look, trust doesn't come easy around here."
              "I've got enough problems to deal with at the moment.\n")
        t.sleep(2)
        print(f"You: Maybe I can help. What is going on?\n")
        t.sleep(2)
        print('The stranger lowers his bow.\n'
              "Unknown man: I've been having mice terrorize my crops for weeks now.\n")
        t.sleep(2)
        print('Unknown man: I am worried that food is going to start becoming scarce.\n'
              'Go hunt some mice for me to reduce their population.\n')
        t.sleep(2)
        print("Bring me 5 mouse tails as proof of your work. Then I'll consider helping you.\n")

