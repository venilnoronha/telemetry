__author__ = 'paul'




class HazardZone:
    SAFE=0
    WARN=1
    DANGER=2
    def __init__(self, safe=[0,20, 30, 40], warn=[20,30, 40, 60],danger=60):
        self.saferange=safe
        self.warnrange=warn
        self.dangerrange=danger

    def currentRange(self, val):
        '''
        gives the (int) hazard level that something is in given the current value.
        :param val:
        :return:
        '''
        if self.checkInterval(self.saferange,val):
            return self.SAFE
        elif self.checkInterval(self.warnrange,val):
            return self.WARN
        else:
            return self.DANGER

    def checkInterval(self, intervals, val):
        '''

        :param intervals:
        :return:
        '''
        is_valid = True

        i = 0
        while(i < len(intervals)):
            minin = min(intervals[i], intervals[i +1])
            maxin = max(intervals[i], intervals[i + 1])

            if(val >= minin and val < maxin):
                is_valid = True
            else:
                is_valid = False

            i += 2
            
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
        self.unittype = 'None'
        self.val = 20
        self.hist = deque(maxlen=self.histsize)
        self.hazardranges = HazardZone()

        #Clock.schedule_interval(self.test, .5)
        return
    
    def getCurrentVal(self):
        return self.val

    def setCurrentVal(self,value):
        for i in range(self.histsize-2,0,-1):
            self.hist.append(self.val)
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

class TemperatureModel(SuperDataModel):
    """
    temperature readings
    """
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = u"\u00B0C".encode('utf-8')
        return

class VoltageModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "V".encode('utf-8')
        return

class AmpModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "A".encode('utf-8')
        return

class RpmModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "rpm".encode('utf-8')
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


