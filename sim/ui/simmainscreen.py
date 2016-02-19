__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
import datetime
from sim.simobj import SimulationObject
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from simparameditor import ParamLoadDialog

class SimMainScreen(BoxLayout):
    def __init__(self, parentapp):
        super (SimMainScreen, self).__init__(orientation='vertical')
        self.parentapp = parentapp

        welcometext = Label(text='Welcome to SC/SC Simluation')
        self.add_widget(welcometext)

        choices = self.buildChoices()
        self.add_widget(choices)
        pass

    def buildChoices(self):
        choices = BoxLayout(orientation='horizontal')
        choices.padding=50
        choices.spacing=20

        loadbutton = Button(text='Load a Plan...')
        loadbutton.bind(on_press=self.loadbuttoncallback)
        choices.add_widget(loadbutton)

        startbutton = Button(text='DEBUG: Run It!', font_size=14)
        startbutton.bind(on_press=self.startbuttoncallback)
        choices.add_widget(startbutton)


        resultbutton = Button(text='Load a Saved Result...', font_size=14)
        resultbutton.bind(on_press=self.resultbuttoncallback)
        choices.add_widget(resultbutton)
        return choices

    def resultbuttoncallback(self, instance):
        print('program should be able to load previous result dumps from disk.')
        return

    def loadbuttoncallback(self, instance):
        print('rakesh insert your magic here')
        content = ParamLoadDialog()#load=self.loadparam, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        return

    def startbuttoncallback(self, instance):
        print('starting simulation...')
        simobj = self.runASim()
        self.parentapp.showResult(simobj)
        return

    def loadparam(self, path, filename):
        print('we got a load')
        return

    def dismiss_popup(self):
        self._popup.dismiss()
        return

    def runASim(self):
        racestart = datetime.datetime.today()
        s = SimulationObject('test sim', racestart)
        rv = s.run()
        print('race finished with return message', rv)
        return s