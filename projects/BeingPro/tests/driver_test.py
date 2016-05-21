from nose.tools import *
import driver

def setup():
    driver.PrintInfo()
    print "SETUP!"
    
def teardown():
    print "TEAR DOWN!"
    
def test_basic():
    print "I RAN!"