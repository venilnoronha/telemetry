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
    pass;


class AllTheData:
    """
    This class simply contains a list of all the data models we'll be looking for in the program.
    """
    #this is a static variable. if you wanted a object specific variable, you declare it in init
    datalist = {    'cabintemp':    TemperatureModel('Cabin Temp'),
                    'motortemp':    TemperatureModel('Motor Temp'),
                    'batterytemp':  TemperatureModel('Battery Temp')
                    #etc
                }

    @classmethod
    def get(cls, dataname):
        """
        should return the POINTER to the model objects.
        this means if you edit the values within it, it will retain the change.
        :param dataname: name of the data you're trying to access
        :return: pointer to data model
        """
        return cls.datalist.get(dataname, default=None)