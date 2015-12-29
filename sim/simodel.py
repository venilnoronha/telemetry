from modules import ElectricalSimulationModel, MotorSimulationModel
from resources import ResourcePool
import datetime
__author__ = 'paul'

class SimCarModel:
    def __init__(self, startdatetime):
        self.respool = ResourcePool(startdatetime)
        self.electricmodule = ElectricalSimulationModel(self.respool)
        self.motormodule = MotorSimulationModel()

    def stepSim(self, deltatime):
        '''

        :param deltatime: in seconds
        :return:
        '''
        print('stepping %s second in the simulation..' % deltatime)
        #imma set a random velocity to hit for now, in meters per second.
        targetvel = 26

        #for now, the return value is Wh
        motorpowerreq = self.motormodule.getPowerReqForVel(targetvel)
        print('we need %s Wh of power for motor.' % motorpowerreq)

        #I'm not really sure where we get the volt...but...
        #the equation of relationship between Watt-hour and Amp-hour is Wh = mAh * V / 1000
        dummyvolt = 5;
        self.electricmodule.drainPower(motorpowerreq, deltatime)
        self.updatetime(deltatime)

    def setTargetPower(self, v):
        '''

        :param v:
        :return:
        '''
        return
    def updatetime(self, deltatime):
        self.respool.dtime = self.respool.dtime + datetime.timedelta(seconds=deltatime)
        return

    def getHeuristic(self):
        self.respool
        return

    def getVelocity(self):
        '''
        Based on the initial conditions given, what velocity did we end up with?
        :return:
        '''
        return 40;