__author__ = 'paul'
from kivy.clock import Clock



class HazardZone:
    SAFE=0
    WARN=1
    DANGER=2
    def __init__(self, safe=[0,20, 30, 40], warn=[20,30, 40, 60],danger=60):
        self.saferange=safe
        self.warnrange=warn
        self.dangerrange=danger

    def currentRange(self, val):
        '''
        gives the (int) hazard level that something is in given the current value.
        :param val:
        :return:
        '''
        if self.checkInterval(self.saferange,val):
            return self.SAFE
        elif self.checkInterval(self.warnrange,val):
            return self.WARN
        else:
            return self.DANGER

    def checkInterval(self, intervals, val):
        '''

        :param intervals:
        :return:
        '''
        is_valid = True

        i = 0
        while(i < len(intervals)):
            minin = min(intervals[i], intervals[i +1])
            maxin = max(intervals[i], intervals[i + 1])

            if(val >= minin and val < maxin):
                is_valid = True
            else:
                is_valid = False

            i += 2
            
        return is_valid

       # minin = min(intervals)
       # maxin = max(intervals)



  #      return False


from collections import deque

class SuperDataModel:

    """
    base class for all the data that we'll be displaying.
    """
    histsize = 100
    def __init__(self, name):
        self.name = name
        self.unit = 'Undef'
<<<<<<< HEAD
        self.val = 0.
        self.hist = [0]*self.histsize
    ##########comment out 2 lines below
=======

        self.val = 0
        self.hist = deque(maxlen=self.histsize)

>>>>>>> origin/master
        self.hazardranges = HazardZone()
        Clock.schedule_interval(self.test, .5)
        return
    def test(self, *arg):
        self.val+= 4
    def getCurrentVal(self):
        return self.val

    def setCurrentVal(self,value):
        for i in range(self.histsize-2,0,-1):
            self.hist.append(self.val)
        self.val=value
        pass

    def getUnit(self):
        return self.unit

    def getHistory(self):
        return self.hist;

    def getHazardRanges(self):
        return self.hazardranges;

    def getQuickText(self):
        return str(self.val) + ' ' + str(self.unit)

class TemperatureModel(SuperDataModel):
    """
    temperature readings
    """
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = u"\u00B0C".encode('utf-8')
        return

class VoltageModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "V".encode('utf-8')
        return

class AmpModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "A".encode('utf-8')
        return

class RpmModel(SuperDataModel):
    def __init__(self, name):
        SuperDataModel.__init__(self,name)
        #lol unicode is hard in python...
        self.unit = "rpm".encode('utf-8')
        return

"""
    This class simply contains a list of all the data models we'll be looking for in the program.
"""
import socket   #for sockets
import sys  #for exit
from kivy.clock import Clock

# this is a static variable. if you wanted a object specific variable, you declare it in init
datalist = {'cabintemp': TemperatureModel('Cabin Temp'),
            'motortemp': TemperatureModel('Motor Temp'),
            'batterytemp': TemperatureModel('Battery Temp'),
            'motor rpm': RpmModel('Motor RPM'),
            'solar volt': VoltageModel('Solar Volt'),
            'bat volt': VoltageModel('Battery Volt')
            #etc
            };


class SolarCarConnector:
    HOST="";
    PORT=13000;
    """
    this class handles actually making a connection to the simulation or the actual microprocessor.
    """

    def __init__(self):
        try:
            #create an AF_INET, STREAM socket (TCP)
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit()
        print 'Socket Created'
        pass

    def startserv(self, pollrate):
        '''
        should attempt to establish a connection and spin off a new thread that polls every @pollrate seconds(or something)
        do whatever necessary for when you can't establish a connection...
        do NOT block the main UI with this.
        :return:
        '''

        try:
            self.s.bind((self.HOST, self.PORT))
        except socket.error , msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

        print 'Socket bind complete'

        #self.s.listen(1)
        #print 'Socket now listening'

        #conn, addr = self.s.accept()
        #print 'Connected with ' + addr[0] + ':' + str(addr[1])
        while 1:
            self.poll()
        #Clock.schedule_interval(self.poll,pollrate)
        pass


    def poll(self):
        '''
        grr...idk how to make private methods...
        should be called within thread in startserv
        :return:
        '''
        message=self.s.recv(4096)
        print('message recieved')
        str=message.split(';')
        str2=[str.size()]
        i=0
        for split in str:
            str2[i]=split.split(',')
            i=i+1
        self.updateModel(str)
        pass

    def messageIsValid(message):
        if message[0] in datalist.keys():
            try:
                float(message[1])
                return True
            except ValueError:
                print('Invaild message')
                return False
        else:
            print('Invaild message')
            return False

    def parsemessage(self, msg):
        '''
        code to parse message
        '''
        str1=[]
        str1=msg.split(';')
        for item in str1:
            print item
        return

    def updateModel(self, info):
        '''

        :return:
        '''
        for i in range(0, info.size()):
            if(self.messageIsValid(info[i])):
                datalist[info[i][0]].setCurrentValue()
        pass