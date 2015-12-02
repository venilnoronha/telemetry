__author__ = 'paul'

from simodel import simcarmodel
import datetime

@classmethod
def runASimIteration():
    #set some initial conditions for simulations
    #such as target powerconsumption, elevation for the next distance, , time of day, etc.
    s = simcarmodel(datetime.date.today())
    s.setTargetVelocity(40)
    #run simulation for so many steps
    steps = 100
    for x in range(steps):
        s.stepSim(1.0)

    #get result statistics
    return

#dummy for testing
if __name__ == '__main__':
    print('running simulation...')
    #this method should eventually take in parameters that sets initial conditions.
    #we take the return heuristic of this, and run more iterations based on the result.
    runASimIteration();