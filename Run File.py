from WeatherDataCollection import WeatherCollection


def run(start, end):
    weather = WeatherCollection(start)
    weatherStart = weather.get_weather()
    print(weatherStart)

    weather = WeatherCollection(end)
    weatherEnd = weather.get_weather()
    print(weatherEnd)


run('Chantilly', 'Centreville')
