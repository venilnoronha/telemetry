__author__ = 'paul'
class SuperDataModel:
    """
    base class for all the data that we'll be displaying.
    """
    def __init__(self, name):
        self.name = name
        self.unit = 'Undef'
        self.val = float("-inf")
        return
    def getCurrentVal(self):
        return self.val

    def getUnit(self):
        return self.unit

    def getHistory(self):
        return None;

    def getHazardRanges(self):
        return None;

    def getQuickText(self):
        return str(self.val) + ' ' + str(self.unit)

class TemperatureModel(SuperDataModel):
    """
    temperature readings
    """
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        self.unit = 'C'
        return


"""
    This class simply contains a list of all the data models we'll be looking for in the program.
    """
# this is a static variable. if you wanted a object specific variable, you declare it in init
datalist = {'cabintemp': TemperatureModel('Cabin Temp'),
            'motortemp': TemperatureModel('Motor Temp'),
            'batterytemp': TemperatureModel('Battery Temp')
            #etc
            };

class SolarCarConnector:
    """
    this class handles actually making a connection to the simulation or the actual microprocessor.
    """

    def __init__(self, addr):
        self.socketaddr = addr
        pass

    def startserv(self, pollrate):
        '''
        should attempt to establish a connection and spin off a new thread that polls every @pollrate miliseconds(or something)
        do whatever necessary for when you can't establish a connection...
        do NOT block the main UI with this.
        :return:
        '''
        pass

    def poll(self):
        '''
        grr...idk how to make private methods...
        should be called within thread in startserv
        :return:
        '''
        pass

    def parsemessage(self, msg):
        pass

    def updateModel(self):
        '''

        :return:
        '''
        pass