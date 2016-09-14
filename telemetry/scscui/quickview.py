
__author__ = 'paul'

from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

from telemetry.scscui.custombuttons import QuickViewButton
from telemetry.modelpy import model


class Quickview(GridLayout):
    """
    defines the class that will give a quick overview of data on the left side of the window.
    should only contain the data's value/unit, and a color for its current status.
    """


    def __init__(self):
        buttonpadding = 10
        quickviewcols = 2
        GridLayout.__init__(self,cols=quickviewcols,size_hint=(.3, 1))
        self.padding=[buttonpadding,buttonpadding,buttonpadding,buttonpadding]
        self.allbuttons = []
        ddmodel = model.datalist
        for mod in ddmodel.keys():
            tempbutt = QuickViewButton(ddmodel.get(mod))
            self.add_widget(tempbutt)
            self.allbuttons.append(tempbutt)
        self.setupUpdateThread()

    def setupUpdateThread(self):
        Clock.schedule_interval(self.update, 1 / 30.)
        return

    def update(self,*args):
        for button in self.allbuttons:
            button.update()
        return