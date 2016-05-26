__author__ = 'paul'
import csv

class DataHolder:
    def getCSVData(self):
        '''
        to be implemented by children the history holder of both sim and telemetry)
        :return: None when not implemented. Expected: list of 'history', which are pairs of time and datavalue.
        '''
        return None

def dumpdata(csvdata):

    print("dumping data...")
    with open('dumptest.csv', 'wb') as csvfile:
        testwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONE,
                                escapechar='\\')
        for row in csvdata:
            testwriter.writerow(row)

