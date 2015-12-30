__author__ = 'paul'

from simobj import SimulationObject
import datetime

def runASimIteration():
    s = SimulationObject('test sim', datetime.datetime.today())
    rv = s.run()
    print('race finished with return message', rv)
    return

#dummy for testing
if __name__ == '__main__':
    print('running simulation...')
    #this method should eventually take in parameters that sets initial conditions.
    #we take the return heuristic of this, and run more iterations based on the result.
    runASimIteration()