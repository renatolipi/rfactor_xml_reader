#coding: utf-8

import sys
from core.qualy_parser import QualyFile

APP_NAME = 'rfactor_xml_log_reader'

def print_help_text():
    print """\nThanks for using this program!\n
             How to call the parser:
             python {0} [qualy/race] path/to/your/file.xml [<leave it blank>/csv/spreadsheet/html]
             \tor
             python {0} help
             to see this help text.\n
          """.format(APP_NAME)


def qualy_demo(args):
    qualifying = QualyFile(args[0])
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


def qualy_parser(input_file, output=None):
    print 'QUALY PARSER'
    print 'input: ', input_file
    if not output:
        output = 'raw'
    print 'output: ', output


def race_parser(input_file, output=None):
    print 'RACE PARSER'
    print 'input: ', input_file
    if not output:
        output = 'raw'
    print 'output: ', output


def initial(args):
    #TODO: improve this function
    print '\n'
    if args[0] in ['qualy', 'race', 'help']:
        try:
            input_file = args[1]
        except IndexError:
            print_help_text()
            print 'YOU NEED TO INFORM WICH PARSER TO USE'
            sys.exit()

        try:
            output_mode = args[2]
            if output_mode not in ['', 'csv', 'spreadsheet', 'html']:
                print 'INVALID OUTPUT MODE'
                print_help_text()
                sys.exit()
        except IndexError:
            output_mode = None

        if args[0] == 'qualy':
            qualy_parser(input_file, output_mode)

        if args[0] == 'race':
            race_parser(input_file, output_mode)

        if args[0] == 'help':
            print_help_text()
    else:
        print 'INVALID PARSER INSTRUCTION'
        print_help_text()


if __name__ == '__main__':
    #qualy_demo(sys.argv[1:])
    try:
        sys.argv[1]
    except IndexError:
        print_help_text()
        sys.exit()

    initial(sys.argv[1:])
