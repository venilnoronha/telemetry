__author__ = 'paul'
import httplib
'''
Gotta make a HTTP request to the nrel database to get some data on the projected solar output of our car.
'''
def testconnection():
    requeststring = "/api/pvwatts/v5.json?api_key=DEMO_KEY&lat=40&lon=-105&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10"
    c = httplib.HTTPSConnection("developer.nrel.gov")
    c.request("GET", requeststring)
    response = c.getresponse()
    print response.status, response.reason
    data = response.read()
    print data

if __name__ == '__main__':
    testconnection()