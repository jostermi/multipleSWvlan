import requests
import json

#print "enter ip address"
#ip=raw_input()
ip = [
          '161.44.45.9',
          '161.44.45.10'
         ]

print "enter vlan to be configured"
vlanId=raw_input()

for address in ip:
    myheaders = {'content-type': 'application/json-rpc'}
    url = "http://"+address+"/ins"
    print url
    username = "admin"
    password = "C1sco123"

    payload=[
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "vlan "+vlanId,"version": 1},"id": 2},
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()
    print payload
