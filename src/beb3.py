import json
from web3 import Web3
from time import sleep

ganach_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganach_url))

class gantiNama(object):
    def __init__(self):
        self.account = web3.eth.accounts[0]
    
    def setup(self):
        with open('../build/contracts/Nama.json') as f:
            self.data = json.loads(f.read())
        self.abi = self.data['abi']
        self.contract_address = web3.toChecksumAddress(self.data['networks']['5777']['address'])
        self.contract = web3.eth.contract(address = self.contract_address,abi = self.abi)
        # print(self.contract.functions.get().call())

    def setnama(self,nama):
        self.ganti_nama = self.contract.functions.set(nama).transact()
        print('Tunggu transaksi...')
        web3.eth.waitForTransactionReceipt(self.ganti_nama)
        sleep(3)
        print("Transaksi berhasil, data berhasil di ganti")

    def menu(self):
        print('---------------------------')
        print('|        Simpan Nama      |')
        print('---------------------------')
        print('| [1] Ambil Data Nama     |')
        print('| [2] Ganti Data Nama     |')
        print('---------------------------')

    def main(self):
        self.menu()
        menu_dipilih = int(input("Input pilihan anda : "))
        if menu_dipilih == 1:
            print(self.contract.functions.get().call())
        else:
            self.nama = input("Data nama baru : ")
            self.setnama(self.nama)

if __name__ == "__main__":
    belajar = gantiNama()
    belajar.setup()
    belajar.main()  
