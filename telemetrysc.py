__author__ = 'paul'
from modelpy.model import *
import kivy
kivy.require('1.0.6')

from math import sin
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from view.quickview import Quickview
from view.graphs import GraphView

"""
main entry point to our program.
"""
class MyApp(App):

    def build(self):
        mainview = BoxLayout(orientation='horizontal')
        quickviewpanel = Quickview()
        graphviewpanel = GraphView()
        mainview.add_widget(quickviewpanel)
        mainview.add_widget(graphviewpanel)
        return mainview


if __name__ == '__main__':
    MyApp().run()