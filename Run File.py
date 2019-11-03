from WeatherDataCollection import WeatherCollection
from GoogleMapsDirections import GoogleMapsDirections

def run(start, end):

    getDir = GoogleMapsDirections((start, end), 'driving')
    startCord, endCord, googleDirs = getDir.getDirections()
    print('Start:', start, startCord, '\nDestination:', end, endCord)

    getWeatherStart = WeatherCollection((startCord['lat'], startCord['lng']))
    startData = getWeatherStart.get_weather()
    print('Temperature in', start, ':', str(startData[0]) + 'F')

    getWeatherEnd = WeatherCollection((endCord['lat'], endCord['lng']))
    endData = getWeatherEnd.get_weather()
    print('Temperature in', end, ':', str(endData[0]) + 'F')


run('sanfrancisco', 'Centreville')
