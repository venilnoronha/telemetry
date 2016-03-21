import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from simobj import SimulationObject
from ui.simmainscreen import SimMainScreen
from ui.simresultscreen import SimResultScreen
from kivy.uix.popup import Popup

import sys

class MyApp(App):
    isConnected=False
    connect=object;
    def build(self):
        global connect
        self.mainview = BoxLayout(orientation='horizontal')

        startscreen = SimMainScreen(self)
        self.mainview.add_widget(startscreen)


        return self.mainview

    def on_stop(self):
        return

    def showResult(self, simobj):
        self.mainview.clear_widgets()
        resultpage = SimResultScreen(self,simobj)
        self.mainview.add_widget(resultpage)



if __name__ == '__main__':
    MyApp().run()