#coding: utf-8

import sys
from bs4 import BeautifulSoup as BS
from core import qualy_parser

APP_NAME = 'rfactor_xml_log_reader'

def print_help_text():
    print """\nThanks for using this program!\n
             How to call the parser:
             python {0} [qualy/race] path/to/your/file.xml [<leave it blank>/csv/spreadsheet/html]
             \tor
             python {0} help
             to see this help text.\n
          """.format(APP_NAME)


def validate_file(session, input_file):
    #TODO: pass BS parameter instead BSing it again.
    print 'Checking if it is a valid file... (it may take a minute)'
    try:
        xml_file = BS(open(input_file))
    except IOError:
        print "An IO error has occurred. Are you shure this file exists? Check if it is in this given path."
        sys.exit()
    #if qualy, check <RaceResults><Qualify>
    if session == 'qualy':
        content = xml_file.raceresults.qualify
        if content:
            return True
        return False
    #if race, check <RaceResults><Race>
    if session == 'race':
        content = xml_file.raceresults.race
        if content:
            return True
        return False


def parse_session(session, input_file, output_mode=None):
    if not validate_file(session, input_file):
        print 'INVALID FILE'
        sys.exit()

    print 'Session: ', session
    print 'input: ', input_file
    if not output_mode:
        output_mode = 'raw'
    print 'output: ', output_mode

    if session == 'qualy':
        qualy_parser.parse_it(input_file, output_mode)


def start_parsing(args):
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
            if output_mode not in ['csv', 'spreadsheet', 'html']:
                print 'INVALID OUTPUT MODE'
                print_help_text()
                sys.exit()
        except IndexError:
            output_mode = None

        if args[0] == 'help':
            print_help_text()
        else:
            parse_session(args[0], input_file, output_mode)
    else:
        print 'INVALID PARSER INSTRUCTION'
        print_help_text()


if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        print_help_text()
        sys.exit()

    start_parsing(sys.argv[1:])
