#coding:utf-8

from qualy_core import QualyFile


def print_basic_qualy_data(qualifying):
    basic_qualy_data = qualifying.basic_qualy_data_list()
    for line in basic_qualy_data:
        print line
    print '\n'


def print_basic_grid(qualifying):
    basic_grid = qualifying.basic_grid_list()
    for driver in basic_grid:
        print driver
    print '\n'

def parse_it(input_file, output_mode):
    print 'Parsing qualifying file... (It takes a minute)\n'
    qualifying = QualyFile(input_file)

    if output_mode == 'raw':
        print_basic_qualy_data(qualifying)
        print_basic_grid(qualifying)

    if output_mode == 'csv':
        print 'Sorry, csv output mode not implemented yet.\n'

    if output_mode == 'html':
        print 'Sorry, html output mode not implemented yet.\n'
