import json
import urllib.request
from bs4 import BeautifulSoup

class GoogleMapsDirections:

    def __init__(self, locations, mode='driving'):
        self.origin, self.destination = locations[0], locations[1]
        self.API = 'AIzaSyCQxEAzWbYsFxNkCceFjMB2Q2U_ptAbNIg'
        self.mode = mode

    def getDirections(self):
        url = 'https://maps.googleapis.com/maps/api/directions/json?' \
              'origin=%s' \
              '&destination=%s' \
              '&mode=%s' \
              '&key=%s' % (self.origin, self.destination, self.mode, self.API)
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return (data['routes'][0]['legs'][0]['start_location'],
                data['routes'][0]['legs'][0]['end_location'],
                data['routes'])

'''
for step in legs[0]['steps']:
    html_instructions = step['html_instructions']
    print("html instructions", html_instructions)
'''
