import os
import subprocess
import tarfile


"""
First Approach

tarfile = '/data3/SCM_Test/Prakash/scripts/logical/any.tar.gz'
path = '/data3/SCM_Test/Prakash/scripts/logical/'
retcode = subprocess.call(['tar', '-xvf', tarfile, '-C', path])
if retcode == 0:
    print "Extracted successfully"
else:
    raise IOError('tar exited with code %d' % retcode)"""

#2nd Approach
#my_tar = tarfile.open('/data3/SCM_Test/Prakash/scripts/logical/any.tar.gz')
#my_tar.extractall('/data3/SCM_Test/Prakash/scripts/logical/') # specify which folder to extract to
#my_tar.close()


#validation
#files = os.listdir("/data3/SCM_Test/Prakash/scripts/logical/")
#print(files)
#for i in files:
#    if i.endswith('.tar.gz'):
#        tar_file = i.split(".tar")[0]
#
#print("Tar File Name is :{}".format(tar_file))
#if tar_file in files:
#    print("Package is untarred successfully")
#else:
#    print("Unabel to untar the package")


#Approach 3
#tar_file = '/data3/SCM_Test/Prakash/scripts/logical/any.tar.gz'
#os.system("tar -xvf {}".format(tar_file))
#for i in list(os.listdir("/data3/SCM_Test/Prakash/scripts/logical/")):
#    print("Inside for loop",i)
#    if folderName==i:
#        print("Untarred Package Successfully")
#        break
#    else:
#        print ("Failed to untar the package")
#



#tarFile = os.listdir("/data3/SCM_Test/Prakash/scripts/logical/")
#temp=[x for x in tarFile if x.endswith("tar.gz")]
#temp=[x for x in os.listdir("/data3/SCM_Test/Prakash/scripts/logical/") if x.endswith("tar.gz")]
#print("Tar file Name : ", temp)


#tar_file = '/data3/SCM_Test/Prakash/scripts/logical/any.tar.gz'
#os.system("tar -xvf {}".format(tar_file))
##validation2 
#folderName = tar_file.split("/")[-1].split(".tar.gz")[0]
#if folderName in os.listdir("/data3/SCM_Test/Prakash/scripts/logical/"):
#    print("Untarred Package Successfully")
#else:
#    print ("Failed to untar the package")


import subprocess
out1 = subprocess.check_output("ls")
#print "Out Put of Untar", out1

print(os.system("tar -xvf any.tar.gz"))

