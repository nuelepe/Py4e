#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
#and retrieve the first plus_code from the JSON. 
#An Open Location Code is a textual identifier that is another form of address based on the location of the address.

#You should use this API endpoint that has a static subset of the Open Street Map Data.
#http://py4e-data.dr-chuck.net/opengeo?

#This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.

#To call the API, you need to provide the address that you are requesting as the q= parameter that is properly URL encoded using the urllib.parse.urlencode() 
#function as shown in http://www.py4e.com/code3/opengeo.py

import urllib.request, urllib.parse
import json, ssl

#url to connect to the service
service_url='http://py4e-data.dr-chuck.net/opengeo?'

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location = input('Enter location: ')
    if len(location)<1: break

    #Remove blank spaces at the beggining and the end of the string
    location = location.strip()
    parameters = dict()
    parameters['q'] = location

    #Create the url by using the service and adding the encoded parameter
    url = service_url + urllib.parse.urlencode(parameters)

    print('Retrieving: ',url)
    handler = urllib.request.urlopen(url,context=ctx)
    data = handler.read().decode()
    print('Retrieved :',len(data), ' characters')

    #create the json dictionary
    try:
        json_data = json.loads(data)
    except:
        json_data = None

    if not json_data or 'features' not in json_data:
        print(' === Download error ===')
        print(data)
        break

    if len(json_data['features'])==0:
        print('Object not found')
        print(data)
        break

    print(json.dumps(json_data, indent=4))

    plus_code = json_data['features'][0]['properties']['plus_code']
    print('Plus code: ',plus_code)





