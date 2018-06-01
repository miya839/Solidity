#!/usr/bin/python
#-*- coding: utf-8 -*- 

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
import json

if __name__ == '__main__':
    web3 = Web3(HTTPProvider('http://localhost:8545'))

    _abi = [ { "constant": True, "inputs": [], "name": "get_msg", "outputs": [ { "name": "", "type": "string", "value": "HelloEthereum" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [], "name": "msg1", "outputs": [ { "name": "", "type": "string", "value": "HelloEthereum" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "inputs": [], "payable": False, "stateMutability": "nonpayable", "type": "constructor" } ]
    contract = web3.eth.contract(abi=_abi, address = "0x2473984718a7b2974Aef57427cC0AAb28DEF1013")    
    #contract.functions.setMsg2("TEST").call()
    print (contract.functions.owner)
