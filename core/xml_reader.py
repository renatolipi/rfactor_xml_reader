#coding:utf-8

import sys
from bs4 import BeautifulSoup as BS


class QualyFile(object):

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
