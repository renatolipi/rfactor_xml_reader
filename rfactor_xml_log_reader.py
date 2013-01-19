#coding: utf-8

from core import xml_reader
import sys


def demonstration(args):
    qualifying = xml_reader.QualyFile(args[0])
    print 'QualyFile'
    print 'Circuit: {}'.format(qualifying.track_name)
    print 'Length: {}m'.format(qualifying.track_length)
    print 'Laps: {}'.format(qualifying.race_laps)
    print 'Time: {}'.format(qualifying.race_time)
    print 'Race length: {}'.format(qualifying.race_length)
    print 'Session time: {}'.format(qualifying.session_time)
    print 'Fuel consumption: {}x'.format(qualifying.fuel_consumption)
    print 'Tire consumption: {}x'.format(qualifying.tire_consumption)
    print 'Drivers on session: {}'.format(qualifying.drivers_on_session)

if __name__ == '__main__':
    demonstration(sys.argv[1:])
