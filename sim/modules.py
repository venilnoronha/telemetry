__author__ = 'paul'

class BatteryModel:
    def __init__(self):
        self.chargeAh = 20;#according to what i know at least, battery charge is measured in Ampere-hour.
        return

    def flow(self, amp, deltatime):
        '''
        amp in ampere, negative if flowing out, positive if flowing in.
        deltatime in seconds.
        '''
        #convert to hours.
        hour = deltatime / 3600.0 #there are 3600 seconds in an hour.
        delta = amp*deltatime
        self.chargeAh = self.chargeAh + delta #gotta account for loss from efficiency later.
        print('battery has %s Ah charge left' % self.chargeAh)
        pass

class ElectricalSimulationModel:
    '''
    This class should take care of the flow of power in solar panels, MPPT, Battery and loss from microprocessors
    '''
    def __init__(self):
        '''
        dummy values for now.
        :return:
        '''

        self.solarpoweramp = 5;

        self.battery = BatteryModel()


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
        self.battery.flow(-power, deltatime)#there's no relationship right now i'm just throwing values around lol.
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

