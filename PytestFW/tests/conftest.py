import pytest
import yaml

@pytest.yield_fixture(scope= "module")
def setUp(request, build_path, load_path):
    print("\nStarting Functional Setup Bringup")
    print("Build Path : ",build_path)
    print("Build LOCATION is :",load_path)
    print("Write command to copy {} to {}".format(load_path,build_path))
    yield
    print("#*"*80)
    print("Finally")
    y = input("Are you sure you want to delete the build path[y/n]:")
    if y=="y":
        print("Cleaning Builds from the build path")
    else:
        print("User chose not to delete the load")

@pytest.yield_fixture()
def oneTimeSetup(request, testbed, build_path,load_path):
    print("$$$$$Running One time Setup")
    print("++"*30)
    print("Testbed is :: ",testbed)
    print("++" * 30)
    print("Build Path is : ",build_path)
    print("++"*30)
    list_of_arg = []
    list_of_arg.append(testbed)
    list_of_arg.append(build_path)
    list_of_arg.append(load_path)
    #list_of_arg.append(wrapper_obj)
    return list_of_arg

def pytest_addoption(parser):
    parser.addoption("--testbed")
    parser.addoption("--build_path")
    parser.addoption("--load_path")

@pytest.fixture(scope="session")
def testbed(request):
    return request.config.getoption("--testbed")

@pytest.fixture(scope="session")
def build_path(request):
    return request.config.getoption("--build_path")

@pytest.fixture(scope="session")
def load_path(request):
    return request.config.getoption("--load_path")