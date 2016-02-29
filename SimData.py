from Tkinter import *
import os
from socket import *
from time import sleep

#Client Stuff
ident=0
isConnected=False;
host = "localhost"
#host = "10.123.117.23" 
port = 13000
addr = (host, port)
UDPSock=socket
message="abc"

def connect():
	global UDPSock
	global isConnected
	if(isConnected==False):
		UDPSock = socket(AF_INET, SOCK_STREAM)
		try:
			UDPSock.connect((host,port))
		except:
			print('Connection cannot be established.')
			return
		print ("Connect successful")
		isConnected=True
	else:
		print('Already connected!')
		return
	master.after(66, get_data)


def disconnect():
	global UDPSock
	global isConnected
	if(isConnected==True):
		UDPSock.sendall("quit")
		master.after_cancel(ident)
		UDPSock.close()
		isConnected=False
	else:
		print("Already disconnected")

def quit():
	global UDPSock
	global master
	global isConnected
	if(isConnected==True):
		UDPSock.sendall("quit")
		UDPSock.close()
	print("Successfully closed")
	master.quit()
	sys.exit()



def get_data():
    global ident
    global isConnected
    a = str(w1.get())
    b = str(w2.get())
    c = str(w3.get())
    d = str(w4.get())
    e = str(w5.get())
    f = str(w6.get())
    data = "cabintemp:" + a + ";" + "solarvolt:" + b + ";" "batvolt:" + c + ";" + "batterytemp:" + d + ";" + "motorrpm:" + e + ";" + "motortemp:" + f
    try:
       UDPSock.sendall(data)
    except:
        print("Sending data failed. Closing connection")
        UDPSock.close()
        isConnected=False
        return
    ident=master.after(66, get_data)

#Slider Stuff
master = Tk()
w1_label = Label(master, text="cabintemp")
w1_label.pack()
w1 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w1.pack()
w1.set(10)
w2_label = Label(master, text="solarvolt")
w2_label.pack()
w2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w2.pack()
w2.set(20)
w3_label = Label(master, text="batvolt")
w3_label.pack()
w3 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w3.pack()
w3.set(30)
w4_label = Label(master, text="batterytemp")
w4_label.pack()
w4 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w4.pack()
w4.set(40)
w5_label = Label(master, text="motorrpm")
w5_label.pack()
w5 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w5.pack()
w5.set(50)
w6_label = Label(master, text="motortemp")
w6_label.pack()
w6 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w6.pack()
w6.set(60)
w7 =Button(master, text="Connect", command=connect)
w7.pack()
w7 =Button(master, text="Disconnect", command=disconnect)
w7.pack()
master.protocol("WM_DELETE_WINDOW", quit)
master.mainloop();




