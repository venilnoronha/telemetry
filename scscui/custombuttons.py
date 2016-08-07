__author__ = 'paul'
from kivy.uix.button import Button
from modelpy.model import *
from modelpy import colorlist

#static vars for colors
safecol = [0,1,0,1]
clicksafecol=[0,.7,0,1]
dangercol = [1,0,0,1]
clickdangercol=[.7,0,0,1]

cautioncol1 = [0.5,1,0,1]
clickcautioncol1=[.2,.7,0,1]
cautioncol2 = [1,1,0,1]
clickcautioncol2=[.7,.7,0,1]
cautioncol3 = [1,0.5,0,1]
clickcautioncol3=[.7,.2,0,1]

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
        print('Creating button')
        print(self.datam.name)
        print(colorlist[self.datam.name])

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
            self.background_color = self.getColor()


            
        else:
            print('Set to true')
            #list=[[self.getColor()],[-50,-50,-50,-50]]
            #self.background_color=[(sum(x) for x in zip(*list))]
            self.datam.setIsSelected(True)
            self.background_color = self.getColor()

            #print self.datam.name


        pass

    def getPrettyText(self):
        self.color = colorlist[self.datam.name]
        return self.datam.name+'\n[b]'+self.datam.getQuickText()+'[/b]'

    def getColor(self):
        zone = self.datam.getHazardRanges().currentRange(self.datam.val)
        if(self.datam.getIsSelected()==False):
            if(zone == HazardZone.SAFE):
                return safecol
            elif (zone == HazardZone.WARN1):
                return cautioncol1
            elif (zone == HazardZone.WARN2):
                return cautioncol2
            elif (zone == HazardZone.WARN3):
                return cautioncol3
            else:
                return dangercol
        else:
            if(zone == HazardZone.SAFE):
                return clicksafecol
            elif (zone == HazardZone.WARN1):
                return clickcautioncol1
            elif (zone == HazardZone.WARN2):
                return clickcautioncol2
            elif (zone == HazardZone.WARN3):
                return clickcautioncol3
            else:
                return clickdangercol

    def update(self):
        self.text = self.getPrettyText()
        self.background_color=self.getColor()

        pass