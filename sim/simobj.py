__author__ = 'paul'
from simodel import SimCarModel


class SimluationObject:
    '''
    describes one full 'run' or 'iteration' of the simulation.
    This includes the starting conditions and some variations in the different rules that we might think of implementing.
    the object is self contained and has its own pool of resources. This way, we can multithread each iteration on its own core
    later, should we decide to do that.
    '''
    carmodel = SimCarModel()
    