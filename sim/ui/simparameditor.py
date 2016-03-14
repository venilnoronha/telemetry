__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty#there's a reference error here, but it's actually fine
#looks like pycharm struggles with referencing cython stuff lol.
from kivy.uix.filechooser import FileChooserIconView

class SimParamEditor(BoxLayout):
    def __init__(self, parentapp, simobj):
        super (SimParamEditor, self).__init__(orientation='vertical')
        self.parentapp = parentapp
        placeholder = Label(text='placeholder')
        self.add_widget(placeholder)


class ParamLoadDialog(BoxLayout):

    def __init__(self, loadaction):
        super (ParamLoadDialog, self).__init__(orientation='vertical')
        self.chooser = FileChooserIconView(size=self.size, pos=self.pos, size_hint=(1.0,0.9))
        self.loadaction = loadaction
        buttonslayout = BoxLayout(orientation='horizontal', size_hint=(1.0,0.1))
        openbutton = Button(text='Open')
        cancelbutton = Button(text='Cancel')

        openbutton.bind(on_press=self.openbehavior)
        cancelbutton.bind(on_press=self.cancelbehavior)

        buttonslayout.add_widget(cancelbutton)
        buttonslayout.add_widget(openbutton)

        self.add_widget(self.chooser)
        self.add_widget(buttonslayout)

    def setselfpop(self, pop):
        self.mypop = pop

    def openbehavior(self,instance):
        self.loadaction(self.chooser.path, self.chooser.selection)


    def cancelbehavior(self,instance):
        self.mypop.dismiss()