__author__ = 'paul'
import socket   #for sockets
import sys  #for exit
import threading
import model
import time
from kivy.clock import Clock
import datetime

class SolarCarConnector:
    HOST="10.120.60.40"
    PORT=13000
    message=""
    keepthreading=True
    NUMGRAPHS=6
    TIMEOUT=15
    SAMPLESPEED_S=0.02
    str=""

    """
    this class handles actually making a connection to the simulation or the actual microprocessor.
    """
    def __init__(self):
        #global thread
        print(threading.active_count())
        try:
            #create an AF_INET, STREAM socket (TCP)
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit()
        print 'Socket Created'
        try:
            thread = threading.Thread(target=self.startserv, args=())
            thread.daemon=True
            thread.start()
        except:
            print 'fucked up'
        pass

    def close(self):

        self.keepthreading=False
        self.s.close()

    def startserv(self):
        '''
        should attempt to establish a connection and spin off a new thread that polls every @pollrate seconds(or something)
        do whatever necessary for when you can't establish a connection...
        do NOT block the main UI with this.
        :return:
        '''
        self.keepthreading=True
        print 'starting serv'
        print 'please run SimData'
        print 'startserv running from graphs.py'
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.s.bind((self.HOST, self.PORT))
        except socket.error , msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

        print 'Socket bind complete'

        self.s.listen(1)
        print 'Socket now listening'
        conn, addr = self.s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        self.readstringevent= Clock.schedule_interval(self.updateReadString, 1 / 10.)
        self.poll(conn)

        pass

    def poll(self,sock):
        '''
        grr...idk how to make private methods...
        should be called within thread in startserv
        :return:
        '''
        sock.settimeout(self.TIMEOUT)

        while self.keepthreading:
            sock.sendall("poll")
            try:
                self.message=sock.recv(128)
            except socket.timeout:
                print('Connection timed out. Disconnected')
                self.message="quit"
            #print self.message
            if not self.message:
                continue
            if (self.message=="quit"):
                print("Disconnected, restarting server")
                self.keepthreading=False
                sock.close()
                Clock.unschedule(self.readstringevent)
                self.startserv()
                break
            if(self.message=="stop"):
                self.keepthreading=False
                print("Stopped")
                sock.close()
                break
            self.str=self.message.split(';')
            time.sleep(self.SAMPLESPEED_S)

        print("unscheduled")
        pass

    def updateReadString(self, *args):
        if(len(self.str)!=0):
            if(len(self.str)<=self.NUMGRAPHS):
                str2=[[0 for x in range(2)] for x in range(len(self.str))]
                i=0
                for s in self.str:
                    str2[i][0], str2[i][1]=s.split(':')
                    i=i+1
                self.updateModel(str2)
            else:
                print "error: recieved message: "+ self.message
        return

    def messageIsValid(self,val=[]):
        if val[0] in model.datalist.keys():
            try:
                int(val[1])
                return True
            except ValueError:
                print('Invalid value')
                return False
        else:
            print('Invalid key:')
            return False

    def updateModel(self, info):
        '''

        :return:
        '''
        for i in range(0, len(info)):
            if(self.messageIsValid(info[i])):
                model.datalist[info[i][0]].setCurrentVal(int(info[i][1]))
        pass
