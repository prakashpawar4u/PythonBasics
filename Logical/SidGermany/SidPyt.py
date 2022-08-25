#
# Write a Python CLI program that reads in a .txt file, which contains either a SIP request or response message following the format of RFC3261 (see the two attached example files `sip_request.txt` and `sip_response.txt`).
# Example: `python -m cli.py <options> <path-to-sip-file>/<file-name>.txt`
# The CLI program shall support the following command line options:
# a) `-p --print`: The .txt file is parsed and one of the following messages -- depending on the message type -- is printed:
#    1. Request:
#        """
#        The given SIP message is a request with:
#        request-uri: <request-uri>
#        method: <method>
#        headers:
#           <header-1>: <header-1-content>
#           <header-1>: <header-1-content>
#           <...>: <...>
#        and body:
#           <raw-body>
#        """
#    2. Response:
#       """
#       The given SIP message is a response with:
#       status code: <status-code>
#       reason: <reason>
#       headers:
#           <header-1>: <header-1-content>
#           <header-1>: <header-1-content>
#           <...>: <...>
#       and body:
#           <raw-body>
#       """
# b) `-e --exists <header-name>`: The .txt file is parsed and the program prints whether the given header exists and what its content is
#     Note: Headers in SIP are case-insensitive and so must be <header-name>
#
# The CLI program shall be tested by unit tests using `pytest`. The naming of the tests shall follow the naming suggested by Roy Osherove (see https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html), only that words are divided by `_` and all lower-case.
# ```
#
# please check it tmmrw.
#
#
#
#
#################################################################################
#usage:- python3.6 sippparser.py Exists /root/SIDD/Assignment sip_request.txt	#
#argv1:- option(any key,print,request,response)					#
#argv2:-path of a file								#
#argv3:-filename								#
#################################################################################
"""
import sys

def Keys_Exist():
	if (sys.argv[1] in mydict.keys()):
    		print ("The Keys exists")
    		print ("Value For requested Key is:", mydict[sys.argv[1]])
	else:
   		print("Key doesn't exists")

def Print_Entirefile():
	print("Inside Print_Entire_function")
	fp1 = sys.argv[2] +'/' + sys.argv[3]
	fp1= open(fp1, 'r')
	sippdata1 = fp1.read()
	print("data:", sippdata1)
	fp.close()


fp = sys.argv[2] +'/' + sys.argv[3]
fp= open(fp, 'r')
sippdata = fp.readlines()
mydict = {}
list1 = []
for  datas in sippdata:
    if (":" in datas):
        x = datas.split(":",1)
        mydict.update({x[0] : x[1]})
    else:
#        list1= list1.append(sippdata)
#        print (list1)
         continue


#print(mydict)
#print (mydict.keys())
#print (mydict.values())




if (sys.argv[1] in mydict.keys() or sys.argv[1] == "Exists"):
	Keys_Exist()
elif (sys.argv[1] == "Request" or sys.argv[1] == "Response" or sys.argv[1] == "Print"):
	Print_Entirefile()

else:
	print("you have to work more")

"""


import pytest
import sys

#
# def test_sc1(setUp,oneTimeSetup):
#     print("SC 1")
#     list_of_arg = oneTimeSetup
#     print(list_of_arg)
#
# def test_sc2(setUp,oneTimeSetup):
#     print("SC2")

def test_sc1(setUp):
    print("SC 1")
    #print(list_of_arg)

def test_sc2(oneTimeSetup):
    print("SC2")
    list_of_arg = oneTimeSetup
    print(list_of_arg)


#Single Test Execution
#pytest -s -v test_p_SidPyt.py::test_sc1 --fileName "Request" --file_path "C:\Users\pawarp\PycharmProjects\MyGit\prakashpawar4u\python\Logical\SidGermany\request.txt"

# Suite Execution
#pytest -s -v SidPyt.py --fileName "request.txt" --file_path "C:\Users\pawarp\PycharmProjects\MyGit\prakashpawar4u\python\Logical\SidGermany\request.txt"