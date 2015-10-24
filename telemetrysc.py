__author__ = 'paul'
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from scscui.quickview import Quickview
from scscui.graphs import GraphView
from modelpy.connector import SolarCarConnector

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

        #i'm commenting these out for now.
        connect= SolarCarConnector()

        return mainview


if __name__ == '__main__':
    MyApp().run()