import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--build')
parser.add_argument('--platform')
args = parser.parse_args()


build = args.build
platform = args.platform
