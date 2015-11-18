from modules import ElectricalSimulationModel, MotorSimulationModel
import datetime
__author__ = 'paul'

class Simulator:
    def __init__(self, startdatetime):
        self.dtime = startdatetime
        self.electricmodule = ElectricalSimulationModel()
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

    def updatetime(self, deltatime):
        self.dtime = self.dtime + datetime.timedelta(seconds=deltatime)
        return

#dummy for testing
if __name__ == '__main__':
    print('running simulation...')
    s = Simulator()
    s.stepSim(1.0)