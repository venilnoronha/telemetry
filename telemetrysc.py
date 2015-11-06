__author__ = 'paul'
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from scscui.quickview import Quickview
from scscui.graphs import GraphView
from modelpy.connector import SolarCarConnector
import sys

"""
main entry point to our program.
"""
class MyApp(App):
    connect=object;
    def build(self):
        global connect
        mainview = BoxLayout(orientation='horizontal')

        quickviewpanel = Quickview()
        graphviewpanel = GraphView()

        mainview.add_widget(quickviewpanel)
        mainview.add_widget(graphviewpanel)


        #i'm commenting these out for now.
        connect= SolarCarConnector()

        return mainview

    def on_stop(self):
        global connect
        connect.close()
        print("Successfully closed")
        sys.exit();
        #App.stop()

if __name__ == '__main__':
    MyApp().run()