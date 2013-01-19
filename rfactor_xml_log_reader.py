#coding: utf-8

from core import xml_reader
import sys

def dump_data(args):
    xml_file = xml_reader.openXML(args[0])
    qualy_circuit = xml_reader.get_qualy_circuit(xml_file)
    print qualy_circuit



if __name__ == '__main__':
    print '---'
    dump_data(sys.argv[1:])
