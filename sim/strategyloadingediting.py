__author__ = 'paul'


class StrategyOpener:
    @classmethod
    def openStrategyFile(cls, path):
        '''

        :param path:
        :return: a strategy object loaded with the path provided, or None, if the path did not point to a valid file.
        '''