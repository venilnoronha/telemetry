__author__ = 'paul'
import json


class StrategyObject:
    def __init__(self):
        self.teststr = 'helloworld'
        self.list = [1,3,3,7]

    def serializeStrategy(self, filepath):
        with open(filepath, 'w') as fp:
            json.dump(self.__dict__,fp,sort_keys=True,indent=4,separators=(',',':'))


