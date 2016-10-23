__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from graphlib import Graph, MeshLinePlot
from telemetry.modelpy import datalist
from telemetry.modelpy import colorlist
from files.configs import GraphUnitConfig


class GraphView(BoxLayout):
    temperaturePlot=object
    gobj2=object
    gobj3=object
    
    def __init__(self):
        BoxLayout.__init__(self,orientation='vertical')
        #blue
        self.tempUnitConfig = GraphUnitConfig()
        self.voltUnitConfig = GraphUnitConfig()
        self.rpmUnitConfig = GraphUnitConfig()
        self.tempUnitConfig.deserializeConfig('../config/TemperatureGraphUnit.cfg')
        self.voltUnitConfig.deserializeConfig('../config/VoltageGraphUnit.cfg')
        self.rpmUnitConfig.deserializeConfig('../config/RPMGraphUnit.cfg')

        self.temperaturePlot = SingleUnitPlot(datalist["cabintemp"], colorlist["Cabin Temp"], self.tempUnitConfig)
        #datalist["cabintemp"].setIsSelected(True)
        self.gobj2 = SingleUnitPlot(datalist["batvolt"], colorlist["Battery Volt"], self.voltUnitConfig)
        self.gobj3 = SingleUnitPlot(datalist["motorrpm"], colorlist["Motor RPM"],self.rpmUnitConfig)
        self.temperaturePlot.addModel(datalist["motortemp"], colorlist["Motor Temp"])
        self.temperaturePlot.addModel(datalist["batterytemp"], colorlist["Battery Temp"])
        self.gobj2.addModel(datalist["solarvolt"], colorlist["Solar Volt"])

        self.temperaturePlot.startupdating()
        self.gobj2.startupdating()
        self.gobj3.startupdating()
        #gobj2 = SingleUnitPlot(datalist["cabintemp"])

        #self.add_widget(gobj2.graphobj)
        self.startupdating()
        self.graphtestvar = 0

        return

    def handleModel(self, model):
        '''
        :param model: the pointer to the datamodel that we want to respond to (based on the click on a button)
        :return:
        '''
        pass

    def startupdating(self):
        Clock.schedule_interval(self.checkPlots, 1/60)
        return

    def checkPlots(self, *args):
        if(self.temperaturePlot.hasPlot()):
            if(not self.temperaturePlot.getIsPlotted()):
                print('added gobj1')
                self.add_widget(self.temperaturePlot)
                self.temperaturePlot.setIsPlotted(True)
        else:
            if(self.temperaturePlot.getIsPlotted()):
                self.remove_widget(self.temperaturePlot)
                self.temperaturePlot.setIsPlotted(False)

        if(self.gobj2.hasPlot()):
            if(not self.gobj2.getIsPlotted()):
                print('added gobj2')
                self.add_widget(self.gobj2)
                self.gobj2.setIsPlotted(True)
        else:
            if(self.gobj2.getIsPlotted()):
                self.remove_widget(self.gobj2)
                self.gobj2.setIsPlotted(False)

        if(self.gobj3.hasPlot()):
            if(not self.gobj3.getIsPlotted()):
                print('added gobj3')
                self.add_widget(self.gobj3)
                self.gobj3.setIsPlotted(True)
        else:
            if(self.gobj3.getIsPlotted()):
                self.remove_widget(self.gobj3)
                self.gobj3.setIsPlotted(False)

class SingleUnitPlot(Graph):
    minwidth = 10#seconds
    numPlots=0
    isPlotted=False
    def __init__(self, datamodel, color, unitconfig):

        Graph.__init__(self,x_ticks_minor=5,
        x_ticks_major=25, y_ticks_minor=unitconfig.grid_ticks_minor, y_ticks_major=unitconfig.grid_ticks_major,
        y_grid_label=unitconfig.grid_label, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-50, xmax=50, ymin=unitconfig.startmin, ymax=unitconfig.startmax)
        self.xlabel = 'Time'
        self.ylabel = unitconfig.unitname
        self.unittype=datamodel.unittype
        self.dataModels = []
        self.plotdata = []
        self.addModel(datamodel,color)
        return

    def hasPlot(self):
        if(self.numPlots!=0):
            return True
        else:
            return False

    def setIsPlotted(self,bool):
        self.isPlotted=bool

    def getIsPlotted(self):
        return self.isPlotted

    def startupdating(self):
        Clock.schedule_interval(self.updatePlots, 1 / 20.)
        return

    def checkUnitType(self, unittype):
        return unittype == self.unittype

    def checkModelAlreadyViewing(self, datamodel):
        return datamodel in self.dataModels

    def addModel(self, datamodel, color_):
        self.dataModels.append(datamodel)
        tempplotdata = self.getPlotDataForModel(datamodel)
        self.plotdata.append(tempplotdata)
        plot = MeshLinePlot(color= color_)
        plot.points = tempplotdata
        self.add_plot(plot)
        return

    def removeModel(self, datamodel):
        self.dataModels.remove(datamodel)
        tempplotdata = self.getPlotDataForModel(datamodel)
        self.plotdata.remove(tempplotdata)
        self.remove_plot()
        return



    def updatePlots(self,*args):
        counter=0
        for i in range(0,len(self.dataModels)):
            if (self.dataModels[i].getIsSelected()):
                updateddata = self.getPlotDataForModel(self.dataModels[i])
                self.plots[i].points = updateddata
                counter+=1
            else:
                self.plots[i].points=[]
        self.numPlots=counter
        return

    def getPlotDataForModel(self, datamodel):
        hist = list(datamodel.getHistory())
        rv = [((x-len(hist)+1)*datamodel.histtimescale, hist[x]) for x in range(0, len(hist))]
        return rv