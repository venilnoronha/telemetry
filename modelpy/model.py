__author__ = 'paul'




class HazardZone:
    SAFE=0
    WARN1=1
    WARN2=2
    WARN3=3
    DANGER=4

    BOUNDS=[20,40,60,80]
    BOUNDTYPE=0


    DESCENDING=0
    ASCENDING=1
    VALLEY=2
    MOUNTAIN=3

    #def __init__(self, safe=[0,20, 30, 40], warn=[20,30, 40, 60],danger=60):
    def __init__(self, warningranges=[20,40,60,80], boundtype=0):
        self.BOUNDS=warningranges
        self.BOUNDTYPE=boundtype

    def currentRange(self, val):
        '''
        gives the (int) hazard level that something is in given the current value.
        :param val:
        :return:
        '''
        if self.BOUNDTYPE==self.ASCENDING:
            if(val>=self.BOUNDS[3]):
                return self.SAFE
            elif(val>=self.BOUNDS[2]):
                return self.WARN1
            elif(val>=self.BOUNDS[1]):
                return self.WARN2
            elif(val>=self.BOUNDS[0]):
                return self.WARN3
            else:
                return self.DANGER
        elif self.BOUNDTYPE==self.DESCENDING:
            if(val>=self.BOUNDS[3]):
                return self.DANGER
            elif(val>=self.BOUNDS[2]):
                return self.WARN3
            elif(val>=self.BOUNDS[1]):
                return self.WARN2
            elif(val>=self.BOUNDS[0]):
                return self.WARN1
            else:
                return self.SAFE
        elif self.BOUNDTYPE==self.MOUNTAIN:
            if(val>=self.BOUNDS[3]):
                return self.DANGER
            elif(val>=self.BOUNDS[2]):
                return self.WARN2
            elif(val>=self.BOUNDS[1]):
                return self.SAFE
            elif(val>=self.BOUNDS[0]):
                return self.WARN2
            else:
                return self.DANGER
        elif self.BOUNDTYPE==self.VALLEY:
            if(val>=self.BOUNDS[3]):
                return self.SAFE
            elif(val>=self.BOUNDS[2]):
                return self.WARN2
            elif(val>=self.BOUNDS[1]):
                return self.DANGER
            elif(val>=self.BOUNDS[0]):
                return self.WARN2
            else:
                return self.SAFE


from collections import deque

class SuperDataModel:

    """
    base class for all the data that we'll be displaying.
    """
    histsize = 100
    def __init__(self, name, hazardzone=[20,40,60,80], hazardtype=0):
        self.name = name
        self.unit = ''
        self.unittype=''
        self.val = 20
        self.hist = deque(maxlen=self.histsize)
        self.filldequezero()
        self.hazardranges = HazardZone(hazardzone,hazardtype)
        self.histtimescale = 1.
        self.isselected=False

        #Clock.schedule_interval(self.test, .5)
        return

    def getCurrentVal(self):
        return self.val

    def setCurrentVal(self,value):
        self.hist.append(value)
        self.val=value
        pass


    def getUnit(self):
        return self.unit

    def getHistory(self):
        return self.hist

    def getHazardRanges(self):
        return self.hazardranges

    def getQuickText(self):
        return str(self.val) + ' ' + str(self.unit)

    def getIsSelected(self):
        return self.isselected

    def setIsSelected(self,bool):
        self.isselected=bool
        pass

    def filldequezero(self):
        for i in range(0,100):
            self.hist.append(0)
        return

class TemperatureModel(SuperDataModel):
    """
    temperature readings
    """
    def __init__(self, name,hazardzone,hazardtype):
        SuperDataModel.__init__(self,name,hazardzone=[20,40,60,80],hazardtype=0)
        #lol unicode is hard in python...
        self.unit = u"\u00B0C".encode('utf-8')
        self.unittype="Temperature"
        return

class VoltageModel(SuperDataModel):
    def __init__(self, name,hazardzone=[20,40,60,80],hazardtype=0):
        SuperDataModel.__init__(self,name,hazardzone,hazardtype)
        #lol unicode is hard in python...
        self.unit = "V".encode('utf-8')
        self.unittype="Voltage"
        return

class AmpModel(SuperDataModel):
    def __init__(self, name,hazardzone=[20,40,60,80],hazardtype=0):
        SuperDataModel.__init__(self,name,hazardzone,hazardtype)
        #lol unicode is hard in python...
        self.unit = "A".encode('utf-8')
        self.unittype="Current"
        return

class RpmModel(SuperDataModel):
    def __init__(self, name,hazardzone=[20,40,60,80],hazardtype=0):
        SuperDataModel.__init__(self,name,hazardzone,hazardtype)
        #lol unicode is hard in python...
        self.unit = "rpm".encode('utf-8')
        self.unittype="RMP"
        return

"""
    This class simply contains a list of all the data models we'll be looking for in the program.
"""

# this is a static variable. if you wanted a object specific variable, you declare it in init
datalist = {'cabintemp': TemperatureModel('Cabin Temp',[20,40,60,80],HazardZone.MOUNTAIN),
            'motortemp': TemperatureModel('Motor Temp',[20,40,60,80],HazardZone.DESCENDING),
            'batterytemp': TemperatureModel('Battery Temp',[20,40,60,80],HazardZone.DESCENDING),
            'motorrpm': RpmModel('Motor RPM',[20,40,60,80],HazardZone.DESCENDING),
            'solarvolt': VoltageModel('Solar Volt',[20,40,60,80],HazardZone.ASCENDING),
            'batvolt': VoltageModel('Battery Volt',[20,40,60,80],HazardZone.ASCENDING)
            #etc
            }

colorlist = {'Cabin Temp': [1, 0, 1, 1], #purple
            'Motor Temp': [0,0,1,1], #blue
            'Battery Temp': [1,1, 0,1], #yellow
            'Motor RPM': [0,1,1,1], #aqua
            'Solar Volt': [0,1,0,1], #green
            'Battery Volt': [1, 0, 0, 1] #red
            #etc
            };

