__author__ = 'paul'
import datetime

class SimRule:
    def __init__(self):
        self.ruleTime = None
        self.statestring = 'None'
        return

    def __init__(self, t, statestring):
        self.ruleTime = t
        self.statestring = statestring
        return

    @classmethod
    def shouldRuleHappen(cls, lasttime, nexttime, ruletime):
        #hurr...python time is stupid and won't let me do math with it unless i stick a date with it...
        #so now we end up with this atrocity...and it probably behaves poorly around midnight.
        #good news is, we'll probably not be doing any state-switching around midnight...fingers crossed.
        lastdiff = datetime.datetime.combine(datetime.datetime(1,1,1,0,0,0),lasttime) - datetime.datetime.combine(datetime.datetime(1,1,1,0,0,0),ruletime)
        nextdiff = datetime.datetime.combine(datetime.datetime(1,1,1,0,0,0),nexttime) - datetime.datetime.combine(datetime.datetime(1,1,1,0,0,0),ruletime)
        zero = datetime.timedelta(0)
        return lastdiff < zero and nextdiff > zero
