__author__ = 'paul'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty#there's a reference error here, but it's actually fine
#looks like pycharm struggles with referencing cython stuff lol.
from kivy.uix.filechooser import FileChooserIconView

class SimParamEditor(BoxLayout):
    def __init__(self, parentapp, simobj=None):
        super (SimParamEditor, self).__init__(orientation='vertical')
        self.parentapp = parentapp

        title = Label(text='Solar Car Strategy Editor', size_hint=(1.0, 0.1))
        self.add_widget(title)


        editor = self.constructActualEditor()
        self.add_widget(editor)

        bottombar = BoxLayout(size_hint=(1.0, 0.1))

        mainpagebut = Button(text='Back to Main Page')
        savebut = Button(text='Save Strategy...')
        runbut = Button(text='Run the Simmulation!')

        bottombar.add_widget(mainpagebut)
        bottombar.add_widget(savebut)
        bottombar.add_widget(runbut)

        self.add_widget(bottombar)

    def constructActualEditor(self):
        editor = BoxLayout(orientation='vertical')

        namelabel = Label(text='Name:')
        editor.add_widget(self.constructEditorLine(namelabel,None))

        descriptionlabel = Label(text='Description: ')
        editor.add_widget(self.constructEditorLine(descriptionlabel,None))

        racedistancelabel = Label(text='Race Distance')
        editor.add_widget(self.constructEditorLine(racedistancelabel,None))

        itinerary = Label(text='race itinerary')
        editor.add_widget(self.constructEditorLine(itinerary,None))

        return editor

    def constructEditorLine(self, left, right):
        rv = BoxLayout(orientation='horizontal')
        rv.add_widget(left)
        if(right):
            rv.add_widget(right)
        else:
            placeholder = Label(text='placeholder')
            rv.add_widget(placeholder)
        return rv


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