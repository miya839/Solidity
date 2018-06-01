pragma solidity ^0.4.15;

contract HelloEthereum {
    address private owner;
    function HelloEthereum() {
        owner = msg.sender;
    }

    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }

    function get_msg() public onlyOwner returns(string) {
        return "HelloEthereum";
    }
}