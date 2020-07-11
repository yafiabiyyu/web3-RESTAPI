const Nama = artifacts.require("Nama");

module.exports = function(deployer) {
  deployer.deploy(Nama);
};