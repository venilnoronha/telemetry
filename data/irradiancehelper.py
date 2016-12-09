__author__ = 'paul'
import httplib
import math
import numpy
from PIL import Image

'''
Gotta make a HTTP request to the nrel database to get some data on the projected solar output of our car.
'''
def testconnection():
    apibegin = '/api/pvwatts/v5.json?'
    apikey = 'api_key=vSnjhMa0wAcb8PoIEQVqmRHd0fZJsek6QBcgw01r'#this is a key that uniquely identifies us. It doesn't really mean anything other than we need to have one.
    locationparams = '&lat=34.02&lon=-118.28'
    timeframeparam = '&timeframe=hourly'#if you don't include this, then it'll automatically give you monthly without the hours.
    remainingparams = '&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10'#stuff i dont' really care about for now so i just went with the default from example
    requeststring = apibegin+apikey+locationparams+timeframeparam+remainingparams
    c = httplib.HTTPSConnection("developer.nrel.gov")
    c.request("GET", requeststring)
    response = c.getresponse()
    print response.status, response.reason
    data = response.read()
    print data

def getirradiance(longitude, latitude):
    lonr = degreetorad(longitude)
    latr = degreetorad(latitude)
    #constants
    S0 = 1367
    obliquity = 23.4398
    eccen = 0.016704
    perihelion = 282.895
    declination = degreetorad(23)
    h0 = math.pi

    R0RE = 1 + math.e * math.cos(lonr + perihelion)

    Q = (S0 / math.pi) * R0RE * (h0 * math.sin(latr) * math.sin(declination) + math.cos(latr) * math.cos(declination) * math.sin(h0))


    costheta = math.cos(lonr) * math.sin(latr)
    return Q

def testirradiance():
    data = numpy.ndarray((180,360), int)
    max = 0
    for x in range(0, 360, 1):
        for y in range(-90, 90, 1):
            val = getirradiance(x, y)
            if(val > max):
                max = val
            data[y+90,x] = int(255*val / 5022.70)#y for row....x for col...
    im = Image.fromarray(data)
    im.show();
    print(max)




def degreetorad(d):
    return d * math.pi / 180


if __name__ == '__main__':
    testirradiance()