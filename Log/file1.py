import os
import logging
import time
from file2 import *
#import file2


import custom_logger as cl
log=cl.customLoggerMethod(logging.DEBUG)

# logging.basicConfig(format='%(asctime)s - %(levelname)s :::: %(message)s',
#                         datefmt='%m/%d/%Y %I:%M:%S',
#                         filename='test.log', level=logging.INFO)
# log = logging.getLogger(__name__)
#

print("Starting Logger")
log.info("StartingLogger")
print("File DIr:",os.path.dirname(__file__))
logDir = os.path.dirname(__file__)
print("ABS Path:", os.path.abspath(os.path.dirname(__file__)))
print("Join", os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'aut_logs'))

time.sleep(1)
for i in range(3):
    log.info("waiting for secs:{}".format(i))

print("Ending time")
log.info("Ending Time")

print("#~"*40)
test1()
test2()