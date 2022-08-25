import pytest
import subprocess

def test_memory(setUp):
    print("Calculate the Memory Usage:")
    list_of_arg = setUp
    memory = list_of_arg[0]
    mem_cmd = memory
    print(mem_cmd)

    # sub = subprocess.Popen(mem_cmd, shell=True, stdout=subprocess.PIPE)
    # subprocess_return = sub.stdout.read()
    #
    # used = int(subprocess_return.split('\n')[1].split()[2]) / 1024
    # free = int(subprocess_return.split('\n')[1].split()[3]) / 1024
    #
    # st = """|  Used   | Unused  |
    #  ---------------------
    # |  {:.1f}GB  |  {:.1f}GB  |"""
    #
    # print(st.format(used, free))
    #

def test_unique_num(setUp):
    print("Extracting Unique Numbers:")
    list_of_arg = setUp
    unique_num= list_of_arg[1]
    print(unique_num)

    number_list = unique_num.split(',')
    count = 0
    for i in number_list:
        if number_list.count(i) == 1:
            count += 1
    print("number of unique number in given list are ", count)

