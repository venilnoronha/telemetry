__author__ = 'paul'
from modelpy.model import *
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from scui.custombuttons import QuickViewButton
"""
main entry point to our program.
"""
class MyApp(App):

    def build(self):
        graphratio = .7

        mainview = BoxLayout(orientation='horizontal')

        tempbutt2 = Button(text='graphview here', size_hint=(graphratio, 1))
        quickviewpanel = StackLayout(size_hint=(1-graphratio, 1))
        quickviewpanel.padding=[15,15,15,15]
        for i in range(12):
            tempbutt = QuickViewButton()
            quickviewpanel.add_widget(tempbutt)

        mainview.add_widget(quickviewpanel)
        mainview.add_widget(tempbutt2)
        return mainview


if __name__ == '__main__':
    MyApp().run()