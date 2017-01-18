__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from graphlib import Graph, MeshLinePlot
from os.path import dirname, abspath
import files.datadump
import os
from kivy.uix.slider import Slider

class SimResultScreen(BoxLayout):

    def __init__(self, parentapp, simobj):
        MINZOOM = 1;
        MAXZOOM = 10;
        super (SimResultScreen, self).__init__(orientation='vertical')
        self.parentapp = parentapp
        self.simobj = simobj
        self.graphmodule = self.getGraphModule(simobj)
        self.zoomslider = Slider(step=1, orientation='horizontal', min=MINZOOM, max=MAXZOOM, size_hint=(1, .1))
        self.zoomslider.bind(value=self.onZoomSliderChange)
        self.zoomslider.bind(value=self.onZoomVerticalSliderChange)

        self.add_widget(self.graphmodule)
        self.add_widget(self.zoomslider)

        bottombar = BoxLayout(orientation='horizontal',size_hint=(1.0,0.1))
        datadumpbutton = Button(text='Save Result...')
        datadumpbutton.bind(on_press=self.dumpcallback)
        backbutton = Button(text='Back')
        backbutton.bind(on_press=self.backcallback)
        bottombar.add_widget(backbutton)
        bottombar.add_widget(datadumpbutton)
        self.add_widget(bottombar)

    def getGraphModule(self, simobj):
        respool = simobj.carmodel.respool
        bat = respool.batteryChargeAh
        g = SimUnitPlot('battery charge', bat)
        #self.add_widget(g)
        v = respool.velocityms
        gv = SimUnitPlot('velocity', v)
        return g

    def backcallback(self, instance):
        self.parentapp.showStartScreen()

    def dumpcallback(self, instance):
        #should refactor this into simobj.writeoutput or something. UI shouldn't really contain datadumping code, just call into it.
        parentDirectory = dirname(dirname(abspath('__path__')))
        targetDirectory = os.path.join(parentDirectory, "outputData")

        if not os.path.isdir(targetDirectory):
            os.mkdir(targetDirectory)

        data = files.datadump.getCSVData(self.simobj.carmodel.respool)
        files.datadump.dumpdata(os.path.join(targetDirectory, 'testdump.csv'), data)

    def onZoomSliderChange(self, instance, value):
        self.graphmodule.setZoom(value)
        return;

    def onZoomVerticalSliderChange(self, instance, value):
        self.graphmodule.setZoomVertical(value)
        return;


class SimUnitPlot(Graph):
    minwidth = 10#seconds
    numPlots=0
    isPlotted=False
    def __init__(self, title, solarres):
        self.bounds=solarres.getMinMax()
        Graph.__init__(self,
        x_ticks_major=60*60*60*24, y_ticks_major=500000,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=self.bounds[0], xmax=self.bounds[1], ymin=self.bounds[2], ymax=self.bounds[3],
                       width=2000, height=500)
        self.unittype='test'
        tempplotdata = solarres.hist

        plot = MeshLinePlot(color=[1,0,0,1])
        plot.points = tempplotdata
        self.add_plot(plot)

        return


    def getDataMinX(self):
        return self.bounds[0]

    def getDataMaxX(self):
        return self.bounds[1]

    def getDataMinY(self):
        return self.bounds[2]

    def getDataMaxY(self):
        return self.bounds[3]

    def setZoom(self, scalef):
        #just a quick and dirty for now...well need to implement actual xmin/xmax windows and zooms onto middle?
        self.xmax = self.getDataMaxX() / float(scalef)
        return

    def setZoomVertical(self, scalef):
        #just a quick and dirty for now...well need to implement actual xmin/xmax windows and zooms onto middle?
        self.ymax = self.getDataMaxY() / float(scalef)
        return