#!/usr/bin/python

import requests

url = "https://192.168.1.254"

# Read api access file in raw format as downloaded from firewall
with open("/home/ada/Downloads/OPNsense.localdomain_root_apikey.txt") as fp:
    lines = fp.readlines()
api_key = lines[0].rstrip("\n").split("=")[1]
api_secret = lines[1].rstrip("\n").split("=")[1]

interface = "igb2"
vlans = [207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231]
interface_descr = "vlan0."

post_requests = list()
for vlan in vlans:
    post_requests.append(
            {
                "vlan": {
                    "vlanif":f"{interface_descr+str(vlan)}",
                    "if":f"{interface}",
                    "tag":f"{vlan}",
                    "pcp":"0",
                    "proto":"",
                    "descr":""
                }
            }
    )

for post_request in post_requests:
    print(post_request)
    r = requests.post(url + "/api/interfaces/vlan_settings/add_item/", json=post_request, auth=(api_key, api_secret), verify=False)
    print(r.status_code)
    print(r.text)

r = requests.post(url + "/api/interfaces/vlan_settings/reconfigure", json={}, auth=(api_key, api_secret), verify=False)
