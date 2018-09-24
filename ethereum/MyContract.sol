pragma solidity ^0.4.18;

contract Owned{
    address owner;
    function Owned() public{
        owner=msg.sender;
    }
    
    modifier isOwned(){
        require(msg.sender==owner);
        _;
    }

}
contract Courses is Owned{
    struct Instructors{
        
        bytes16 fName;
        bytes16 lName;
        uint256 age;
    }
    
    mapping(address => Instructors) mapOfInstructors;
    address[] public instructorAddress;
    event InstructorEvent(bytes16 fName,bytes16 lName,uint256 age);
    
    function setInstructors(address _address,bytes16 _fName,bytes16 _lName,uint256 _age) isOwned public{
      var newInstructor=mapOfInstructors[_address];   
      newInstructor.fName=_fName;
      newInstructor.lName=_lName;
      newInstructor.age=_age;
      instructorAddress.push(_address);
      emit InstructorEvent(_fName,_lName,_age);
    }
    
    function getInstructors() view public returns (address[]){
        return instructorAddress;
    }
    
    function getInstructor(address _address) view public returns(bytes16 _fName,bytes16 _lName,uint256 age){
        return (mapOfInstructors[_address].fName,mapOfInstructors[_address].lName,mapOfInstructors[_address].age);
    }
    
    function getTotalInstructors() view public returns (uint256 length){
        return instructorAddress.length;
    }
}