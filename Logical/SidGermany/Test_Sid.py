import pytest
import argparse
import sys

# try:
#     fileName = sys.argv[1]
#     filePath = sys.argv[2]
#     #bring_up_flag = sys.argv[3]
# except Exception as e:
#     print("\n************************************Missing Required Arguments************************************\n"
#           "\t\tUsage: python Test_Sid.py Request.txt \n"
#           #           "**************************************************************************************************\n")
# sys.exit()



# parser = argparse.ArgumentParser()
# parser.add_argument('--fileName')
# args = parser.parse_args()
# fileName = args.fileName
# print("The FileName passed is:",fileName)


def test_sc1(fileExistence):
    print("##"*50)
    print("SC 1")
    fileName = fileExistence
    print("File Name Provided to Test is: ", fileName)
    print("##" * 50)


def test_sc2(fileExistence, readContent):
    print("##" * 50)
    combined_path, headerName = readContent
    print("Returned File Name :", combined_path)
    print("Header Name:", headerName)
    fp = open(combined_path,"r+")
    sipdata = fp.read()
    print(sipdata)

    sippdata = fp.readlines()
    mydict = {}
    list1 = []
    for datas in sippdata:
        print(datas)
        if (":" in datas):
            x = datas.split(":", 1)
            mydict.update({x[0]: x[1]})
        else:
            #list1= list1.append(sippdata)
            #print (list1)
            #continue
            print("No data is found!")

    print(mydict)
    print("##" * 50)

    #print("Header passed :",mydict[headerName])


#pytest -s -v Test_Sid.py --fileName response.txt --file_path C:\Users\pawarp\PycharmProjects\MyGit\prakashpawar4u\python\Logical\SidGermany\ --headerName header-1