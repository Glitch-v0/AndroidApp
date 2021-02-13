from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock, ClockEvent
from kivy.core.window import Window
import random
import sys
import time as t
from Characters import *
from Events import *
from Fight_Sequence import *


class GameScreen(Widget):
    pass


class AdventureText(App):
    stats = StringProperty(f'STR: {you.strength}\nCHA: {you.charisma}\nLUC: {you.luck}')
    health = StringProperty(f'HP:\n{you.current_health}/{you.max_health}')
    experience = StringProperty(f'EXP:\n{you.current_exp}/{you.experience_to_level}')
    story = StringProperty('')
    temp_list = []
    choice = ''

    def story_chugger(self, text_list):

        def list_mover(*args):
            for section in text_list:
                # print(f'TEXT LIST: {text_list} is type {type(text_list)}')
                # print(f'MAIN SECTION:\n {section} is type {type(section)}')
                # for actual_section in section:
                #print(f'SUB SECTION:\n {actual_section} is type {type(actual_section)}')
                self.temp_list.append(section)
            print(f'TEMP LIST: {self.temp_list}')
        # Schedules the list printer to print everything in the list, after a specified duration
        list_mover()

        def print_first_item(*args):
            def recursion(*args):
                self.story = self.story[0:-14]
                self.temp_list.remove(first_item)
                if len(self.temp_list) > 0:
                    Clock.schedule_once(print_first_item, 0.3)
            if len(self.temp_list) == 0:
                return
                # if final_function is not None:
                #     return final_function()
            first_item = self.temp_list[0]
            #print(f'List is {self.temp_list}')
            #print(f'First item is: {first_item}')
            self.choice_sequence_function_results(
                intro=first_item,
                choices=['Continue'],
                result_functions=[recursion],
                result_text=[''])

        print_first_item()

    def button_choice(self, button):
        # self.story += f'You chose {button.text}\n'
        self.choice = button.text

        def reset(*args):
            self.choice = ''

        Clock.schedule_once(reset, 1 / 3)
        #print(self.choice)

    def choice_sequence_function_results(self, intro, choices, result_functions, result_text):
        self.story += intro
        number_of_choices = len(choices)
        # print(f'There are {number_of_choices} choices')
        valid_inputs = []
        for i in range(1, number_of_choices + 1):
            self.story += f"\n'{i}': {choices[i - 1]}"
            # print(f'Adding {choices[i-1]} to screen')
            valid_inputs.append(str(i))
        self.story += '\n'

        def wait_for_choice(*args):
            if self.choice not in valid_inputs:
                # print(f'Waiting on a choice between 1 and {number_of_choices}')

                def reset():
                    Clock.schedule_once(wait_for_choice, 1 / 3)

                reset()
            elif self.choice in valid_inputs:
                position = int(self.choice) - 1
                self.story += f'{result_text[position]}'
                result = result_functions[position]
                return result()

        Clock.schedule_once(wait_for_choice, 1 / 3)

    def choice_sequence_basic(self, intro, choices=['Press 1 to continue']):
        self.story += intro
        number_of_choices = len(choices)
        # print(f'There are {number_of_choices} choices')
        valid_inputs = []
        # Puts the choice codes on the screen
        for i in range(1, number_of_choices + 1):
            self.story += f"\n'{i}': {choices[i - 1]}"
            # print(f'Adding {choices[i-1]} to screen')
            valid_inputs.append(str(i))
        self.story += '\n'

        # A sequence regularly called to wait for player choice
        def wait_for_choice(*args):
            if self.choice not in valid_inputs:
                # print(f'Waiting on a choice between 1 and {number_of_choices}')

                def reset():
                    return Clock.schedule_once(wait_for_choice, 1 / 3)

                reset()
            elif self.choice in valid_inputs:
                return

        Clock.schedule_once(wait_for_choice)

    def save_or_load(self, *args):
        return self.choice_sequence_function_results(
            intro='Would you like to load a save?',
            choices=['Yes', 'No'],
            result_functions=[load_save, next_step],
            result_text=[f'Save loaded: {you.name}\n'
                         f'Strength: {you.strength}\n'
                         f'Luck: {you.luck}\n'
                         f'Charisma: {you.charisma}\n'
                         f'HP: {you.current_health}/{you.max_health}\n',
                         'Starting a new game...'])

    def build(self):
        self.save_or_load()
        return GameScreen()


if __name__ == '__main__':
    AdventureText().run()