__author__ = 'paul'
from socket import *
import socket
import threading
import time
import Tkinter as tk
from Tkinter import *
import datetime

import kivy.uix.popup
from kivy.clock import Clock

from telemetry.modelpy import model
from files.telemetrydatadump import datadump


def selectIPAddress():
    def saveValue(self):
        SolarCarConnector.HOST=ipOptions.get()
        popup.destroy()
    ipaddresses= [ip for ip in socket.gethostbyname_ex(socket.gethostname())][2]
    NORM_FONT= ("Verdana", 10)
    #popup = Popup(title="Select IPHost Address",
    #              content=Label(text="Select IPHost Address"),
    #             size_hint=(None, None), size=(300, 180))
    popup = tk.Tk()
    popup.wm_title("Select IPHost Address")
    h=180
    w=300
    popup.geometry('%dx%d+600+250' % (w, h))
    label = Label(popup, text="Please select the IP address to host from", font=NORM_FONT, wraplength= 260)
    label.pack(side="top", fill="x", pady=10, padx=20)
    ipOptions = StringVar(popup)
    ipOptions.set(ipaddresses[0])
    dropdown = apply(OptionMenu, (popup, ipOptions) + tuple(ipaddresses))
    dropdown.pack()
    buttonframe= Frame(popup,width=popup.winfo_reqwidth())
    B1 = Button(buttonframe, text="Okay", width=10, command = lambda: saveValue(popup))
    B1.grid(row=0, column=0, pady=20)
    buttonframe.pack()

    popup.mainloop()

def saveDataDialogBox(msg):
    def saveValues(input):
        SolarCarConnector.saveData=input
        SolarCarConnector.saveCSV = csv.get()
        SolarCarConnector.saveJSON = json.get()
        popup.destroy()

    NORM_FONT= ("Verdana", 10)
    popup = tk.Tk()
    popup.wm_title("Save Data")
    h=180
    w=300
    popup.geometry('%dx%d+600+250' % (w, h))
    label = Label(popup, text=msg, font=NORM_FONT, wraplength= 260)
    label.pack(side="top", fill="x", pady=10, padx=20)
    csv=BooleanVar()
    checkCSV=Checkbutton(popup,text="Save as .csv file", variable=csv)
    checkCSV.toggle()
    checkCSV.pack()
    json=BooleanVar()
    checkJSON=Checkbutton(popup,text="Save as .json file", variable=json)
    checkJSON.pack()
    buttonframe= Frame(popup,width=popup.winfo_reqwidth())
    B1 = Button(buttonframe, text="Okay", width=10, command = lambda: saveValues(True))
    B1.grid(row=0, column=0, pady=20)
    B2 = Button(buttonframe, text="Cancel", width=10, command = lambda: saveValues(False))
    B2.grid(row=0, column=1, pady=20, sticky=E)
    buttonframe.pack()

    popup.mainloop()

class SolarCarConnector:

    PORT=13000
    message=""
    keepthreading=True
    NUMGRAPHS=6
    TIMEOUT=15
    SAMPLESPEED_S=0.02
    str=""
    dump=datadump()
    updateCount=0
    UPDATE_COUNT_MODULUS=20
    starttime=''
    endtime=''
    saveData=False
    saveCSV=False
    saveJSON=False
    connected=False
    HOST=""

    """
    this class handles actually making a connection to the simulation or the actual microprocessor.
    """
    def __init__(self, ipaddr='192.168.1.110'):
        #global thread
        #selectIPAddress()
        self.HOST=socket.gethostbyname(socket.gethostname())
        self.starttime=datetime.datetime.now().strftime('%m_%d_(%H.%M')
        try:
            #create an AF_INET, STREAM socket (TCP)
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit()
        print 'Socket Created'
        try:
            thread = threading.Thread(target=self.startserv, args=())
            thread.daemon=True
            thread.start()
        except:
            print 'messed up'
        pass

    def close(self):
        #saveDataDialogBox("Would you like to save the collected data as a .json and/or .csv file?")
        if(self.saveData==True):
            self.endtime=datetime.datetime.now().strftime('%H.%M)')
            fileName1=self.starttime+'-'+self.endtime+'.json'
            fileName2=self.starttime+'-'+self.endtime+'.csv'
            if(self.saveJSON):
                self.dump.exportJSON(fileName1)
            if(self.saveCSV):
                self.dump.exportCSV(fileName2)
        self.keepthreading=False
        self.connected=False
        self.s.close()

    def startserv(self):
        '''
        should attempt to establish a connection and spin off a new thread that polls every @pollrate seconds(or something)
        do whatever necessary for when you can't establish a connection...
        do NOT block the main UI with this.
        :return:
        '''
        self.connected=False
        self.keepthreading = True
        print 'IP Address: '+str(self.HOST)
        print 'starting serv'
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.s.bind((self.HOST, self.PORT))
        except socket.error, msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

        print 'Socket bind complete'
        try:
            thread = threading.Thread(target=self.broadcastIP, args=())
            thread.daemon=True
            thread.start()
        except:
            print 'Cannot broadcast'
        pass
        self.s.listen(1)
        print 'Socket now listening'
        conn, addr = self.s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        self.connected=True
        self.readstringevent = Clock.schedule_interval(self.parseStringToModel, 1 / 10)
        self.poll(conn)

        pass

    def broadcastIP(self, *args):
        print "Starting broadcast"
        b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        b.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        try:
            b.bind(('', 9999))
        except socket.error, msg:
            if (msg[0]==10048):
                print "Already binded"
            print "Broadcast binding failed"
            return
        b.settimeout(10)
        while(self.connected==False):
            print "Waiting to receive broadcast"
            try:
                data, addr = b.recvfrom(8096)
                print "Received broadcast from "+addr[0]
                b.sendto(self.HOST, addr)
                print "Sent response"
            except socket.error:
                print "Timed out"
        print "Broadcast closed; already connected"


    def poll(self,sock):
        '''
        grr...idk how to make private methods...
        should be called within thread in startserv
        :return:
        '''
        sock.settimeout(self.TIMEOUT)
        if(threading.active_count() > 5):
            print 'High number of threads found'
            print 'Number of threads:' + str(threading.active_count())
        while self.keepthreading:
            try:
                sock.sendall("poll")
                self.message=sock.recv(128)
            except socket.timeout:
                print('Connection timed out. Disconnected')
                self.message="quit"
            except socket.error:
                self.message="quit"
            #print self.message
            if not self.message:
                continue
            if (self.message=="quit"):
                print("Disconnected, restarting server")
                self.keepthreading=False
                #unschedule this for continuous flat graph even when it isn't connected (will mess up datadump values)
                Clock.unschedule(self.readstringevent)
                self.startserv()
                break
            if(self.message=="stop"):
                self.keepthreading=False
                print("Stopped")
                sock.close()
                Clock.unschedule(self.readstringevent)
                break
            self.str=self.message.split(';')
            time.sleep(self.SAMPLESPEED_S)

        #print("unscheduled")
        pass

    def parseStringToModel(self, *args):
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
                #print('Invalid value')
                return False
        else:
            print('Invalid key:')
            return False

    def updateModel(self, info):
        '''

        :return:
        '''
        self.updateCount+=1

        for i in range(0, len(info)):
            if(self.messageIsValid(info[i])):
                if(self.updateCount==self.UPDATE_COUNT_MODULUS):
                    self.dump.appendValue(info[i][0],[time.time(),int(info[i][1])])
                model.datalist[info[i][0]].setCurrentVal(int(info[i][1]))

        if(self.updateCount==self.UPDATE_COUNT_MODULUS):
            self.updateCount=0

        pass
