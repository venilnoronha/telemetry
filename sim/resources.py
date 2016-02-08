__author__ = 'paul'

class CarResource:
    def __init__(self,unit='N/A',initvalue=0):
        self.unit = unit
        self.value = initvalue
        self.hist = [(0,0)]
        return
    def recordHist(self, elapsedtime):
        '''
        uses the current value and the time provided to add an entry to the history.
        '''
        self.hist.append((elapsedtime,self.value))
        return

    def getMinMax(self):
        maxx = 0
        minx = 0
        maxy = 0
        miny = 0
        for pair in self.hist:
            x = pair[0]
            y = pair[1]
            if x > maxx:
                maxx = x
            if x < minx:
                minx = x
            if y > maxy:
                maxy = y
            if y < miny:
                miny = y
        return (minx, maxx, miny, maxy)

class ResourcePool:
    '''
    defines the entire resource pool for the modeled car during one simulation iteration.
    '''
    def __init__(self):
        self.batteryChargeAh = CarResource('Ah', 1000000)#according to what i know at least, battery charge is measured in Ampere-hour.
        self.velocityms = CarResource('m/s', 0)
        self.solarOutput = CarResource('W(dc)', 0)
        self.batteryConnection = CarResource('', 0)#some regulations require you to remove your battery at a certain time.
        return

    def recordResources(self, elapsedtime):
        '''
        to be called every update step in order to preserve data to be viewed and analyzed later.
        '''
        self.batteryChargeAh.recordHist(elapsedtime)
        self.velocityms.recordHist(elapsedtime)
        self.solarOutput.recordHist(elapsedtime)
        self.batteryConnection.recordHist(elapsedtime)