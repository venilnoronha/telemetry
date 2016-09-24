from sim.physics.modules import *
from sim.carobjectmodel.resources import ResourcePool
from sim.physics.behaviors import *

__author__ = 'paul'

class SimCarModel:
    '''
    The SimCarModel should describe all the resources that are relevant to the car,
    as well as the rules governing how those resources are used.
    such things include:
    -battery charge (max charge, charging and depletion behaviors)
    -how the energy input from solar panel interact with battery
    -how the motor's power requirement interact with the battery
    etc.
    relevant resources should also have a history of values per simulation run so that they can be analyzed.
    '''
    def __init__(self, startedatetime, stratobj):
        #I included a stratobj here because the initial values should be included in the strategy object.
        #This isn't implemented yet tho!
        self.startdatetime = startedatetime
        self.respool = ResourcePool()
        self.batterymodule = BatterySimulationModel()
        self.motormodule = MotorSimulationModel()
        self.solarpanelmodule = PanelSimulationModel()
        self.distanceTraveled = 0#probably will put it in its own obj later.
        self.masskg = 500
        self.initBehaviorStates()
        return

    def initBehaviorStates(self):
        self.behaviorState = CarBehaviorParserFactory.createInactiveBehavior()
        return


    def stepSim(self, currentdatetime, deltatime):
        '''
        This method will take whatever 'state' the car happens to be in, and perform all the
          energy gain and loss that that state needs to do based on the current time and the elapsed time for that step.
        :param currentdatetime: a python DateTime object representing the current date and time
        :param deltatime: in seconds
        :return:
        '''
        self.respool.recordResources(self.getElapsedTime(currentdatetime))
        self.behaviorState.update(self, currentdatetime, deltatime)

        return

    def isOutOfResoures(self):
        if self.respool.batteryChargeAh.value < 0:
            return True
        return False

    def transitionBehavior(self, behavior):
        self.behaviorState = behavior
        return

    def getElapsedTime(self, currenttime):
        diff = currenttime - self.startdatetime

        return diff.total_seconds()

