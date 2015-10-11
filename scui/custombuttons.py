__author__ = 'paul'
from kivy.uix.button import Button
from kivy.graphics import Color
#static vars for colors
safecol = [0,1,0,1]
dangercol = [1,0,0,1]
cautioncol = [1,1,0,1]

class QuickViewButton(Button):

    def __init__(self):
        #python inheritance syntax is so wonky...
        super(Button, self).__init__(text='quickview', size_hint=(.3, None), height=64)
        self.background_color=safecol
        return
