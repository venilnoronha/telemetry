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


class ResourcePool:
    '''
    defines the entire resource pool for the modeled car during one simulation iteration.
    '''
    def __init__(self, startdatetime):
        self.battery = BatteryModel()
        self.dtime = startdatetime

        return