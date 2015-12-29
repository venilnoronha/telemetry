from modules import ElectricalSimulationModel, MotorSimulationModel
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
        self.electricmodule = ElectricalSimulationModel(self.respool)
        self.motormodule = MotorSimulationModel()

    def stepSim(self, currentdatetime, deltatime):
        '''
        This method will take whatever 'state' the car happens to be in, and perform all the
          energy gain and loss that that state needs to do based on the current time and the elapsed time for that step.
        :param currentdatetime: a python DateTime object representing the current date and time
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
        return

    def isOutOfResoures(self):
        '''
        TODO
        :return:
        '''
        return False

    def setTargetPower(self, v):
        '''

        :param v:
        :return:
        '''
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