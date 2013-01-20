#coding: utf-8

import sys
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


def parse_session(session, input_file, output_mode=None):
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
