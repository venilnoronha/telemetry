__author__ = 'paul'
from modelpy.model import *
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label
"""
main entry point to our program.
"""
class MyApp(App):

    def build(self):
        return Label(text='Hello USC')


if __name__ == '__main__':
    MyApp().run()