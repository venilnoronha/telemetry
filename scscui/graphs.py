__author__ = 'paul'
from math import sin
from graphlib import Graph, MeshLinePlot
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random
from modelpy.connector import SolarCarConnector
from modelpy import datalist




class GraphView(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self,orientation='vertical')
        gobj = SingleUnitPlot(datalist["cabintemp"])
        gobj2 = SingleUnitPlot(datalist["cabintemp"])
        self.add_widget(gobj.graphobj)
        self.add_widget(gobj2.graphobj)
        self.graphtestvar = 0
        #i'm commenting these out for now.
        #connect= SolarCarConnector()
        #connect.startserv()
        return


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

class SingleUnitPlot:
    '''
    I decided to make this class HAVE a Graph obj instead of BE a Graph...
    '''
    minwidth = 10#seconds
    def __init__(self, datamodel):
        self.datas = [datamodel]
        self.testdata = [(x, sin(x / 10.)) for x in range(0, 101)]#fortesting
        self.graphobj = Graph(x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=0, ymax=100)
        self.graphobj.xlabel = 'Time'
        self.graphobj.ylabel = datamodel.unittype
        self.unittype=datamodel.unittype

        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = self.testdata
        self.graphobj.add_plot(plot)
        return

    def checkUnitType(self, unittype):
        return unittype == self.unittype

    def checkModelAlreadyViewing(self, datamodel):
        return datamodel in self.datas #not sure if this will check pointer or values...hopefully pointers.

    def addModel(self, datamodel):
        return

    def removeModel(self, datamodel):
        return