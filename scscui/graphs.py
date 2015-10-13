__author__ = 'paul'
from math import sin
from graphlib import Graph, MeshLinePlot
from kivy.uix.gridlayout import GridLayout

class GraphView(GridLayout):
    def __init__(self):
        self.currentrows=1
        GridLayout.__init__(self,rows=self.currentrows,size_hint=(.7, 1))
        self.add_widget(self.getgraph())

    def getgraph(self):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)

        return graph
