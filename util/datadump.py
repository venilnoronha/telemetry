__author__ = 'paul'
import csv

class DataHolder:
    def getAllData(self):
        '''
        to be implemented by children the history holder of both sim and telemetry)
        :return: None when not implemented. Expected: list of 'history', which are pairs of time and datavalue.
        '''
        return None

def dumpdata(dataholder):

    print("attempting to dump data...")
    with open('dumptest.csv', 'wb') as csvfile:
        testwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|',
                            quoting=csv.QUOTE_NONE,
                            escapechar='\\')
        testwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        testwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    '''
    allrecords = dataholder.getAllData()
    if(allrecords) :
        for hist in allrecords:
            for pair in hist:
                print(pair)
                    '''