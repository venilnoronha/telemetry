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
        self.respool.recordResources(currentdatetime)
        self.behaviorState.update(self, currentdatetime, deltatime)

        return

    def isOutOfResoures(self):
        if self.respool.batteryChargeAh.value < 0:
            return True
        return False

    def transitionBehavior(self, behavior):
        self.behaviorState = behavior
        return

class CarBehaviorState:
    def __init__(self, name):
        self.name = name
        return

    def update(self, carmodel, currentdatetime, deltatime):
        '''
        does the heavy lifting of the simulation.
        based on whatever state this car is in, it will change its behavior and call on different models to achieve said behavior.
        :param carmodel: the carmodel actually is the thing that contains a carstate, however, it needs to pass itself in, because this update method needs to access the different models contained in carmodel.
        :return:
        '''
        return

    def transition(self, carmodel):
        '''
        defines the behavior of transitioning to this state. sets all the appropriate state variables in carmodel (such as velocity, etc) to the proper values.
        :param carmodel:
        :return:
        '''
        return

class CarDrivingBehavior(CarBehaviorState):

    def __init__(self, velocity=0):
        CarBehaviorState.__init__(self, 'driving')
        self.targetvelocity = velocity
        return


    def update(self, carmodel, currentdatetime, deltatime):
        carmodel.respool.velocityms.value = self.targetvelocity

        solarIn = carmodel.solarpanelmodule.getPowerAt(currentdatetime)
        motorRequirement =  carmodel.motormodule.getPowerReqForVel(carmodel.respool.velocityms.value)
        electricComponentRequirement = 3#describes the power used for lights and microprocessor and stuff. should have another module for this. too lazy for now.

        #calculate all the powe requirements.
        powerReq = 0
        powerReq += motorRequirement
        powerReq += electricComponentRequirement

        powerIn = 0
        powerIn += solarIn

        batflow = carmodel.batterymodule.batteryFlow(powerIn, powerReq, deltatime)
        carmodel.respool.batteryChargeAh.value += batflow
        print(currentdatetime.time())
        print('driving, there is %s battery charge left right now.' % carmodel.respool.batteryChargeAh.value)
        carmodel.distanceTraveled += carmodel.respool.velocityms.value*deltatime
        return

class CarChargingBehavior(CarBehaviorState):

    def __init__(self):
        CarBehaviorState.__init__(self, 'chargestop')
        return

    def update(self, carmodel, currentdatetime, deltatime):
        solarIn = carmodel.solarpanelmodule.getPowerAt(currentdatetime)
        powerIn = 0
        powerIn += solarIn

        batflow = carmodel.batterymodule.batteryFlow(powerIn, 0, deltatime)
        carmodel.respool.batteryChargeAh.value += batflow
        print(currentdatetime.time())
        print('charging, there is %s battery charge left right now.' % carmodel.respool.batteryChargeAh.value)
        return

class CarStoppedNoChargeBehavior(CarBehaviorState):
    def __init__(self):
        CarBehaviorState.__init__(self, 'nochargestop')
        return

    def update(self, carmodel, currentdatetime, deltatime):
        print('in the stopped behavior update method.')
        print('we don\'t do anything here.')
        return

class CarBehaviorParserFactory:
    '''
    Need some way of parsing a string (probably read from a JSON later on) into a real CarBehavior...
    this in in the future will include what behavior it is, as well as additional relevant parameter like speed and other stuff.
    all of the methods in here are static method (@classmethods) so you can access it anywhere.
    '''
    @classmethod
    def parseCreateCarBehavior(cls, str):
        if str == 'driving':
            return cls.createDrivingBehavior(50)#all of these are just debug values for now. to be filled later.
        elif str == 'charging':
            return cls.createChargingBehavior()
        elif str == 'inactive':
            return cls.createInactiveBehavior()
        else:
            return None
        return

    @classmethod
    def createDrivingBehavior(cls, velocity):
        return CarDrivingBehavior(velocity)

    @classmethod
    def createChargingBehavior(cls):
        return CarChargingBehavior()

    @classmethod
    def createInactiveBehavior(cls):
        return CarStoppedNoChargeBehavior()
