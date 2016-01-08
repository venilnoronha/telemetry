__author__ = 'paul'
import httplib
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

if __name__ == '__main__':
    testconnection()