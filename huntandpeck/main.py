#!/usr/bin/env python2.7

import os
import random

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class HuntAndPeck(BoxLayout):
    the_label = ObjectProperty(None)
    the_textbox = ObjectProperty(None)

    def start_typing(self):
        ''' Initializes the typing process, resets in case of already typing.
        '''
        # Start by killing any existing clocks or they double up
        Clock.unschedule(self._type_next_letter)
        # Clear the label
        self.the_label.text = ''
        # Reset the starting position
        self.string_pos = 0
        # Save the text in a string in case it is changed while typing
        self.type_this = self.the_textbox.text
        # Start the actual typing
        self._type_next_letter()

    def abort_typing(self):
        ''' Stop any typing that is currently happening
        '''
        Clock.unschedule(self._type_next_letter)

    def _type_next_letter(self, dt=0):
        ''' Types the next letter and plays a typewriter sound.
        '''
        # Play the sound
        snd = SoundLoader.load(os.path.join('media',
                                            '9098__ddohler__typewriter.wav'))
        snd.play()
        # Append the next letter
        self.the_label.text += self.type_this[self.string_pos]
        # Advance the position
        self.string_pos += 1
        # If there are more letters, schedule the next one at a random time
        # between 0.25 and 0.75 seconds from now.
        if self.string_pos < len(self.type_this):
            Clock.schedule_once(self._type_next_letter,
                                random.uniform(0.25, 0.75))


class HuntAndPeckApp(App):
    def build(self):
        return HuntAndPeck()


if __name__ == '__main__':
    HuntAndPeckApp().run()
