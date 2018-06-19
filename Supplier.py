import csv
import json
import ObjectNode

SupplierDict = dict()

# Init
god = ObjectNode.ObjectNode("god")
Sdate = god.ObjectPeer("Sdate")
Edate = god.ObjectPeer("Edate")
Company = god.ObjectPeer("Company")
CID = god.ObjectPeer("CID")

with open('testt.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    flag = True # delete head
    for row in rows:
        if flag:
            flag = False
            continue
        if row[10] not in SupplierDict:
            SupplierDict[row[10]] = list()
        Ingredient = ObjectNode.ObjectNode(row[4])
        if row[6] != "":
            Ingredient.AddHash(Sdate,row[6])
        if row[7] != "":
            Ingredient.AddHash(Edate,row[7])
        if row[10] != "":
            Ingredient.AddHash(Company,row[10])
        if row[12] != "":
            Ingredient.AddHash(CID,row[12])
        SupplierDict[row[10]].append(Ingredient.ObjectHash)


#for x in SupplierDict:
#    print(x,SupplierDict[x])

fw = open('supplier.json','w')
fw.write(json.dumps(SupplierDict))
fw.close()
