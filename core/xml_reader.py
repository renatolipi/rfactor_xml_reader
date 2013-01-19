#coding:utf-8

from bs4 import BeautifulSoup

def openXML(input_file):
    xml_file = BeautifulSoup(open(input_file))
    return xml_file

def get_qualy_circuit(xml_file):
    return xml_file.raceresults.trackcourse.string


