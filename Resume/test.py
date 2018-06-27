# -*- coding: utf-8 -*-
import json
from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract
import os
import sys
Cpath = os.path.dirname(os.path.realpath(__file__))

host = 'localhost'
#account = '0x42946c2bb22ad422e7366d68d3ca07fb1862ff36' ## supplier
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

if sys.argv[1] == "GetStringInfo":
    a = contract_instance.GetStringInfo()
    tmp = a.split(";")
    for x in tmp:
        print(x)
elif sys.argv[1] == "SendNotice":
    a = contract_instance.SendNotice("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR","0xe6ab871f860d9f28764d5d2e0672396a7643710e",transact={'from': account})
    print(a)
elif sys.argv[1] == "GetNotice":
    a = contract_instance.GetNotice()
    print(a)
elif sys.argv[1] == "GetIndex":
    a = contract_instance.GetIndex()
    print(a)
elif sys.argv[1] == "FillItem":
    a = contract_instance.FillItem("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR")
    print(a)
    if a=="SUCCESS":
        a = contract_instance.FillItem("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR",transact={'from': account})
    print("TransactionID : "+a)
elif sys.argv[1] == "GetStringItemFlow":
    a = contract_instance.GetStringItemFlow("QmTAW2mzTE1dPdPcHxGhEpVaQLeaUj2nNRm3iHqnBMJhwR")
    print(a)
