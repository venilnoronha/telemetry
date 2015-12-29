__author__ = 'paul'
from simodel import SimCarModel


class SimluationObject:
    '''
    describes one full 'run' or 'iteration' of the simulation.
    This includes the starting conditions and some variations in the different rules that we might think of implementing.
    the object is self contained and has its own pool of resources. This way, we can multi-thread each iteration on its
    own core or something later, should we decide to do that.
    '''
    carmodel = SimCarModel()
    rules = DailyItinerary()


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
        return

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