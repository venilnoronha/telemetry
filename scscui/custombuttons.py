__author__ = 'paul'
from kivy.uix.button import Button
from modelpy.model import *
#static vars for colors
safecol = [0,1,0,1]
dangercol = [1,0,0,1]
cautioncol = [1,1,0,1]

class QuickViewButton(Button):

    def __init__(self, datamodel):
        #python inheritance syntax is so wonky...
        Button.__init__(self)
        self.datam = datamodel
        self.text = self.getPrettyText()
        self.halign = 'center'
        self.background_color=self.getColor()
        self.markup = True
        return

    def getPrettyText(self):
        return self.datam.name+'\n[b]'+self.datam.getQuickText()+'[/b]'

    def getColor(self):
        zone = self.datam.getHazardRanges().currentRange(self.datam.val)
        if(zone == HazardZone.SAFE):
            return safecol
        elif (zone == HazardZone.WARN):
            return cautioncol
        else:
            return dangercol

    def update(self):
        self.text = self.getPrettyText()
        self.background_color=self.getColor()
        pass