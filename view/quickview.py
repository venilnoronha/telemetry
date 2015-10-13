
__author__ = 'paul'

from kivy.uix.gridlayout import GridLayout
from scui.custombuttons import QuickViewButton
from modelpy import model
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
        ddmodel = model.datalist
        for mod in ddmodel.keys():
            tempbutt = QuickViewButton(ddmodel.get(mod))
            self.add_widget(tempbutt)


