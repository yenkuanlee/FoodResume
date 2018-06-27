pragma solidity ^0.4.21;

contract Resume {

    function Resume() public{
    }

    struct itemRecord {
        uint256 index;
        string[] itemList;
    }

    mapping (string => address[]) itemFlow; // some item sales to someone
    mapping (address => itemRecord) itemLog; // someone generate some items
    mapping (address => string[]) Notice; // call someone to check

    function stringToBytes32(string memory source) returns (bytes32 result) {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }
        assembly {
            result := mload(add(source, 32))
        }
    }

    function stringsEqual(string storage _a, string memory _b) internal constant returns (bool) {
        bytes storage a = bytes(_a);
        bytes memory b = bytes(_b);
        if (a.length != b.length)
            return false;
        for (uint i = 0; i < a.length; i ++)
            if (a[i] != b[i])
                return false;
        return true;
    }

//==================================================== Start Logic

    function Record(string ObjectHash) public returns (string){
        bytes memory tmpOH = bytes(ObjectHash);
        if(tmpOH.length!=46)
            return "HashErrorException";
        for(uint i=0;i<itemLog[msg.sender].itemList.length;i++){
            if(stringsEqual(itemLog[msg.sender].itemList[i],ObjectHash))
                return "DuplicateObjectHashException";
        }
        itemLog[msg.sender].index ++;
        itemLog[msg.sender].itemList.length = itemLog[msg.sender].index;
        itemLog[msg.sender].itemList[itemLog[msg.sender].index-1] = ObjectHash;
        return "SUCCESS";
    }

    function SendNotice(string ObjectHash, address client) public returns(string){
        bool flag = false;
        for(uint i=0;i<itemLog[msg.sender].itemList.length;i++){
            if(stringsEqual(itemLog[msg.sender].itemList[i],ObjectHash))
                flag = true;
        }
        if(flag){
            Notice[client].length++;
            Notice[client][Notice[client].length-1] = ObjectHash;
            return "SUCCESS";
        }
        return "NoObjectHashException";
    }

    function GetNotice() public returns(string){
        string memory Stmp = new string(Notice[msg.sender].length*47);
        bytes memory Btmp = bytes(Stmp);
        uint k = 0;
        for(uint i=0;i<Notice[msg.sender].length;i++){
            bytes memory Ntmp = bytes(Notice[msg.sender][i]);
            for(uint j=0;j<Ntmp.length;j++)
                Btmp[k++] = Ntmp[j];
            Btmp[k++] = ";";
        }
        return string(Btmp);
    }

    function FillItem(string ObjectHash) public returns(string){
        for(uint i=0;i<itemFlow[ObjectHash].length;i++){
            if(itemFlow[ObjectHash][i] == msg.sender)
                return "AlreadyFilledException";
        }
        bool flag = false;
        for(i=0;i<Notice[msg.sender].length;i++){
            if(stringsEqual(Notice[msg.sender][i],ObjectHash))
                flag = true;
        }
        if(flag){
            itemFlow[ObjectHash].length++;
            itemFlow[ObjectHash][itemFlow[ObjectHash].length-1] = msg.sender;
            return "SUCCESS";
        }
        return "NoObjectHashException";
    }

    function GetStringItemFlow(string ObjectHash) public returns(address[]){
        return itemFlow[ObjectHash];
    }

    function GetIndex() public returns(uint256){
        return itemLog[msg.sender].index;
    }

    function GetObjectHash(uint256 indexx) public returns(string){
        return itemLog[msg.sender].itemList[indexx];
    }

    function GetStringInfo()public returns(string){
        uint256 indexx = GetIndex();
        string memory Stmp = new string(indexx*47);
        bytes memory Btmp = bytes(Stmp);
        uint k = 0;
        for(uint256 i=0;i<indexx;i++){
            bytes memory Ntmp = bytes(GetObjectHash(indexx-1-i));
            for(uint j=0;j<Ntmp.length;j++)
                Btmp[k++] = Ntmp[j];
            Btmp[k++] = ";";
        }
        return string(Btmp);
    }
    function GetInfo() public returns(bytes32[]){
        uint256 indexx = GetIndex();
        bytes32[] bytesArray;
        bytesArray.length = indexx;
        for(uint256 i=0;i<indexx;i++){
            bytesArray[i] = stringToBytes32(GetObjectHash(indexx-1-i));
        }
        return bytesArray;
    }
}
