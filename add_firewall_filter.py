#!/usr/bin/python

import requests

url = "https://192.168.1.254"

# Read api access file in raw format as downloaded from firewall
with open("/home/ada/Downloads/OPNsense.localdomain_root_apikey.txt") as fp:
    lines = fp.readlines()
api_key = lines[0].rstrip("\n").split("=")[1]
api_secret = lines[1].rstrip("\n").split("=")[1]

rules = [
    {
        "description": "",
        "source_net": "192.168.1.0/24",
        "protocol": "TCP",
        "destination_net": "192.168.2.8/29",
        "destination_port": "3389"
    },
    {
        "description": "",
        "source_net": "192.168.1.0/24",
        "protocol": "TCP",
        "destination_net": "192.168.2.16/29",
        "destination_port": "3389"
    },
    {
        "description": "",
        "source_net": "192.168.1.0/24",
        "protocol": "TCP",
        "destination_net": "192.168.2.24/29",
        "destination_port": "3389"
    },
    {
        "description": "",
        "source_net": "192.168.1.0/24",
        "protocol": "TCP",
        "destination_net": "192.168.2.32/29",
        "destination_port": "3389"
    },
    {
        "description": "",
        "source_net": "192.168.1.0/24",
        "protocol": "TCP",
        "destination_net": "192.168.2.40/29",
        "destination_port": "3389"
    },
    {
        "description": "",
        "source_net": "192.168.1.0/24",
        "protocol": "TCP",
        "destination_net": "192.168.2.48/29",
        "destination_port": "3389"
    },
]

for rule in rules:
    post_data = {
        "rule": {
            "description": rule["description"],
            "source_net": rule["source_net"],
            "protocol": rule["protocol"],
            "destination_net": rule["destination_net"],
            "destination_port": rule["destination_port"]
        }
    }
    r = requests.post(url + "/api/firewall/filter/add_rule/", json=post_data, auth=(api_key, api_secret), verify=False)
    print(r.status_code)
    print(r.text)
r = requests.post(url + "/api/firewall/filter/apply", auth=(api_key, api_secret), verify=False)
print(r.status_code)
print(r.text)
