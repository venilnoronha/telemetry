__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from graphlib import Graph, MeshLinePlot


class SimResultScreen(BoxLayout):
    def __init__(self, parentapp, simobj, **kwargs):
        super (SimResultScreen, self).__init__(**kwargs)
        self.parentapp = parentapp
        self.showGraph(simobj)

    def showGraph(self, simobj):
            respool = simobj.carmodel.respool
            bat = respool.batteryChargeAh
            g = SimUnitPlot('test', bat)
            self.add_widget(g)



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