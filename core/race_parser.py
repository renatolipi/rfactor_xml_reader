#coding:utf-8

from race_core import RaceFile


def print_basic_race_data(race):
    basic_race_data = race.basic_race_data_list()
    for line in basic_race_data:
        print line
    print '\n'


def parse_it(input_file, output_mode):
    print 'Parsing racing file... (It takes a minute. Or two.)\n'
    race = RaceFile(input_file)

    if output_mode == 'raw':
        print_basic_race_data(race)

    if output_mode == 'csv':
        print 'Sorry, csv output mode not implemented yet.\n'

    if output_mode == 'html':
        print 'Sorry, html output mode not implemented yet.\n'