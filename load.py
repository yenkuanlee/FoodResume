import json
import ObjectNode
import subprocess
import sys

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

if sys.argv[1] == "supplier":
    f = open('supplier.json','r')
    line = f.readline()
    Jline = json.loads(line)
    for x in Jline:
        for y in Jline[x]:
            print(x,GetIngredient(y),y)
elif sys.argv[1] == "gmeal":
    f = open('gmeal.json')
    line = f.readline()
    Jline = json.loads(line)
    for x in Jline:
        print(x,Jline[x])
