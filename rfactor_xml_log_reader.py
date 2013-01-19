#coding: utf-8

from core import xml_reader
import sys


def demonstration(args):
    xml_file = xml_reader.QualyFile(args[0])
    print 'QualyFile'
    print 'Circuit: {}'.format(xml_file.track_name)
    print 'Length: {}m'.format(xml_file.track_length)
    print 'Laps: {}'.format(xml_file.race_laps)
    print 'Time: {}'.format(xml_file.race_time)
    print 'Race length: {}'.format(xml_file.race_length)


if __name__ == '__main__':
    demonstration(sys.argv[1:])
