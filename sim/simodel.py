from modules import *
from resources import ResourcePool

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
    def __init__(self):
        self.respool = ResourcePool()
        self.batterymodule = BatterySimulationModel()
        self.motormodule = MotorSimulationModel()
        self.solarpanelmodule = PanelSimulationModel()
        self.distanceTraveled = 0#probably will put it in its own obj later.
        self.masskg = 500

        return

    def stepSim(self, currentdatetime, deltatime):
        '''
        This method will take whatever 'state' the car happens to be in, and perform all the
          energy gain and loss that that state needs to do based on the current time and the elapsed time for that step.
        :param currentdatetime: a python DateTime object representing the current date and time
        :param deltatime: in seconds
        :return:
        '''
        targetvel = 26#debug value
        self.respool.velocityms.value = targetvel

        solarIn = self.solarpanelmodule.getPowerAt(currentdatetime)
        motorRequirement = self.motormodule.getPowerReqForVel(self.respool.velocityms.value)
        electricComponentRequirement = 3#describes the power used for lights and microprocessor and stuff. should have another module for this. too lazy for now.

        #calculate all the powe requirements.
        powerReq = 0
        powerReq += motorRequirement
        powerReq += electricComponentRequirement

        powerIn = 0
        powerIn += solarIn

        batflow = self.batterymodule.batteryFlow(powerIn, powerReq, deltatime)
        self.respool.batteryChargeAh.value += batflow
        print('there is %s battery charge left right now.' % self.respool.batteryChargeAh.value)
        self.distanceTraveled += self.respool.velocityms.value*deltatime

        self.respool.recordResources(currentdatetime)
        return

    def isOutOfResoures(self):
        if self.respool.batteryChargeAh.value < 0:
            return True
        return False

    def setTargetPower(self, v):
        '''

        :param v:
        :return:
        '''
        return

    def getVelocity(self):
        '''
        Based on the initial conditions given, what velocity did we end up with?
        :return:
        '''
        return 40;
