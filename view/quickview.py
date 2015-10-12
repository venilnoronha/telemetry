from modelpy.model import *
__author__ = 'paul'
class Quickview:
    """
    defines the class that will give a quick overview of data on the left side of the window.
    should only contain the data's value/unit, and a color for its current status.
    """
    #Setting a initial object to datam first
    def __init__(self, datamodel):

        print("starting view")
