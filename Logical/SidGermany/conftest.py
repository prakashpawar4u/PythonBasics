import pytest
import os
import pdb

@pytest.yield_fixture()
def fileExistence(request, fileName):
    print("Running First Scenario:")
    print("File Name : ",fileName)
    if fileName != None:
        print("File Name is found as {}".format(fileName))
        return fileName
    else:
         assert 0, "FileName is mandatory"

@pytest.yield_fixture()
def readContent(request, fileName, file_path, headerName):
    # if fileName != None:
    #     print("File Name is found as {}".format(fileName))
    #     # return fileName
    #     #pass
    # else:
    #      assert 0, "FileName is mandatory"
    print("File Name is found as {}".format(fileName))
    print("++" * 30)
    print("File Path is : ",file_path)
    print("++"*30)
    combined_path = file_path + fileName
    print(headerName)
    print("COMBINED PATH IS :",combined_path )
    try:
        if os.path.exists(combined_path):
            print("FILE PRESENT:", combined_path)
            return combined_path, headerName
        else:
            print("FILE NOT FOUND")
            return 0
    except:
        assert 0, "FileNotFound"

    # list_of_arg = []
    # list_of_arg.append(fileName)
    # list_of_arg.append(file_path)
    # return list_of_arg

def pytest_addoption(parser):
    parser.addoption("--fileName")
    parser.addoption("--file_path")
    parser.addoption("--headerName")


@pytest.fixture(scope="session")
def fileName(request):
    return request.config.getoption("--fileName")

@pytest.fixture(scope="session")
def file_path(request):
    return request.config.getoption("--file_path")

@pytest.fixture(scope="session")
def headerName(request):
    return request.config.getoption("--headerName")


