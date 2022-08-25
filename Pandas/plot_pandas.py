import pandas
import matplotlib.pyplot as plt
import matplotlib

dl_tp = [147.0, 147.0, 147.0, 147.0, 147.0, 147.0, 144.0,145.0, 147.0,147.0, 147.0, 147.0, 147.0, 147.0, 147.0, 144.0, 147.0, 136.0, 127.0, 147.0, 147.0, 147.0, 140.0, 147.0, 147.0, 147.0, 147.0, 147.0, 147.0, 147.0, 143.0, 110.0, 110.0, 110.0, 110.0, 110.0, 110.0, 110.0, 107.0, 103.0, 96.1, 69.3, 61.0, 62.0, 58.1, 53.1, 53.6, 51.2, 39.0, 41.7, 37.6, 37.9, 41.5, 38.3, 36.0, 36.2, 35.2, 37.9, 33.5, 32.4]

RSRP = ['-68', '-69', '-70', '-70', '-71', '-72', '-73', '-74', '-75', '-76', '-77', '-78', '-79', '-80', '-81', '-83', '-84', '-85', '-85', '-86', '-87', '-89', '-90', '-91', '-92', '-93', '-94', '-94', '-95', '-96', '-97', '-98', '-99', '-100', '-101', '-102', '-103', '-104', '-105', '-106', '-107', '-108', '-109', '-110', '-111', '-113', '-114', '-115', '-116', '-117', '-118', '-119', '-120', '-119', '-120', '-119', '-119', '-119', '-119', '-118']

#rsrp = [int(x.strip('-')) for x in RSRP]

rsrp =[int(x) for x in RSRP]
print(len(dl_tp))
print(len(RSRP))
print(rsrp)
plt.plot(rsrp,dl_tp,"b")
plt.xlabel('RSRP in dbm')
plt.ylabel("Throughput in Mbps")
plt.title("DL throughput against RSRP")
plt.show()


# mini = min(dl_tp)
# maxi = max(dl_tp)
# Ymin = mini - (0.1 * mini)
# Ymax = maxi + (0.1 * maxi)
#
# plt.ylim(Ymin, Ymax)
# plt.title('DL Throughput plot')
# plt.ylabel('Throughput in Mbps')
# plt.xlabel('Time in seconds')
# plt.show()

"""
def read_stats(file_p):
    fileExists = os.path.isfile(file_p)
    print(fileExists)
    dl_tp = []
    if (fileExists):
        with open(file_p) as my_file:
            testsite_array = my_file.readlines()
        pat = re.compile(r'[\d]*.?[\d]*\sMbits/sec')
        for ele in testsite_array:
            sh = pat.search(ele)
            if (sh != None):
                dl_tp.append(float(sh.group(0).strip(' Mbits/sec')))
                print(sh)
    else:
        print("No Such file")
    print("DL TP:", dl_tp)
    print("RSRP:", rsrp_list)


inside out: b'\r\n'b'!GSTATUS: \r\n'b'Current Time:  444231\t\tTemperature: 32\r\n'b'Reset Counter: 1\t\tMode:        ONLINE         \r\n'b'System mode:   LTE        \tPS state:    Attached     \r\n'b'LTE band:      B7     \t\tLTE bw:      20 MHz  \r\n'b'LTE Rx chan:   3110\t\tLTE Tx chan: 21110\r\n'b'LTE SSC1 state:NOT ASSIGNED\r\n'b'LTE SSC2 state:NOT ASSIGNED\r\n'b'LTE SSC3 state:NOT ASSIGNED\r\n'b'LTE SSC4 state:NOT ASSIGNED\r\n'b'EMM state:     Registered     \tNormal Service \r\n'b'RRC state:     RRC Connected  \r\n'b'IMS reg state: No Srv  \t\t\r\n'b'\r\n'b'PCC RxM RSSI:  -89\t\tPCC RxM RSRP:  -117\r\n'b'PCC RxD RSSI:  -89\t\tPCC RxD RSRP:  -116\r\n'b'Tx Power:      --\t\tTAC:         0001 (1)\r\n'b'RSRQ (dB):     -8.0\t\tCell ID:     00005101 (20737)\r\n'b'SINR (dB):      8.6\r\n'b'\r\n'b'\r\n'b'OK\r\n'



!GSTATUS:
Current Time:  496474           Temperature: 25
Reset Counter: 1                Mode:        ONLINE
System mode:   LTE              PS state:    Attached
LTE band:      B7               LTE bw:      20 MHz
LTE Rx chan:   3110             LTE Tx chan: 21110
LTE SSC1 state:NOT ASSIGNED
LTE SSC2 state:NOT ASSIGNED
LTE SSC3 state:NOT ASSIGNED
LTE SSC4 state:NOT ASSIGNED
EMM state:     Registered       Normal Service
RRC state:     RRC Idle
IMS reg state: No Srv

PCC RxM RSSI:  -40              PCC RxM RSRP:  -66
PCC RxD RSSI:  -40              PCC RxD RSRP:  -66
Tx Power:      --               TAC:         0001 (1)
RSRQ (dB):     -6.0             Cell ID:     00005101 (20737)
SINR (dB):     30.0





!GSTATUS:
Current Time:  496557           Temperature: 24
Reset Counter: 1                Mode:        ONLINE
System mode:   LTE              PS state:    Attached
LTE band:      B7               LTE bw:      20 MHz
LTE Rx chan:   3110             LTE Tx chan: 21110
LTE SSC1 state:NOT ASSIGNED
LTE SSC2 state:NOT ASSIGNED
LTE SSC3 state:NOT ASSIGNED
LTE SSC4 state:NOT ASSIGNED
EMM state:     Registered       Normal Service
RRC state:     RRC Idle
IMS reg state: No Srv

PCC RxM RSSI:  -89              PCC RxM RSRP:  -118
PCC RxD RSSI:  -90              PCC RxD RSRP:  -118
Tx Power:      --               TAC:         0001 (1)
RSRQ (dB):     -8.6             Cell ID:     00005101 (20737)
SINR (dB):      3.8
"""