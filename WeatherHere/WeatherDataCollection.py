import json
import urllib.request


class WeatherCollection:

    def __init__(self, location):
        self.API = 'AIkWklh7Z3m26EMr6gssS4PHn5X4z1Oi'
        self.lat, self.lon = location
        self.city = self.get_location()


    def get_location(self):
        url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=%s' \
              '&q=%s,%s' \
              '&details=true' % (self.API, self.lat, self.lon)
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return data['Key']

    def get_weather(self):
        url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (self.city, self.API)
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        print(data[0]['LocalObservationDateTime'][11:])
        return (data[0]['Temperature']['Imperial']['Value'],
                data[0]['RelativeHumidity'],
                data[0]['Wind']['Direction']['Degrees'],
                data[0]['Wind']['Speed']['Imperial']['Value'],
                data[0]['WindChillTemperature']['Imperial']['Value'],
                data[0]['UVIndex'],
                data[0]['CloudCover'],
                data[0]['Pressure']['Metric']['Value'],
                data[0]['Precip1hr']['Metric']['Value'],
                data[0]['LocalObservationDataTime'])
