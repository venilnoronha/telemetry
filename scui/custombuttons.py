__author__ = 'paul'
from kivy.uix.button import Button
from kivy.graphics import Color
#static vars for colors
safecol = [0,1,0,1]
dangercol = [1,0,0,1]
cautioncol = [1,1,0,1]

class QuickViewButton(Button):

    def __init__(self, datamodel):
        #python inheritance syntax is so wonky...
        super(Button, self).__init__(size_hint=(.3, None))
        self.datam = datamodel
        self.text = self.getPrettyText()
        self.halign = 'center'
        self.background_color=safecol
        self.markup = True
        return

    def getPrettyText(self):
        return self.datam.name+'\n[b]'+self.datam.getQuickText()+'[/b]'