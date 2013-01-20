#coding:utf-8

from race_core import RaceFile


def race_demo(input_file):
    print 'Reading race log... (it takes a minute)'
    race = RaceFile(input_file)
    print '\nRaceFile demo:'
    print 'Circuit: {}'.format(race.track_name)
    print 'Length: {}m'.format(race.track_length)
    print 'Laps: {}'.format(race.race_laps)
    print 'Time: {}'.format(race.race_time)
    print 'Race length: {}\n'.format(race.race_length)
    print 'Session start: {}'.format(race.session_start)
    print 'Session length: {} min'.format(race.session_length)
    print 'Fuel consumption: {}x'.format(race.fuel_consumption)
    print 'Tire consumption: {}x'.format(race.tire_consumption)
    print 'Drivers on session: {}\n\n'.format(race.drivers_on_session)

def parse_it(input_file, output_mode):
	race_demo(input_file)