__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
import datetime
from simobj import SimulationObject
from kivy.uix.button import Button

class SimMainScreen(BoxLayout):
    def __init__(self, parentapp, **kwargs):
        super (SimMainScreen, self).__init__(**kwargs)
        self.parentapp = parentapp

        startbutton = Button(text='Begin Simulation...', font_size=14)


        startbutton.bind(on_press=self.startbuttoncallback)
        self.add_widget(startbutton)
        pass


    def startbuttoncallback(self, instance):
        print('starting simulation...')
        simobj = self.runASim()
        self.parentapp.showResult(simobj)


    def runASim(self):
        racestart = datetime.datetime.today()
        s = SimulationObject('test sim', racestart)
        rv = s.run()
        print('race finished with return message', rv)
        return s