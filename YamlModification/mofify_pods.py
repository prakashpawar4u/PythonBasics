#!/bin/bash
import os
import re
import subprocess
path = "pods.yaml"

def finder(reg, spliter):
    cmd= "grep -Eo '" + reg + "' " + path
    print(cmd)
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    s = out.decode("utf-8")
    #p = s.split("value: ")
    p = s.split(spliter)
    print(s)
    old_version = p[1].split("\n")[0]
    print(old_version)
    return old_version

def modifier(spliter,old_version,new_version):
    cmd1 = "sed -i 's#" + spliter + old_version + "#" + spliter + new_version + "#g' " + path
    print(cmd1)
    subprocess.Popen([cmd1], stdout=subprocess.PIPE, shell=True)


#-------------------------------------------------------------------------------
#################modifying version
#reg1 = "value:[[:space:]][0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
reg1 = "value:\s[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
spliter = "value: "
old_v1 = finder(reg1,spliter)
print("OLD Value:",old_v1)
new_v1= "4.4.4.4"
print("UPDATED Value:",new_v1)

modifier(spliter,old_v1,new_v1)

#------------------------------------------------------------------------
#######modifying image name:-------------------------------------

#reg2 = "image:[[:space:]]*.*_cuup:*.*"
reg2 = "image:\s.*producttype:*.*"
spliter = "image: "
old_v2 = finder(reg2,spliter)

new_v2 = "hub/docker.com/projectName/productType:r_version_tag"
modifier(spliter,old_v2,new_v2)



