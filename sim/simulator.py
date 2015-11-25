__author__ = 'paul'

from simodel import simcarmodel
import datetime

#dummy for testing
if __name__ == '__main__':
    print('running simulation...')
    s = simcarmodel(datetime.date.today())
    s.stepSim(1.0)