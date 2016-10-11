__author__ = 'paul'

from sim.simulation.simodel import SimCarModel
from files.strategyserializeobject import StrategySerializableObject
from sim.stratparam.itinereary import *
from raceobj import RaceObject


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
        self.startdatetime = startdatetime
        #following are some objects that (should eventually) be loaded from files
        #these objects provide the varying parameters within our race.
        self.stratobj = StrategySerializableObject()
        self.stratobj.deserializeStrategy('parameters/strategy.json');
        self.raceconditions = RaceObject()
        self.carmodel = SimCarModel(startdatetime, self.stratobj)
        self.itinerary = DailyItinerary(self.stratobj)

        return


    def startRun(self):
        '''
        This method is empty for now. I plan on making run() the blocking version, and
        this version can spin off a separate thread and run the task separately, allowing us to run multiple cases at once.
        We'll implement the non-threaded version for now, and work on this later.
        '''
        #fire off a new thread with run() as a lambda or something
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
        '''
        if self.DEBUG:
            print('updating', self.iterationName, ', elapsed time:', self.getElapsedSeconds(), 'seconds')
        '''
        self.carmodel.stepSim(self.currentdatetime, deltatime)
        self.itinerary.updateStateFromRules(self.currentdatetime, deltatime, self.carmodel)
        self.advancecurrentdatetime(deltatime)
        return

    def advancecurrentdatetime(self, deltatime):
        self.currentdatetime = self.currentdatetime + datetime.timedelta(seconds=deltatime)
        return

    def getElapsedDatetime(self):
        return self.currentdatetime-self.startdatetime

    def getElapsedSeconds(self):
        return self.getElapsedDatetime().total_seconds()

    def getReturnMsg(self):
        '''
        checks if the simulations has either met the success or failure states, and should stop running and return or not.
        :return: the return message
        '''
        if self.carmodel.distanceTraveled >= (self.raceconditions.racedistkm*1000):
            return SimulationObject.SUCCESS
        if self.carmodel.isOutOfResoures():
            return SimulationObject.OUTOFRESOURCES
        if self.getElapsedSeconds() > self.raceconditions.timeLimitSeconds:
            return SimulationObject.TIMEOUT
        return SimulationObject.RUNNING
