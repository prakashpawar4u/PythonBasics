import pytest

@pytest.yield_fixture()
def setUp(request, m, u):
    print("Running method level setUp")
    list_of_arg = []
    list_of_arg.append(m)
    list_of_arg.append(u)
    return list_of_arg


def pytest_addoption(parser):
    parser.addoption("--m")
    parser.addoption("--u")


@pytest.fixture(scope="session")
def m(request):
    return request.config.getoption("--m")

@pytest.fixture(scope="session")
def u(request):
    return request.config.getoption("--u")
