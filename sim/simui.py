import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from simobj import SimulationObject
import datetime
from graphlib import Graph, MeshLinePlot
import sys

class MyApp(App):
    isConnected=False
    connect=object;
    def build(self):
        global connect
        mainview = BoxLayout(orientation='horizontal')


        startbutton = Button(text='Begin Simulation...', font_size=14)
        def startbuttoncallback(instance):
            print('starting simulation...')
            simobj = self.runASim()
            mainview.remove_widget(startbutton)
            self.showGraph(simobj, mainview)

        startbutton.bind(on_press=startbuttoncallback)
        mainview.add_widget(startbutton)


        return mainview

    def on_stop(self):
        return

    def runASim(self):
        racestart = datetime.datetime.today()
        s = SimulationObject('test sim', racestart)
        rv = s.run()
        print('race finished with return message', rv)
        return s

    def showGraph(self, simobj, view):
        respool = simobj.carmodel.respool
        bat = respool.batteryChargeAh
        g = SimUnitPlot('test', bat)
        view.add_widget(g)



class SimUnitPlot(Graph):
    minwidth = 10#seconds
    numPlots=0
    isPlotted=False
    def __init__(self, title, solarres):
        bounds=solarres.getMinMax()
        Graph.__init__(self,
        x_ticks_major=60*60*60*24, y_ticks_major=500000,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=bounds[0], xmax=bounds[1], ymin=bounds[2], ymax=bounds[3])
        self.unittype='test'
        tempplotdata = solarres.hist

        plot = MeshLinePlot()
        plot.points = tempplotdata
        self.add_plot(plot)

        return

if __name__ == '__main__':
    MyApp().run()
