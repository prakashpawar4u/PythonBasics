import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
#import yaml_reader


class TestlineHandler(Exception):
    pass


class CDM(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class RRU(object):
    def __init__(self, hostname, username, password, alias, rru_type, **kwargs):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.alias = alias
        self.kwargs = kwargs
        self.type = rru_type


class TL(object):
    def __init__(self,
                 cdm,
                 cu,
                 dus, ptp):
        self.cdm = cdm
        self.cu = cu
        self.dus = dus
        self.ptp = ptp


class TestLine(object):

    def __init__(self, path, job_info={}):
        try:
            print("Inside your constructor",path, job_info)
            tl_config = []
            if not isinstance(tl_config, dict):
                raise TestlineHandler('TL config should be in dictionary format')
        except Exception as e:
            raise TestlineHandler('Failed in Testline configuration, Error message: {}'.format(e))

    @staticmethod
    def _mcms_config(config, config_path):
        if config is not None:
            print("Config is not None")
        else:
            return config

tl_config = TestLine("yamal path", {"sierra": "Suite"})