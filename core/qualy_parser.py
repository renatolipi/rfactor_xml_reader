#coding:utf-8

from qualy_core import QualyFile


def qualy_demo(input_file):
    qualifying = QualyFile(input_file)
    print '\nQualyFile demo:'
    print 'Circuit: {}'.format(qualifying.track_name)
    print 'Length: {}m'.format(qualifying.track_length)
    print 'Laps: {}'.format(qualifying.race_laps)
    print 'Time: {}'.format(qualifying.race_time)
    print 'Race length: {}\n'.format(qualifying.race_length)
    print 'Session start: {}'.format(qualifying.session_start)
    print 'Session length: {} min'.format(qualifying.session_length)
    print 'Fuel consumption: {}x'.format(qualifying.fuel_consumption)
    print 'Tire consumption: {}x'.format(qualifying.tire_consumption)
    print 'Drivers on session: {}\n\n'.format(qualifying.drivers_on_session)

def parse_it(input_file, output_mode):
	qualy_demo(input_file)