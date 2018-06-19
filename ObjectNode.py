import json
import os
import subprocess
class ObjectNode:
	def __init__(self, UserID):
		self.UserID = UserID
		self.ObjectHash = "NULL"
		if self.ObjectHash == "NULL":
			cmd = "echo '{ \"Data\": \""+UserID+"\" }' | ipfs object put"
			output = subprocess.check_output(cmd, shell=True)
			output = output.decode("utf-8")
			self.ObjectHash = output.split(" ")[1].split("\n")[0]
			os.system("timeout 100 ipfs pin add "+self.ObjectHash)

	def GetSwarm(self):
		Rset = set()
		cmd = "ipfs swarm peers"
		output = subprocess.check_output(cmd, shell=True)
		output = output.decode("utf-8")
		tmp = output.split("\n")
		for x in tmp:
			if x=="":continue
			Rset.add(x.split("/")[2])
		return Rset

	def ObjectPeer(self,PeerID):
		cmd = "echo '{ \"Data\": \""+PeerID+"\" }' | ipfs object put"
		output = subprocess.check_output(cmd, shell=True)
		output = output.decode("utf-8")
		PeerHash = output.split(" ")[1].split("\n")[0]
		return PeerHash	

	def AddHash(self,Fhash,ObjectName):
		if Fhash == "NotYet":
			return
		cmd = "timeout 10 ipfs object patch add-link "+self.ObjectHash+" "+ObjectName+" "+Fhash
		output = "OUTPUT ERROR"
		try:
			output = subprocess.check_output(cmd, shell=True)
			output = output.decode("utf-8")
			if "Error" in output:
				return
		except:
			return
		NewOhash = output.split("\n")[0]
		#os.system("timeout 10 ipfs pin add "+NewOhash)
		cmd = "timeout 10 ipfs pin add "+NewOhash
		output = subprocess.check_output(cmd, shell=True)
		output = output.decode("utf-8")
		if "Error" in output:
			return
		self.ObjectHash = NewOhash

	def RemoveHash(self,Fhash,ObjectName):
		cmd = "timeout 10 ipfs object patch rm-link "+self.ObjectHash+" "+ObjectName
		output = "OUTPUT ERROR"
		try:
			output = subprocess.check_output(cmd, shell=True)
			output = output.decode("utf-8")
			if "Error" in output:
				return
		except:
			return
		NewOhash = output.split("\n")[0]
		#os.system("timeout 10 ipfs pin add "+NewOhash)
		cmd = "timeout 10 ipfs pin add "+NewOhash
		output = subprocess.check_output(cmd, shell=True)
		output = output.decode("utf-8")
		if "Error" in output:
			return
		if NewOhash != self.ObjectHash:
			os.system("timeout 10 ipfs pin rm "+self.ObjectHash)
		self.ObjectHash = NewOhash

	def GetJsonObjectInfo(self, ObjectHash):
		cmd = "timeout 10 ipfs object get "+ObjectHash
		try:
			output = subprocess.check_output(cmd, shell=True)
			output = output.decode("utf-8")
			if "Error" in output:
				return
			JsonOutput = json.loads(output)
			return JsonOutput
		except:
			return "GetJsonObjectInfo ERROR"
