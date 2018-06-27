# -*- coding: utf-8 -*-
import json
import ObjectNode
import subprocess
import sys
import os

def GetIngredient(Fhash):
    cmd = "timeout 10 ipfs object get "+Fhash
    output = subprocess.check_output(cmd, shell=True)
    output = output.decode("utf-8")
    Joutput = json.loads(output)
    Ingredient = Joutput['Data']
    return Ingredient

# Init
god = ObjectNode.ObjectNode("god")
Sdate = god.ObjectPeer("Sdate")
Edate = god.ObjectPeer("Edate")
Company = god.ObjectPeer("Company")
CID = god.ObjectPeer("CID")

Tset = set()

if sys.argv[1] == "supplier":
    f = open('supplier.json','r')
    line = f.readline()
    Jline = json.loads(line)
    for x in Jline:
        for y in Jline[x]:
            print(x,GetIngredient(y),y)
            Tset.add(y)
    os.chdir("Resume")
    for x in Tset:
        print("supplier put item into contract : "+x)
        os.system("python3 test.py supplier PushItem "+x)
elif sys.argv[1] == "gmeal":
    f = open('gmeal.json')
    line = f.readline()
    Jline = json.loads(line)
    os.chdir("Resume")
    for x in Jline:
        print(x,Jline[x])
        print("gmeal put item into contract : "+Jline[x])
        os.system("python3 test.py gmeal PushItem "+Jline[x])
