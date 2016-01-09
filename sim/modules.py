__author__ = 'paul'

class BatterySimulationModel:
    '''
    This class should take care of the flow of power in solar panels, MPPT, Battery and loss from microprocessors
    '''
    def batteryFlow(self, input, requirement, deltatimeseconds):
        '''
        if the input is higher than the power requirements, then the input power will flow directly towards the requirements, and the battery will gain the difference.
        if the requirement power is higher than the ammount input, then we will lose the difference of the power
        :param input: the amount of power put into the battery
        :param requirement: the amount of power that's requested from the battery
        :return: the amount of charge the battery should gain or lose. (negative is lose, positive is gain.)
        '''
        #calculate the predicted power flow.
        diff = input - requirement
        #caluclate the amount of charge that equates to for the amount of time given.
        chargeflow = deltatimeseconds * diff
        return chargeflow

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
        factor = .6
        return 950

class PanelSimulationModel:
    '''
    encompasses the panel

    Right now, there's only one method that probably should just be static and we won't have to create an instance
    of this object, but in case in the future, we need to have some state variables for the state of the solar panel,
    we choose to keep the methods non-static.
    '''


    def getPowerAt(self, datetime):
        power = 650#W(dc) which is V*A or J/s
        #do some compuation to convert to whatever the return unit should be...
        return power