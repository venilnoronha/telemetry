__author__ = 'paul'
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from scui.quickview import Quickview
from scui.graphs import GraphView

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