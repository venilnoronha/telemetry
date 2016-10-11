__author__ = 'paul'
import csv


def dumpdata(filename, csvdata):

    print("dumping data...")
    with open(filename, 'wb') as csvfile:
        testwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONE,
                                escapechar='\\')
        for row in csvdata:
            testwriter.writerow(row)

def getCSVData(resourceholder):
        temp = [resourceholder.batteryChargeAh,
                resourceholder.velocityms,
                resourceholder.solarOutput,
                resourceholder.batteryConnection]
        rv = []
        tempdata = []
        row = ["Elapsed Time (s)"]
        for hist in temp:
            row.append(hist.name + " (" + hist.unit + ")")
            tempdata.append(hist.getHist(10))
        rv.append(row)
        for index in range(0,len(tempdata[0])):
            row = [tempdata[0][index][0]]
            for hist in tempdata:
                row.append(hist[index][1])
            rv.append(row)
        return rv;