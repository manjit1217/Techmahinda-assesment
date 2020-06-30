import configparser
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

def readproperty(MainName,variable):
    config = configparser.RawConfigParser()
    config.read(os.path.join(ROOT_DIR,'Data/config.properties'))
    return config.get(MainName, variable)





