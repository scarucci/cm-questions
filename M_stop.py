# sample code for citymapper
# author Simon Carucci

# TfL automatically updates GPS positions of each bus every 30s

import requests

def getTime():
    r = requests.get('http://countdown.tfl.gov.uk/stopBoard/52222') #52222 is the unique ID of London Bridge stop (M)
    json_result = r.json() # obtain json file from stopboard
    stops = json_result['arrivals']
    M_stop = []

    # search within the json file for destinations

    for x in stops:
        """

below, it is also possible to specify the direction by putting x[destination] == 'destination_name'

        """
        if x['isRealTime'] == True:
            x = str(x['routeName']) + '/' + str(x['destination']) + '/' + str(x['estimatedWait']) # routeName == routeId
            M_stop.append(x)
            print(M_stop)

