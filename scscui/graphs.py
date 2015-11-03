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
        #blue
        white = [1,1,1,1]
        blue = [0,0,255,1]
        yellow = [255,255, 0,1]
        pink = [255,0,255,1]
        green = [0,255,0,1]
        red = [255, 0, 0, 1]
        
        gobj = SingleUnitPlot(datalist["cabintemp"], red)
        #datalist["cabintemp"].setIsSelected(True)
        gobj.addModel(datalist["motorrpm"], white)
        gobj.addModel(datalist["batvolt"], blue)

        gobj.addModel(datalist["solarvolt"], yellow)
        gobj.addModel(datalist["motortemp"], pink)
        gobj.addModel(datalist["batterytemp"], green)

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
    def __init__(self, datamodel, color):

        Graph.__init__(self,x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-100, xmax=0, ymin=0, ymax=100)
        self.xlabel = 'Time'
        self.ylabel = datamodel.unittype
        self.unittype=datamodel.unittype
        self.datas = []
        self.plotdata = []

        self.addModel(datamodel,color)
        return

    def startupdating(self):
        Clock.schedule_interval(self.updatePlots, 1 / 30.)
        return

    def checkUnitType(self, unittype):
        return unittype == self.unittype

    def checkModelAlreadyViewing(self, datamodel):
        return datamodel in self.datas #not sure if this will check pointer or values...hopefully pointers.

    def addModel(self, datamodel, color_):
        self.datas.append(datamodel)
        tempplotdata = self.getPlotDataForModel(datamodel)
        self.plotdata.append(tempplotdata)
        plot = MeshLinePlot(color= color_)
        plot.points = tempplotdata
        self.add_plot(plot)
        return

    def removeModel(self, datamodel):
        self.datas.remove(datamodel)
        tempplotdata = self.getPlotDataForModel(datamodel)
        self.plotdata.remove(tempplotdata)
        self.remove_plot()
        return



    def updatePlots(self,*args):
        for i in range(0,len(self.datas)):
            if (self.datas[i].getIsSelected()):
                updateddata = self.getPlotDataForModel(self.datas[i])
                self.plots[i].points = updateddata
            else:

                self.plots[i].points=[]
        return

    def getPlotDataForModel(self, datamodel):
        hist = list(datamodel.getHistory())
        rv = [((x-len(hist)+1)*datamodel.histtimescale, hist[x]) for x in range(0, len(hist))]
        return rv