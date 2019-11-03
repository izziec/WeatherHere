class Recommendations:

    def __init__(self, startData, endData):

        self.recommendation = ''

        self.startTemperature, self.startHumidity, self.startWindBearing, self.startWindSpeed, self.startWindChill, \
        self.startUvIndex, self.startCloudCover, self.startPressure, self.startPrecipitation, self.startTime = startData

        self.endTemperature, self.endHumidity, self.endWindBearing, self.endWindSpeed, self.endWindChill, \
        self.endUvIndex, self.endCloudCover, self.endPressure, self.endPrecipitation, self.endTime = endData

    def getRecommedation(self):
        self.startRecommendations()
        self.endRecommendations()
        return self.recommendation

    def startRecommendations(self):

        if 5 < int(self.startTime[11:13]) < 12:
            self.recommendation += 'Good Morning! '
        elif 12 <= int(self.startTime[11:13]) < 5:
            self.recommendation += 'Good Afternoon! '
        elif int(self.startTime[11:13]) > 17:
            self.recommendation += 'Good Evening! '
        elif 1 < int(self.startTime[11:13]) <= 4:
            self.recommendation += 'Is this really a good time to leave? Anyways ... '

        isCold = False
        isWindy = False
        isRaining = False

        if self.startTemperature - self.endWindChill <= -10:
            isCold = True
        if self.startPrecipitation > 0:
            isRaining = True
        if self.startWindSpeed > 30:
            isWindy = True

        if isCold:
            self.recommendation += 'It is a tad bit chilly in your area today! Put on those layers to stay warm! '
        if isRaining:
            self.recommendation += 'Seems like it has been raining in your area. Don\'t forget your umbrella! '
        if isWindy:
            self.recommendation += 'Quite windy today. The wind is blowing ' + self.getDirsName(self.startWindBearing) \
                                   + '. Wear something to break the wind or avoid traveling directly '\
                                   + self.getReverseDirs(self.startWindBearing) + '.'
        if not(isCold or isRaining or isWindy):
            self.recommendation += 'The weather is looking really nice in your area! Are you sure you want to leave?'

    def endRecommendations(self):

        isCold = False
        isWindy = False
        isRaining = False

        if self.startTemperature - self.endWindChill <= -10:
            isCold = True
        if self.startPrecipitation > 0:
            isRaining = True
        if self.startWindSpeed > 30:
            isWindy = True

        self.recommendation += '\nWhen you arrive at you destination '
        if isCold:
            self.recommendation += 'It\'s going to be brisk! Bring a jacket if you didn\'t already! '
        if isRaining:
            self.recommendation += 'It may be raining when you get there. Water gear is advised.'
        if isWindy:
            self.recommendation += 'it\'s going to be quite windy today. The wind is blowing ' + self.getDirsName(self.startWindBearing) \
                                   + '. Wear something to break the wind or avoid traveling directly ' \
                                   + self.getReverseDirs(self.startWindBearing) + '.'
        if not(isCold or isRaining or isWindy):
            self.recommendation += 'take the time to enjoy the beautiful weather!'

    def getDirsName(self, abbr):

        direction = ''
        for ch in abbr:
            if ch == 'N':
                direction += 'North'
            if ch == 'S':
                direction += 'South'
            if ch == 'W':
                direction += 'West '
            if ch == 'E':
                direction += 'East '

        if len(direction.split()) == 2:
            lst = direction.split()
            lst.insert(1, 'of')
            direction = ''
            for dirs in lst:
                direction += dirs + ' '

        return direction[:len(direction)]

    def getReverseDirs(self, abbr):
        direction = ''
        dirs = self.getDirsName(abbr)
        dirs = dirs.split()
        dirs.reverse()
        for i in dirs:
            direction += i + ' '

        if direction.count('North') > 0:
            direction = direction.replace('North', 'South')
        else:
            direction = direction.replace('South', 'North')
        if direction.count('East'):
            direction = direction.replace('East', 'West')
        else:
            direction = direction.replace('West', 'East')

        return direction[:len(direction) - 1]

