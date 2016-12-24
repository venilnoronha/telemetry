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
from kivy.uix.button import Button
from telemetry.scscui.quickview import Quickview
from telemetry.scscui.graphs import GraphView
from telemetry.modelpy.connector import SolarCarConnector
from files.telemetrydatadump import datadump
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
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
        outerpanel = BoxLayout(orientation='horizontal')
        outerpanel.add_widget(graphviewpanel)
        buttonspanel = BoxLayout(orientation='vertical',size_hint=(.2,.1))
        savebutton = Button(text='save data')
        savebutton.bind(on_press=self.dump)
        buttonspanel.add_widget(savebutton)
        outerpanel.add_widget(buttonspanel)
        th1.content = outerpanel
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
        self.connectbutton = Button(size_hint=(.15, .05),pos_hint={'x': .88, 'y': .93})
        self.connecticon=Image(source="../img/disconnected.png", size_hint=(.05, .04),pos_hint={'x': .94, 'y': .94})
        self.condropdown = DropDown()

        autobut = Button(text='Automatic', size_hint_y=None, height=44)
        autobut.bind(on_press=self.autoLookIP)
        custombut = Button(text='Custom IP...', size_hint_y=None, height=44)
        custombut.bind(on_press=self.makecustomIPPop)
        self.condropdown.add_widget(autobut)
        self.condropdown.add_widget(custombut)
        self.condropdown.bind(on_select=lambda instance, x: setattr(self.connectbutton, 'text', x))
        self.connectbutton.bind(on_release=self.condropdown.open)


        self.masterlayout.add_widget(mainview)
        self.masterlayout.add_widget(self.connectbutton)
        self.masterlayout.add_widget(self.connecticon)
        self.connector= SolarCarConnector()
        self.updateEvent=Clock.schedule_interval(self.update, 1/5)
        return self.masterlayout


    def autoLookIP(self, arg):
        #yutong do ur magic here
        self.condropdown.dismiss()
        return

    def connectIP(self, ip):
        #yutong do ur magic here
        print('got ip %s' % ip)
        return

    def makecustomIPPop(self, arg):
        layout = BoxLayout(orientation='horizontal')



        input = TextInput(text='271.0.0.1', size_hint=(.8,1))
        button = Button(text='Connect', size_hint=(.2, 1))

        layout.add_widget(input)
        layout.add_widget(button)

        popup = Popup(title='connect to custom IP', content=layout, auto_dismiss=False,
                      size_hint=(.4,.2))

        # defint a function within a function because i didn't want to keep making global funcs
        def connectlocal(arg):
            ip = input.text
            self.connectIP(ip)
            popup.dismiss()
            return

        button.bind(on_press=connectlocal)
        popup.open()

        self.condropdown.dismiss()

        return


    def dump(self, args):
        d = datadump()
        fileName = 'testtelemetrydump.csv'
        d.exportCSV(fileName)

    def on_stop(self):
        Clock.unschedule(self.updateEvent)
        self.connector.close()
        print("Successfully closed")
        sys.exit()
        #App.stop()

if __name__ == '__main__':
    MyApp().run()