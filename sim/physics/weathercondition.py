__author__ = 'paul'

class WeatherCondition
	'''
	this class classify some weathers that can be 
	encountered; 
	later we need to add some new chages to battery,
	and other functions as well due to weathers
	'''
	def __init__(self):
	'''
	define the chages and parameters that the weather
	condition makes
	'''
		self.airdensity      #kg/(m*m*m)
		self.airvelocity       #m/s
		self.sunshine   #no idea what unit
		#there must be some change to the input received by solar panel
	

	#all the following subject to change
	def sunnyday(self):
		self.airdensity = 1.225
		self.airvelocity = 0.1
		
	def windyday(self):
		self.airdensity = 1.225
		self.airvelocity = 2.0
		
	def rainyday(self):
		self.airdensity = 0.8
		self.airvelocity = 1.5
		
	