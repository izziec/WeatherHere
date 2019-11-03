from WeatherDataCollection import WeatherCollection
from GoogleMapsDirections import GoogleMapsDirections


def run(start, end):

    getDir = GoogleMapsDirections((start, end), 'driving')
    startCord, endCord, googleDirs = getDir.getDirections()
    print('Start:', start, startCord, '\nDestination:', end, endCord)

    getWeatherStart = WeatherCollection((startCord['lat'], startCord['lng']))
    print('Weather in', start, ':', getWeatherStart.get_weather())

    getWeatherEnd = WeatherCollection((endCord['lat'], endCord['lng']))
    print('Weather in', end, ':', getWeatherEnd.get_weather())


run('Boston', 'Centreville')
