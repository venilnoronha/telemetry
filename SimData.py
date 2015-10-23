from Tkinter import *
import os
from socket import *

#Client Stuff
host = "localhost"
#host = "10.123.117.23" 
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_STREAM)
try:
	UDPSock.connect((host,port))
except socket.error:
    print('Connection cannot be established. Exiting')
    sys.exit()

print "Connected!!!"


def get_data():
	a = str(w1.get())
	b = str(w2.get())
	c = str(w3.get())
	d = str(w4.get())
	e = str(w5.get())
	f = str(w6.get())
	data = "cabintemp:" + a + ";" + "motortemp:" + b + ";" "batterytemp:" + c + ";" + "motorrpm:" + d + ";" + "solarvolt:" + e + ";" + "batvolt:" + f
	UDPSock.sendall(data)
	master.after(66, get_data)
	
#Slider Stuff
master = Tk()
w1_label = Label(master, text="cabintemp")
w1_label.pack()
w1 = Scale(master, from_=0, to=42, orient=HORIZONTAL)
w1.pack()
w1.set(21)
w2_label = Label(master, text="motortemp")
w2_label.pack()
w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w2.pack()
w2.set(100)
w3_label = Label(master, text="batterytemp")
w3_label.pack()
w3 = Scale(master, from_=0, to=154, orient=HORIZONTAL)
w3.pack()
w3.set(77)
w4_label = Label(master, text="motorrpm")
w4_label.pack()
w4 = Scale(master, from_=0, to=154, orient=HORIZONTAL)
w4.pack()
w4.set(77)
w5_label = Label(master, text="solarvolt")
w5_label.pack()
w5 = Scale(master, from_=0, to=154, orient=HORIZONTAL)
w5.pack()
w5.set(77)
w6_label = Label(master, text="batvolt")
w6_label.pack()
w6 = Scale(master, from_=0, to=154, orient=HORIZONTAL)
w6.pack()
w6.set(77)

counter = 0
while counter < 100:
	master.after(1000, get_data)
	print('hit mainloop')
	master.mainloop()
	print('hit mainloop')
	counter = counter + 1
	'''if x == '0':
		break'''
UDPSock.close()
os._exit(0)


