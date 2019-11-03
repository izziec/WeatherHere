

class Recommendations:

    def __init__(self, startData, endData):

        self.recommendation = ''

        self.startTemperature, self.startHumidity, self.startWindBearing, self.startWindSpeed, self.startWindChill, \
        self.startUvIndex, self.startCloudCover, self.startPressure, self.startPrecipitation, self.startTime = startData

        self.endTemperature, self.endHumidity, self.endWindBearing, self.endWindSpeed, self.endWindChill, \
        self.endUvIndex, self.endCloudCover, self.endPressure, self.endPrecipitation, self.endTime = endData

    def startRecommendations(self):

        if 5 < int(self.startTime[11:13]) < 12:
            self.recommendation += 'Good Morning!'
        elif 12 <= int(self.startTime[11:13]) < 5:
            self.recommendation += 'Good Afternoon!'
        elif int(self.startTime[11:13]) > 17:
            self.recommendation += 'Good Evening!'
        elif 1 < int(self.startTime[11:13]) <= 4:
            self.recommendation += 'Is this really a good time to leave? Anyways...'


        return self.recommendation

    def endRecommendations(self):
        return