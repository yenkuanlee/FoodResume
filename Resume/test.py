# -*- coding: utf-8 -*-
import json
from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract
import os
import sys
Cpath = os.path.dirname(os.path.realpath(__file__))

host = 'localhost'
if sys.argv[1]=="supplier":
    account = '0x42946c2bb22ad422e7366d68d3ca07fb1862ff36' ## supplier
elif sys.argv[1]=="gmeal":
    account = '0xe6ab871f860d9f28764d5d2e0672396a7643710e'  ## gmeal
passwd = '123'


# web3.py instance
w3 = Web3(HTTPProvider('http://'+host+':3000'))
w3.eth.defaultAccount = account
w3.personal.unlockAccount(account,passwd)
f = open(Cpath+'/resume.json','r')
line = f.readline()
Jline = json.loads(line)
f.close()

abi = Jline['abi']
contract_address = Jline['contract_address']


# Contract instance in concise mode
contract_instance = w3.eth.contract(abi, contract_address, ContractFactoryClass=ConciseContract)

if sys.argv[2] == "PushItem":
    a = contract_instance.Record(sys.argv[3]);
    print(a)
    if a == "SUCCESS":
        a = contract_instance.Record(sys.argv[3],transact={'from': account})
        print("TransactionID : "+a)
if sys.argv[2] == "GetStringInfo":
    a = contract_instance.GetStringInfo()
    tmp = a.split(";")
    for x in tmp:
        print(x)
elif sys.argv[2] == "SendNotice":
    ObjectHash = sys.argv[3]
    toSomone = sys.argv[4]
    a = contract_instance.SendNotice(ObjectHash,toSomeone,transact={'from': account})
    print(a)
elif sys.argv[2] == "GetNotice":
    a = contract_instance.GetNotice()
    print(a)
elif sys.argv[2] == "GetIndex":
    a = contract_instance.GetIndex()
    print(a)
elif sys.argv[2] == "FillItem":
    a = contract_instance.FillItem("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR")
    print(a)
    if a=="SUCCESS":
        a = contract_instance.FillItem("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR",transact={'from': account})
    print("TransactionID : "+a)
elif sys.argv[2] == "GetStringItemFlow":
    a = contract_instance.GetStringItemFlow("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR")
    print(a)
