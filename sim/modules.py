__author__ = 'paul'

class ElectricalSimulationModel:
    '''
    This class should take care of the flow of power in solar panels, MPPT, Battery and loss from microprocessors
    '''
    def __init__(self, respool):
        '''
        dummy values for now.
        :return:
        '''

        self.solarpoweramp = 5
        self.respool = respool

        return

    def drainPower(self, power, deltatime):
        '''
        Ideally, we know all the power we need to drain from the electrical unit when we call this per timestep.
        That way, we can figure out where the charge is distributed (to the motor, from/to the battery, etc)
        :param amp:
        :param deltatime:
        :return:
        '''

        #if solar panel is providing more power than necessary to run the motor, then we charge the battery.
        #if not, the battery is drained in addition to whatever power is generated from the panels.
        self.respool.battery.flow(-power, deltatime)#there's no relationship right now i'm just throwing values around lol.
        return

class MotorSimulationModel:
    def __init__(self):
        pass

    def getPowerReqForVel(self, vel):
        '''
        I can't decide units.....ugh.
        :param vel: in m/s??
        :return: something in Watt-hour??
        '''

        #gotta do some shenanigans here with velocity-to-efficiency to figure out how much power we need, too.

        return 80 #some random number for now lol


class SolarDayModel:
    @classmethod
    def getSolarOutput(cls, datetime):
        #we may need to figure out how to import numpy and scipy for these stuff..
        return 1

class PanelSimulationModel:
    '''
    encompasses the panel
    '''

    def __init__(self):

        return

    def getPowerAt(self, datetime):
        daylight = SolarDayModel.getSolarOutput(datetime)
        #do some compuation to convert to whatever the return unit should be...
        return daylight

