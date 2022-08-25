l1 = ['modify_pods.py', 'values', 'VDU_PTP_INFO.log', 'pods.yaml', 'mofify_pods.py', 'VDU_INFO.log', 'pods.yaml_orig', 'yaml_modfier.py', 'values.yaml']

d1 = {}
for i in l1:
    if "INFO" in i:
        print(i)
        sp = i.split("_INFO")[0]
        print(sp)
        fp = open(i, "r+")
        fp.readline()
        #d1[sp]=fp.readline()