__author__ = 'paul'
from math import sin
from graphlib import Graph, MeshLinePlot
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random
from modelpy import SolarCarConnector
from modelpy import datalist




class GraphView(BoxLayout):
    def __init__(self):
        self.currentrows=1
        self.data = [(x, sin(x / 10.)) for x in range(0, 101)]
        BoxLayout.__init__(self,orientation='vertical')
        self.graph = self.getgraph()
        self.add_widget(self.graph)
        self.graphtestvar = 0
        connect= SolarCarConnector()
        #connect.startserv()
        return

    def getgraph(self):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-100, ymax=100)
        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = self.data
        graph.add_plot(plot)
        Clock.schedule_interval(self.test, 1 / 30.)
        return graph

    def test(self,*args):
        index = self.graphtestvar % 101
        #self.data[index] = (self.data[index][0],random.random())
        self.data[index] = (self.data[index][0],datalist["cabintemp"].getCurrentVal())
        self.graph.plots[0].points = self.data
        self.graphtestvar += 1
        return

    def handleModel(self, model):
        '''
        :param model: the pointer to the datamodel that we want to respond to (based on the click on a button)
        :return:
        '''
        pass