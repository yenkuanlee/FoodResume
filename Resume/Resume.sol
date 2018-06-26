pragma solidity ^0.4.21;

contract Resume {

    function Resume() public{
    }

    struct itemRecord {
        uint256 index;
        string[] itemList;
    }

    mapping (address => itemRecord) itemLog;

    function stringToBytes32(string memory source) returns (bytes32 result) {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }
        assembly {
            result := mload(add(source, 32))
        }
    }

    function Record(string ObjectHash) public{
        //if(itemLog[msg.sender].index!=0){
            itemLog[msg.sender].index ++;
            itemLog[msg.sender].itemList.length = itemLog[msg.sender].index;
            itemLog[msg.sender].itemList[itemLog[msg.sender].index-1] = ObjectHash;
        //}
    }

    function GetIndex(address a) public returns(uint256){
        return itemLog[a].index;
    }

    function GetObjectHash(address a, uint256 indexx) public returns(string){
        return itemLog[a].itemList[indexx];
    }

    function GetStringInfo(address a)public returns(string){
        uint256 indexx = GetIndex(a);
        string memory Stmp = new string(indexx*47);
        bytes memory Btmp = bytes(Stmp);
        uint k = 0;
        for(uint256 i=0;i<indexx;i++){
            bytes memory Ntmp = bytes(GetObjectHash(a,indexx-1-i));
            for(uint j=0;j<Ntmp.length;j++)
                Btmp[k++] = Ntmp[j];
            Btmp[k++] = ";";
        }
        return string(Btmp);
    }
    function GetInfo(address a) public returns(bytes32[]){
        uint256 indexx = GetIndex(a);
        bytes32[] bytesArray;
        bytesArray.length = indexx;
        for(uint256 i=0;i<indexx;i++){
            bytesArray[i] = stringToBytes32(GetObjectHash(a,indexx-1-i));
        }
        return bytesArray;
    }
}
