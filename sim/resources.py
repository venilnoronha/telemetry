__author__ = 'paul'

class CarResource:
    def __init__(self,unit='N/A',initvalue=0):
        self.unit = unit
        self.value = initvalue
        self.hist = [(0,0)]
        return
    def recordHist(self, dt):
        '''
        uses the current value and the time provided to add an entry to the history.
        '''
        self.hist.append((dt,self.value))
        return

class ResourcePool:
    '''
    defines the entire resource pool for the modeled car during one simulation iteration.
    '''
    def __init__(self):
        self.batteryChargeAh = CarResource('Ah', 2000)#according to what i know at least, battery charge is measured in Ampere-hour.
        self.velocityms = CarResource('m/s', 0)
        self.solarOutput = CarResource('kW/hr', 0)
        self.batteryConnection = CarResource('', 0)#some regulations require you to remove your battery at a certain time.
        return

    def recordResources(self, currentdatetime):
        '''
        to be called every update step in order to preserve data to be viewed and analyzed later.
        '''
        self.batteryChargeAh.recordHist(currentdatetime)
        self.velocityms.recordHist(currentdatetime)
        self.solarOutput.recordHist(currentdatetime)
        self.batteryConnection.recordHist(currentdatetime)