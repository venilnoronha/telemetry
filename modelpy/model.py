__author__ = 'paul'




class HazardZone:
    SAFE=0
    WARN=1
    DANGER=2
    #def __init__(self, safe=[0,20, 30, 40], warn=[20,30, 40, 60],danger=60):
    def __init__(self, safe=[40], warn=[40, 60],danger=[60]):
        self.saferange=safe
        self.warnrange=warn
        self.dangerrange=danger

    def currentRange(self, val):
        '''
        gives the (int) hazard level that something is in given the current value.
        :param val:
        :return:
        '''
        if self.checkInterval(self.saferange,val, self.SAFE):
            return self.SAFE
        elif self.checkInterval(self.warnrange,val, self.WARN):
            return self.WARN
        else:
            return self.DANGER

    def checkInterval(self, intervals, val, zone):
        '''

        :param intervals:
        :return:
        '''
        is_valid = False
        if(zone==self.SAFE and len(intervals)==1):
            if(val<intervals[0]):
                is_valid=True
        elif(zone==self.WARN and len(intervals)==2):
            if(val>=intervals[0] and val<intervals[1]):
                is_valid=True
        elif(zone==self.DANGER and len(intervals)==1):
            if(val>=intervals[0]):
                is_valid=True
        else:
            print 'false'
            is_valid=False
        '''
        i = 0
        while(i < len(intervals)):
            minin = min(intervals[i], intervals[i + 1])
            maxin = max(intervals[i], intervals[i + 1])

            if(val >= minin and val < maxin):
                is_valid = True
            else:
                is_valid = False

            i += 2
        '''
        return is_valid

       # minin = min(intervals)
       # maxin = max(intervals)



  #      return False


from collections import deque

class SuperDataModel:

    """
    base class for all the data that we'll be displaying.
    """
    histsize = 100
    def __init__(self, name):
        self.name = name
        self.unit = ''
        self.unittype=''
        self.val = 20
        self.hist = deque(maxlen=self.histsize)
        self.filldequezero()
        self.hazardranges = HazardZone()
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
        return self.hist;

    def getHazardRanges(self):
        return self.hazardranges;

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
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = u"\u00B0C".encode('utf-8')
        self.unittype="Temperature"
        return

class VoltageModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "V".encode('utf-8')
        self.unittype="Voltage"
        return

class AmpModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "A".encode('utf-8')
        self.unittype="Current"
        return

class RpmModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "rpm".encode('utf-8')
        self.unittype="RMP"
        return

"""
    This class simply contains a list of all the data models we'll be looking for in the program.
"""

# this is a static variable. if you wanted a object specific variable, you declare it in init
datalist = {'cabintemp': TemperatureModel('Cabin Temp'),
            'motortemp': TemperatureModel('Motor Temp'),
            'batterytemp': TemperatureModel('Battery Temp'),
            'motorrpm': RpmModel('Motor RPM'),
            'solarvolt': VoltageModel('Solar Volt'),
            'batvolt': VoltageModel('Battery Volt')
            #etc
            };

colorlist = {'Cabin Temp': [146, 0, 227, 1], #purple
            'Motor Temp': [0,0,255,1], #blue
            'Battery Temp': [255,255, 0,1], #yellow
            'Motor RPM': [0,255,255,1], #aqua
            'Solar Volt': [0,255,0,1], #green
            'Battery Volt': [255, 0, 0, 1] #red
            #etc
            };

