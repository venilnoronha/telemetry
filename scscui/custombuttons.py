__author__ = 'paul'
from kivy.uix.button import Button
from modelpy.model import *
#static vars for colors
safecol = [0,1,0,1]
clicksafecol=[0,.7,0,1]
dangercol = [1,0,0,1]
clickdangercol=[.7,0,0,1]
cautioncol = [1,1,0,1]
clickcautioncol=[.7,.7,0,1]

class QuickViewButton(Button):

    def __init__(self, datamodel):
        #python inheritance syntax is so wonky...
        Button.__init__(self)
        self.datam = datamodel
        self.text = self.getPrettyText()
        self.halign = 'center'
        self.background_color=self.getColor()
        self.markup = True
        self.bind(on_press=self.pressed)
        return

    def pressed(self,instance):
        '''key=self.datam.getAssociatedKey()
        print(key)
        print('The button <%s> is being pressed' % instance.text)
        if(datalist[key].getIsSelected()==True):
            print('%s is set to false', key)
            datalist[key].setIsSelected(False)
        else:
            print('%s is set to true', key)
            datalist[key].setIsSelected(True)'''

        if(self.datam.getIsSelected()==True):
            print('Set to false')
            #list=[[self.getColor()],[50,50,50,50]]
            #self.background_color=[(sum(x) for x in zip(*list))]
            self.datam.setIsSelected(False)
        else:
            print('Set to true')
            #list=[[self.getColor()],[-50,-50,-50,-50]]
            #self.background_color=[(sum(x) for x in zip(*list))]
            self.datam.setIsSelected(True)
        pass

    def getPrettyText(self):
        return self.datam.name+'\n[b]'+self.datam.getQuickText()+'[/b]'

    def getColor(self):
        zone = self.datam.getHazardRanges().currentRange(self.datam.val)
        if(self.datam.getIsSelected()==False):
            if(zone == HazardZone.SAFE):
                return safecol
            elif (zone == HazardZone.WARN):
                return cautioncol
            else:
                return dangercol
        else:
            if(zone == HazardZone.SAFE):
                return clicksafecol
            elif (zone == HazardZone.WARN):
                return clickcautioncol
            else:
                return clickdangercol

    def update(self):
        self.text = self.getPrettyText()
        self.background_color=self.getColor()
        pass