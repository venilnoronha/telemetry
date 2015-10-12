__author__ = 'paul'
from modelpy.model import *
import kivy
kivy.require('1.0.6')

from math import sin
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from scui.custombuttons import QuickViewButton
from graphlib import Graph, MeshLinePlot
from modelpy import model
"""
main entry point to our program.
"""
class MyApp(App):

    def build(self):
        graphratio = .7
        buttonpadding = 10
        quickviewcols = 2

        mainview = BoxLayout(orientation='horizontal')
        quickviewpanel = GridLayout(cols=quickviewcols,size_hint=(1-graphratio, 1))
        quickviewpanel.padding=[buttonpadding,buttonpadding,buttonpadding,buttonpadding]
        ddmodel = model.AllTheData.datalist
        for mod in ddmodel.keys():
            tempbutt = QuickViewButton(ddmodel.get(mod))
            quickviewpanel.add_widget(tempbutt)

        mainview.add_widget(quickviewpanel)
        mainview.add_widget(self.getgraph())
        return mainview

    def getgraph(self):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)

        return graph

if __name__ == '__main__':
    MyApp().run()