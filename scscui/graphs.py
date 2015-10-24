__author__ = 'paul'
from math import sin
from graphlib import Graph, MeshLinePlot
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock, ClockBase
import random

from modelpy import datalist




class GraphView(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self,orientation='vertical')
        gobj = SingleUnitPlot(datalist["cabintemp"])
        gobj.addModel(datalist["motortemp"])
        gobj.addModel(datalist["batterytemp"])
        gobj.startupdating()
        #gobj2 = SingleUnitPlot(datalist["cabintemp"])
        self.add_widget(gobj)
        #self.add_widget(gobj2.graphobj)
        self.graphtestvar = 0
        
        return

    def handleModel(self, model):
        '''
        :param model: the pointer to the datamodel that we want to respond to (based on the click on a button)
        :return:
        '''
        pass

class SingleUnitPlot(Graph):
    minwidth = 10#seconds
    def __init__(self, datamodel):

        Graph.__init__(self,x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-100, xmax=0, ymin=0, ymax=100)
        self.xlabel = 'Time'
        self.ylabel = datamodel.unittype
        self.unittype=datamodel.unittype
        self.datas = []
        self.plotdata = []
        self.addModel(datamodel)
        return

    def startupdating(self):
        Clock.schedule_interval(self.updatePlots, 1 / 30.)
        return

    def checkUnitType(self, unittype):
        return unittype == self.unittype

    def checkModelAlreadyViewing(self, datamodel):
        return datamodel in self.datas #not sure if this will check pointer or values...hopefully pointers.

    def addModel(self, datamodel):
        self.datas.append(datamodel)
        tempplotdata = self.getPlotDataForModel(datamodel)
        self.plotdata.append(tempplotdata)
        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = tempplotdata
        self.add_plot(plot)
        return

    def removeModel(self, datamodel):
        return



    def updatePlots(self,*args):
        for i in range(0,len(self.datas)):
            updateddata = self.getPlotDataForModel(self.datas[i])
            self.plots[i].points = updateddata
        return

    def getPlotDataForModel(self, datamodel):
        hist = list(datamodel.getHistory())
        rv = [((x-len(hist)+1)*datamodel.histtimescale, hist[x]) for x in range(0, len(hist))]
        return rv