__author__ = 'paul'
from simodel import SimCarModel, CarBehaviorParserFactory
import datetime
import random
from strategyobject import StrategySerializableObject
from rules import SimRule


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
        teststrat = StrategySerializableObject()
        teststrat.deserializeStrategy('testserialize.json');
        self.iterationName = iname
        self.currentdatetime = startdatetime
        self.startdatetime = startdatetime
        self.carmodel = SimCarModel(startdatetime)
        self.rules = DailyItinerary(teststrat)
        self.initDebugDefaults()
        return

    def initDebugDefaults(self):
        self.totalRaceMeters = 3000000 #test value of 3000km for now
        self.timeLimitSeconds = 60*60*24*7 #test value of 7 days for now

    def readStaticParameters(self):
        '''
        reads some data to establish the initial conditions of the simulation iteration.
        we'll probably end up using json?
        :return:
        '''
        return

    def setDynamicParameters(self):
        '''
        The point of the simulation is to vary a bunch of parameters and figure out what the 'best' configuration
         of parameters are.
         Therefore, we have to figure out a way to set a whole bunch of policies and rules for our race.
        :return:
        '''


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
        '''
        if self.DEBUG:
            print('updating', self.iterationName, ', elapsed time:', self.getElapsedSeconds(), 'seconds')
        '''
        self.carmodel.stepSim(self.currentdatetime, deltatime)
        self.rules.updateStateFromRules(self.currentdatetime, deltatime, self.carmodel)
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
        if self.carmodel.distanceTraveled >= self.totalRaceMeters:
            return SimulationObject.SUCCESS
        if self.carmodel.isOutOfResoures():
            return SimulationObject.OUTOFRESOURCES
        if self.getElapsedSeconds() > self.timeLimitSeconds:
            return SimulationObject.TIMEOUT
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
    def __init__(self, paramobj):
        #debug list of itinerary reflects the comments above.
        self.paramobj = paramobj
        self.list = DailyItinerary.getRulesListFromParameterObject(paramobj)
        self.currentIndex = 0
        return

    @classmethod
    def getRulesListFromParameterObject(cls, param):
        list = []
        print(param)
        for rule in param.itinerary:
            hdelim = rule[0].split("h");
            h = int(hdelim[0])
            mdelim = hdelim[1].split("m");
            m = int(mdelim[0])
            dd = datetime.time(hour=h, minute=m)
            behavior = rule[1]
            specifictime = SpecificTimeBehavior(dd,behavior)
            list.append(SimRule(dd, behavior))

        return list

    def updateStateFromRules(self, currentdatetime, deltatime, carmodel):
        '''
        updates the state of the car model based on whatever itinerary or rule within that itinerary we strategize.

        :return:
        '''

        nextdatetime = currentdatetime+datetime.timedelta(seconds=deltatime)

        #if we move onto the next day, then we should reset the itinerary to the start.
        if nextdatetime.day > currentdatetime.day:
            self.currentIndex = 0


        if self.currentIndex < len(self.list):
            nextrule = self.list[self.currentIndex]
            if SimRule.shouldRuleHappen(currentdatetime.time(), nextdatetime.time(), nextrule.ruleTime):
                behavior = CarBehaviorParserFactory.parseCreateCarBehavior(nextrule.statestring, self.paramobj)
                if behavior:
                    carmodel.transitionBehavior(behavior)

                self.currentIndex += 1



        return

class SimVariationObject:
    '''
    This object defines all the variable and some non-variable parameters within the racing simulation.
     For example, the timing of the itinerary,
     the parameters involved in determining the velocity,
     but also non-varying parameters (that might vary depending on the race we enter) like:
     starting battery charge,
     race distance,
     etc.
    '''
    def __init__(self):
        self.itinerary = [SpecificTimeBehavior(datetime.time(hour=7),behaviorname='charging'),
                             SpecificTimeBehavior(datetime.time(hour=9),behaviorname='driving'),
                             SpecificTimeBehavior(datetime.time(hour=12),behaviorname='charging'),
                             SpecificTimeBehavior(datetime.time(hour=13),behaviorname='driving'),
                             SpecificTimeBehavior(datetime.time(hour=17),behaviorname='charging'),
                             SpecificTimeBehavior(datetime.time(hour=19),behaviorname='inactive')]

        return

    def getVariedItinerary(self):
        rv = []
        for item in self.itinerary:
            rv.append(SimRule(item.getTime(), item.behaviorname))
        return rv
class TimeBehavior:
    def __init__(self, behaviorname='inactive'):
        self.behaviorname = behaviorname

    def getTime(self):
        return datetime.time(hour=0,minute=0)

class VariedItineraryItem(TimeBehavior):
    def __init__(self, seedtime, variation=1.0, behaviorname='inactive'):
        '''

        :param behaviorname: serialized string for the behavior. for example, 'driving' for the Driving Car Behavior.
        :param seedtime: the mid-point of time for the range. for example, 5:30pm will be 17.5
        :param variation: the variation on either side of the specified seed. in hours.
        :return:
        '''
        TimeBehavior.__init__(self,behaviorname=behaviorname)
        self.seedtime = seedtime
        self.variation = variation

        return

    def getTime(self):
        hr = self.seedtime
        hr += random.uniform(-self.variation, self.variation)
        ihour = int(hr)
        min = hr-ihour
        min *= 60
        min = int(min)
        ttt = datetime.time(hour=ihour, minute=min)
        return ttt

class SpecificTimeBehavior(TimeBehavior):
    def __init__(self, time=datetime.time(), behaviorname='inactive'):
        TimeBehavior.__init__(self, behaviorname=behaviorname)
        self.time = time

    def getTime(self):
        return self.time