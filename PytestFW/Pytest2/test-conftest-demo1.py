import pytest

def test_demo1_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo1 method A")

def test_demo1_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")

def test_demo1_methodab(setUp):
    ab = 0
    if not ab:
        assert 0, "Bringup Failed"
    #print("Running demo1 method A")

