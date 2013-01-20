#coding:utf-8

import sys
from bs4 import BeautifulSoup as BS


class RaceFile(object):

    def __init__(self, input_file):
        try:
            self.xml_file = BS(open(input_file))
        except IOError:
            print "An IO error has occurred. Are you shure this file exists? Check if it is in this given path."
            sys.exit()

        self.__set_initial_info()

    def __set_initial_info(self):
        self.track_name = self.xml_file.trackcourse.string
        self.track_length = self.xml_file.tracklength.string

        self.race_laps = '{} laps'.format(self.xml_file.racelaps.string)
        self.race_time = '{} min'.format(self.xml_file.racetime.string)
        if self.xml_file.racelaps.string == '0':
            self.race_length = self.race_time
        else:
            self.race_length = self.race_laps

        self.session_start = self.xml_file.race.timestring.string
        self.session_length = self.xml_file.race.minutes.string
        self.fuel_consumption = self.xml_file.fuelmult.string
        self.tire_consumption = self.xml_file.tiremult.string
        self.drivers_on_session = len(self.xml_file.find_all("driver"))

    def basic_race_data_list(self):
        basic_race_data = []
        basic_race_data.append('Circuit: {}'.format(self.track_name))
        basic_race_data.append('Length: {}m'.format(self.track_length))
        basic_race_data.append('Laps: {}'.format(self.race_laps))
        basic_race_data.append('Time: {}'.format(self.race_time))
        basic_race_data.append('Race length: {}'.format(self.race_length))
        basic_race_data.append('Session start: {}'.format(self.session_start))
        basic_race_data.append('Session length: {} min'.format(self.session_length))
        basic_race_data.append('Fuel consumption: {}x'.format(self.fuel_consumption))
        basic_race_data.append('Tire consumption: {}x'.format(self.tire_consumption))
        basic_race_data.append('Drivers on session: {}'.format(self.drivers_on_session))
        return basic_race_data

    def basic_race_data_dict(self):
        basic_race_data = {}
        basic_race_data['Circuit'] = self.track_name
        basic_race_data['Circuit length'] = self.track_length
        basic_race_data['Laps'] = self.race_laps
        basic_race_data['Time'] = self.race_time
        basic_race_data['Race length'] = self.race_length
        basic_race_data['Session start'] = self.session_start
        basic_race_data['Session length'] = self.session_length
        basic_race_data['Fuel consumption'] = self.fuel_consumption
        basic_race_data['tire consumption'] = self.tire_consumption
        basic_race_data['Drivers on session'] = self.drivers_on_session
        return basic_race_data
