__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty#there's a reference error here, but it's actually fine
#looks like pycharm struggles with referencing cython stuff lol.
from kivy.uix.filechooser import FileChooserIconView

class SimParamEditor(BoxLayout):
    def __init__(self, parentapp, simobj):
        super (SimParamEditor, self).__init__(orientation='vertical')
        self.parentapp = parentapp
        placeholder = Label(text='placeholder')
        self.add_widget(placeholder)


class ParamLoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    def __init__(self):
        super (ParamLoadDialog, self).__init__()
        chooser = FileChooserIconView()
        self.add_widget(chooser)
