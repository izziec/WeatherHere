from WeatherDataCollection import WeatherCollection
from GoogleMapsDirections import GoogleMapsDirections
from Recommendations import Recommendations


def run(start, end):

    getDir = GoogleMapsDirections((start, end), 'driving')
    startCord, endCord, googleDirs = getDir.getDirections()
    print('Start:', start, startCord, '\nDestination:', end, endCord, '\n')

    getWeatherStart = WeatherCollection((startCord['lat'], startCord['lng']))
    startData = getWeatherStart.get_weather()
    print('Current temperature in', start, ':', str(startData[0]) + 'F')

    getWeatherEnd = WeatherCollection((endCord['lat'], endCord['lng']))
    endData = getWeatherEnd.get_weather()
    print('Current temperature in', end, ':', str(endData[0]) + 'F')

    getReco = Recommendations(startData, endData)
    print('\nRoute Recommendations: ' + getReco.getRecommedation())


run('sandeigo', 'StateCollege')
