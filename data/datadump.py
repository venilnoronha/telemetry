__author__ = 'YutongGu'
import json

class datadump:
    data={'cabintemp':[],
    'motortemp':[],
    'batterytemp':[],
    'motorrpm':[],
    'solarvolt':[],
    'batvolt':[]}
    dataNames=['cabintemp','motortemp','batterytemp','motorrpm','solarvolt','batvolt']

    def __init__(self):
        pass

    def appendValue(self,name, value):
        if(self.data.has_key(name)):
            print 'appended value to datadump'
            self.data[name].append(value)

        else:
            print 'Error, ' + name + 'does not exist'

    def exportJSON(self,fileName):
        print 'exporting json data as '+fileName
        with open(fileName, 'w') as outfile:
            json.dump(self.data, outfile, indent=2, separators=(',', ':'))

    def exportCSV(self, fileName):
        print 'exporting csv data to ' +fileName
        with open(fileName, 'w') as csvfile:
            csvfile.write('cabintemp,,batterytemp,,motortemp,,motorrpm,,solarvolt,,batvolt,\n')
            for i in range(0,len(self.data['cabintemp'])):
                string=''
                for j in range (0, len(self.dataNames)):
                    string+=str(self.data[self.dataNames[j]][i][0])+','+str(self.data[self.dataNames[j]][i][1])+','
                csvfile.write(string+'\n')
