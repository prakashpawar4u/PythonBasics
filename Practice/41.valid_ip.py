import re
st = "172.16.60.104 is my DU ip & CU IP is 10.10.4.71"
#pat = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
pat = "((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

# ips = re.findall(pat, st)
# print("IPS: ", ips)

ip = re.search(pat, st)
print(ip.group(0))