import csv
import json
import ObjectNode
import subprocess

# get supplier information

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

f = open('supplier.json','r')
line = f.readline()
Jline = json.loads(line)

Sdict = dict()

for x in Jline:
    for y in Jline[x]:
        if x not in Sdict:
            Sdict[x] = dict()
        Sdict[x][GetIngredient(y)] = y
        #print(x,GetIngredient(y),y)

# =======================================================

Fdict = dict()

with open('testt.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    flag = True # delete head
    for row in rows:
        if flag:
            flag = False
            continue
        if row[3] not in Fdict:
            Food = ObjectNode.ObjectNode(row[3])
            Fdict[row[3]] = Food
        #Ingredient = Fdict[row[3]].ObjectPeer(row[4])
        Ingredient = Sdict[row[10]][row[4]]
        Fdict[row[3]].AddHash(Ingredient,row[4])

Rdict = dict()
for x in Fdict:
    Rdict[x] = Fdict[x].ObjectHash
fw = open('gmeal.json','w')
fw.write(json.dumps(Rdict))
fw.close()

#for x in Fdict:
#    print(x,Fdict[x].ObjectHash)
