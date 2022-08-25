import pytest
import sys
import yaml
import re
import glob
import os
import pdb

#sys.path.append('../utilities')

def test_modify_xml(setUp,oneTimeSetup):
    print("#*"*80)
    list_of_arg = oneTimeSetup
    testbed = list_of_arg[0]
    build_path = list_of_arg[1]
    build_location = list_of_arg[2]
    #wrapper_obj = list_of_arg[2]
    print("####"*30)
    print("Testbed ::", testbed)
    print("Build_path ::", build_path)
    print("Default Build Location", build_location)

def test_check(setUp):
    a = 0
    # if not a:
    #     print("AAAAA",a)
    #     print('xml modification failed')
    if not a:
        assert 0, "Bringup Failed"

def test_modify_2(setUp,oneTimeSetup):
    print("#*"*80)
    list_of_arg = oneTimeSetup
    testbed = list_of_arg[0]
    build_path = list_of_arg[1]
    build_location = list_of_arg[2]
    print("####"*30)
    print("Testbed ::", testbed)
    print("Build_path ::", build_path)
    print("Default Build Location", build_location)
