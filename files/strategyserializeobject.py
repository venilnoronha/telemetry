__author__ = 'paul'
import json
import datetime

class StrategySerializableObject:
    '''
    I'm lazy and don't want to look up exactly how to make every class serializable...
    since python's default JSON serializer/deserializer can only handle primitive datatypes, I'll just
    boil down everything into primitives, and then have a function within this class to convert it to a more
    OOP-friendly object for use within our simulation.
    '''
    def __init__(self):
        self.teststr = 'helloworld'
        self.list = [1,3,3,7]
        self.itinerary = [('7h0m','charging'),
                            ('9h0m','driving'),
                            ('12h0m','charging'),
                            ('13h0m','driving'),
                            ('17h0m','charging'),
                            ('19h0m','inactive')]
        self.targetvelocity = 24.0
        #max battery power 4.5kW

    #TODO serializing *should* be moved to its own module under /files/
    def serializeStrategy(self, filepath):
        with open(filepath, 'w') as fp:
            json.dump(self.__dict__,fp,sort_keys=True,indent=4,separators=(',',':'))

    def deserializeStrategy(self, filepath):
        with open(filepath, 'r') as fp:
            self.__dict__ = json.load(fp)

        return self


class StrategyObject:
    '''
    ACTUAL representation of the strategy that's going to be used for the simulation. We'll use the clas *above* to serialize/deserialize
    and then we'll parse it into one of these objects.
    '''
