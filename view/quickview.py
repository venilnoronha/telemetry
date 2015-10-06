from modelpy.model import *
__author__ = 'paul'
class Quickview:
    """
    defines the class that will give a quick overview of data on the left side of the window.
    should only contain the data's value/unit, and a color for its current status.
    """
    #Setting a initial object to datam first
    datam = SuperDataModel();
    def __init__(self):
        print("starting view")
