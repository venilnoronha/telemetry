__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from graphlib import Graph, MeshLinePlot


class SimResultScreen(BoxLayout):
    def __init__(self, parentapp, simobj):
        super (SimResultScreen, self).__init__(orientation='vertical')
        self.parentapp = parentapp
        self.showGraph(simobj)

    def showGraph(self, simobj):
        respool = simobj.carmodel.respool
        bat = respool.batteryChargeAh
        g = SimUnitPlot('battery charge', bat)
        self.add_widget(g)
        v = respool.velocityms
        gv = SimUnitPlot('velocity', v)
        self.add_widget(gv)



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

        plot = MeshLinePlot(color=[1,0,0,1])
        plot.points = tempplotdata
        self.add_plot(plot)

        return