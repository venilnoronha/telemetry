__author__ = 'paul'
from simodel import SimCarModel
import datetime


class SimulationObject:
    '''
    describes one full 'run' or 'iteration' of the simulation.
    This includes the starting conditions and some variations in the different rules that we might think of implementing.
    the object is self contained and has its own pool of resources. This way, we can multi-thread each iteration on its
    own core or something later, should we decide to do that.
    '''
    timeresolutionseconds = 30
    RUNNING=0
    OUTOFRESOURCES=-1
    TIMEOUT=-2
    SUCCESS=1
    DEBUG = True

    def __init__(self, iname, startdatetime):
        self.iterationName = iname
        self.currentdatetime = startdatetime
        self.carmodel = SimCarModel()
        self.rules = DailyItinerary()
        return


    def startRun(self):
        '''
        This method is empty for now. I plan on making run() the blocking version, and
        this version can spin off a separate thread and run the task separately, allowing us to run multiple cases at once.
        We'll implement the non-threaded version for now, and work on this later.
        '''
        return

    def run(self):
        '''
        This method actual runs through all of the itinerary per day
        either until the battery is completely run out or when we've reached the end of the race.
        '''
        rmsg = self.getReturnMsg()
        while self.shouldKeepRunning(rmsg):
            self.update(SimulationObject.timeresolutionseconds)
            rmsg = self.getReturnMsg()

        return rmsg

    def shouldKeepRunning(self, msg):
        return msg == SimulationObject.RUNNING

    def update(self, deltatime):
        '''
         at each step, we consider all the things that are state-dependent
         like the acquisition of energy from the solar panels when battery is attached and the loss of energy from
         motions
         then we use the datetime variables compare with our DailyItinerary, and figure out if we need to change
         any of the state of the car model.
         finally, we advance the current time with the deltatime.
        '''
        if self.DEBUG:
            print('updating %s...' % self.iterationName)
        self.carmodel.stepSim(self.currentdatetime, deltatime)
        self.rules.updateStateFromRules(self.currentdatetime, deltatime, self.carmodel)
        self.advancecurrentdatetime(deltatime)
        return

    def advancecurrentdatetime(self, deltatime):
        self.currentdatetime = self.currentdatetime + datetime.timedelta(seconds=deltatime)
        return

    def getReturnMsg(self):
        '''
        checks if the simulations has either met the success or failure states, and should stop running and return or not.
        :return: the return message
        '''

        return SimulationObject.RUNNING

class DailyItinerary:
    '''
    Describes the sequence of events that we might take during any given day during the race.
    This is determined by both the regulation of the particular race we are in, as well as the strategy we decide.
    An example of this would be something like:
    7:00am charge batteries
    9:00am begin driving
    12:00pm stop for lunch
    1:00pm begin driving
    5:00pm stop and charge
    7:00pm mandatory battery removal
    as you can see, each itinerary item has a time and an activity associated with it.
    These modules are described in the file modules.py.
    The daily itinerary as well as the rule-modules inside the itinerary (how we choose the speed, what we do at what time, etc)
    is the 'meat' of the strategy, and will be the factors we adjust (either manually or with random variations)
    '''
    def __init__(self):

        return

    def updateStateFromRules(self, currentdatetime, deltatime, carmodel):
        '''
        updates the state of the car model based on whatever itinerary or rule within that itinerary we strategize.

        :return:
        '''
        return