// SPDX-License-Identifier: MIT
pragma solidity ^0.6.8;

contract Nama {

    string nama = "Abiyyu Yafi";

    function get() public view returns(string memory){
        return nama;
    }

    function set(string memory _nama) public {
        nama = _nama;
    }
}