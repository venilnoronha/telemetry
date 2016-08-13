__author__ = 'paul'
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.tabbedpanel import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from scscui.quickview import Quickview
from scscui.graphs import GraphView
from modelpy.connector import SolarCarConnector
import sys

"""
main entry point to our program.
"""

class MyApp(App):
    connecticon=object
    connector=object
    updateEvent=object
    prevConnectionVal=False

    def update(self, *args):
        isConnected=self.connector.connected
        if(self.prevConnectionVal != isConnected):
            self.masterlayout.remove_widget(self.connecticon)
            if self.connector.connected:
                self.connecticon=Image(source="img/connected.png",size_hint=(.05, .04),pos_hint={'x':.94, 'y':.94})
            else:
                self.connecticon=Image(source="img/disconnected.png",size_hint=(.05, .04),pos_hint={'x':.94, 'y':.94})
            self.masterlayout.add_widget(self.connecticon)
            self.prevConnectionVal=isConnected
        pass

    def build(self):
        #global connect
        self.title="SCSCTelemetry1.0"
        self.masterlayout=FloatLayout()
        mainview = BoxLayout(orientation='horizontal',size_hint=(1, .98),pos_hint={'x':0, 'y':0})

        #btn1 = Label(text='Hello', size_hint=(.7, 1))
        quickviewpanel = Quickview()
        graphviewpanel = GraphView()

        mainview.add_widget(quickviewpanel)
       # mainview.add_widget(graphviewpanel)
        '''****************************************************************************************************'''
        tp=TabbedPanel()
        tp.do_default_tab=False

        th1=TabbedPanelHeader(text= 'Graphs')
        th1.content = graphviewpanel
        tp.add_widget(th1)

        th2=TabbedPanelHeader(text='Analytics')
        analysistp=TabbedPanel()
        analysistp.do_default_tab=False
        ath1=TabbedPanelHeader(text='cabintemp')
        ath1.content=Label(text='This is where we will put our data analysis for cabintemp')
        ath2=TabbedPanelHeader(text='motortemp')
        ath2.content=Label(text='This is where we will put our data analysis for motortemp')
        ath3=TabbedPanelHeader(text='batterytemp')
        ath3.content=Label(text='This is where we will put our data analysis for batterytemp')
        ath4=TabbedPanelHeader(text='motorrpm')
        ath4.content=Label(text='This is where we will put our data analysis for motorrpm')
        ath5=TabbedPanelHeader(text='solarvolt')
        ath5.content=Label(text='This is where we will put our data analysis for solarvolt')
        ath6=TabbedPanelHeader(text='batteryvolt')
        ath6.content=Label(text='This is where we will put our data analysis for batteryvolt')
        analysistp.add_widget(ath1)
        analysistp.add_widget(ath2)
        analysistp.add_widget(ath3)
        analysistp.add_widget(ath4)
        analysistp.add_widget(ath5)
        analysistp.add_widget(ath6)
        th2.content = analysistp
        tp.add_widget(th2)

        mainview.add_widget(tp)
        '''****************************************************************************************************'''

        self.connecticon=Image(source="img/disconnected.png",size_hint=(.05, .04),pos_hint={'x':.94, 'y':.94})

        self.masterlayout.add_widget(mainview)
        self.masterlayout.add_widget(self.connecticon)
        self.connector= SolarCarConnector()
        self.updateEvent=Clock.schedule_interval(self.update, 1/5)
        return self.masterlayout

    def on_stop(self):
        Clock.unschedule(self.updateEvent)
        self.connector.close()
        print("Successfully closed")
        sys.exit()
        #App.stop()

if __name__ == '__main__':
    MyApp().run()