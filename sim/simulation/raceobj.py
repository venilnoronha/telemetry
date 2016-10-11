__author__ = 'paul'

class RaceObject:
    '''
    This class keeps all the parameters of the race such as:
    how long the race is
    where the checkpoint is
    Other regulation-related things might have to be stored in here such as time allowed to drive, speed limit, etc?
    eventually we can even get down to stuff like topology of the route
    i'd like for this to be serialized later.
    '''
    def __init__(self):
        self.racedistkm = 3022
        #checkpoints stored as list of km's along the path
        self.checkpoints = [1000, 2000, 3000]
        self.timeLimitSeconds = 60*60*24*7 #test value of 7 days for now
        self.speedlimitkmph = 110
        return