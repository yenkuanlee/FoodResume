# -*- coding: utf-8 -*-
import json
from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract
import os
import sys
Cpath = os.path.dirname(os.path.realpath(__file__))

host = 'localhost'
account = '0x42946c2bb22ad422e7366d68d3ca07fb1862ff36'
passwd = '123'


# web3.py instance
w3 = Web3(HTTPProvider('http://'+host+':3000'))
w3.personal.unlockAccount(account,passwd)
f = open(Cpath+'/resume.json','r')
line = f.readline()
Jline = json.loads(line)
f.close()

abi = Jline['abi']
contract_address = Jline['contract_address']


# Contract instance in concise mode
contract_instance = w3.eth.contract(abi, contract_address, ContractFactoryClass=ConciseContract)

contract_instance.Record(sys.argv[1],transact={'from': account})
