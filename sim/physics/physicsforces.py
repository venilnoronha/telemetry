__author__ = 'austin'
import math

class OutsideForceModel:
	'''
	this class shall take care of the outer forces of the car
	wind force, wheel friction,etc
	'''
	def RollingCoeffient(mass, tyrepres, velocity):
		'''
		c is rolling coeffient, tyrepres is tyre pressure(unit:bar)
		vk is velocity with unit km/has_key
		All double
		'''
		if c is None:
		vk = velocity * 3.6
		rollc = 0.005 + (1/p)*(0.01+0.0095*(vk/100)*(vk/100))
		return rollc
		
	def WheelFriction(rollc, mass, angle):
		'''
		angle is the angle between car and horizental plain,
		this is to calculate narmal force
		angle is in radians!
		'''
		Nf = mass*9.8*cos(angle)
		Wf = rollc * Nf
		return Wf
		
	def DragForce(airdensity, velocity, airvelocity, dragc, surfacearea):
		'''
		airdensity shall be in unit kg/m3
		dragc is drag coefficient, it depends on the shape of the 
		car and on the Reynolds number
		'''
		Df = 0.5*airdensity*(velocity+airvelocity)*(velocity+airvelocity)*dragc*surfacearea
		return Df
		
		
