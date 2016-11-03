__author__ = 'paul'
import files.datadump

class CarResource:
    def __init__(self,name,unit='N/A',initvalue=0):
        self.name = name
        self.unit = unit
        self.value = initvalue
        self.hist = []
        return
    def recordHist(self, elapsedtime):
        '''
        uses the current value and the time provided to add an entry to the history.
        '''
        self.hist.append((elapsedtime,self.value))
        return

    def getHist(self, granularity):
        '''
        returns a history but with values of every timestep*granularity seconds instead of the original
        this gives you a way to save out data at a higher resolution so you don't take up WAY too much data.
        '''
        rv = []
        for x in range(0,len(self.hist),granularity):
            rv.append(self.hist[x])

        return rv
    '''
    I think this is used to set the range for the graph visualization atm
    '''
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
        self.batteryChargeAh = CarResource('Charge', 'Ah', 1000000)#according to what i know at least, battery charge is measured in Ampere-hour.
        self.velocityms = CarResource('Velocity', 'm/s', 0)
        self.solarOutput = CarResource('Solar Output', 'W(dc)', 0)
        self.batteryConnection = CarResource('Battery Connection','', 0)#some regulations require you to remove your battery at a certain time.
        #all parameters below subject to change after real measurements
	self.mass = CarResource('Mass','kg',500)
	self.tyrePressure = CarResource('Tyre Pressure','bar',0.5)
	self.surfaceareaTowind = CarResource('Surface Area to Wind','m*m',10)
	return

    def recordResources(self, elapsedtime):
        '''
        to be called every update step in order to preserve data to be viewed and analyzed later.
        '''
        self.batteryChargeAh.recordHist(elapsedtime)
        self.velocityms.recordHist(elapsedtime)
        self.solarOutput.recordHist(elapsedtime)
        self.batteryConnection.recordHist(elapsedtime)
		#all parameters subject to change after real measurements
	self.mass.recordHist(elapsedtime)
	self.tyrePressure.recordHist(elapsedtime)
	self.surfaceareaTowind.recordHist(elapsedtime)
	return