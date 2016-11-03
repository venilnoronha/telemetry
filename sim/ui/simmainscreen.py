__author__ = 'paul'
import datetime

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from sim.simulation.simobj import SimulationObject
from simparameditor import ParamLoadDialog
from files.strategyserializeobject import StrategySerializableObject


class SimMainScreen(BoxLayout):
    def __init__(self, parentapp):
        super (SimMainScreen, self).__init__(orientation='vertical')
        self.parentapp = parentapp

        welcometext = Label(text='Solar Car Strategy Simluation', size_hint=(1, .3),font_size=70, )

        self.add_widget(welcometext)

        choices = self.buildChoices()
        self.add_widget(choices)

        pass

    def buildChoices(self):
        choices = BoxLayout(orientation='vertical')
        choices.padding=50
        choices.spacing=20

        simmenu = self.buildSimuMenu
        choices.add_widget(simmenu)

        anamenu = self.buildAnaMenu()
        choices.add_widget(anamenu)

        return choices

    def buildAnaMenu(self):
        choices = BoxLayout(orientation='vertical')
        title = Label(text='Analysis', font_size=50, halign='left',valign='top')
        title.bind(size=title.setter('text_size'))
        choices.add_widget(title)

        strategysection = BoxLayout(orientation='horizontal')
        resultbutton = Button(text='Load a Saved Result')
        resultbutton.bind(on_press=self.resultbuttoncallback)
        strategysection.add_widget(resultbutton)

        choices.add_widget(strategysection)



        return choices

    @property
    def buildSimuMenu(self):
        choices = BoxLayout(orientation='vertical')

        title = Label(text='Simulation',font_size=50, halign='left',valign='top')
        title.bind(size=title.setter('text_size'))
        choices.add_widget(title)

        strategysection = BoxLayout(orientation='horizontal')

        #selectedlabel = Label(text='Selected Strategy:')
        #strategysection.add_widget(selectedlabel)

        loadbutton = Button(text='Edit...')
        loadbutton.bind(on_press=self.loadbuttoncallback)
        strategysection.add_widget(loadbutton)

        choices.add_widget(strategysection)

        startbutton = Button(text='Run Simulation with Strategy')
        startbutton.bind(on_press=self.startbuttoncallback)
        choices.add_widget(startbutton)

        return choices

    def resultbuttoncallback(self, instance):
        print('program should be able to load previous result dumps from disk.')
        return

    def newbuttoncallback(self, instance):
        print('creating a new strategy...')
        teststrat = StrategySerializableObject()
        teststrat.serializeStrategy('testserialize.json')
        self.parentapp.showEditorNew()


    def loadbuttoncallback(self, instance):

        content = ParamLoadDialog(self.loadparam)#load=self.loadparam, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        content.setselfpop(self._popup)
        return

    def startbuttoncallback(self, instance):
        print('starting simulation...')
        simobj = self.runASim()
        self.parentapp.showResult(simobj)
        return

    def loadparam(self, path, filename):
        print('rakesh insert your magic here')

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