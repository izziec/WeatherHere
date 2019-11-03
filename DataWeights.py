from WeatherDataCollection import WeatherCollection
from sklearn import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import style; style.use('ggplot');


class DataWeights:

    def __init__(self, location):
        self.temperature, self.humidity, self.wind_bearing, self.wind_speed, self.uv_index, \
        self.cloud_cover, self.pressure, self.precipitation, self.raw \
            = WeatherCollection(location)

    def weights(self):


