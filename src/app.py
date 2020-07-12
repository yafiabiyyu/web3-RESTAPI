from flask import Flask,jsonify, request
from web3 import Web3


app = Flask(__name__)
ganache_endpoint = "https://ropsten.infura.io/v3/<Isi dengan Project ID masing masing>"
web3 = Web3(Web3.HTTPProvider(ganache_endpoint))

"""
Alamat address ethereum dibawah ini hanya digunakan untuk testing,
jangan dipergunakan untuk wallet ethereum pribadi
karena private key disebar di ranah public
"""
address = "0x79B40e448Fd12C86824E90b5B449302429B32384"
priv_key = "065b87316b0839f07bc711d82c489e3ae3ca0ba5d37830ceb0793472ef2612d7"

@app.route("/",methods=['GET'])
def index():
    response = {
        'message':'Ini halaman index',
        'status':'Berhasil'
    }
    return jsonify(response)

@app.route("/web3/status",methods=['GET'])
def web3_status():
    response = {
        'message':'Status web3',
        'aktif': web3.isConnected()
    }
    return jsonify(response)

@app.route("/web3/create/account",methods=['POST'])
def create_account():
    data = request.get_json()
    account = web3.eth.account.create(data['password'])
    response = {
        'message':'Account berhasil dibuat',
        'data':{
            'privateKey': bytearray(account.privateKey).hex(),
            'address':str(account.address)
        }
    }
    return jsonify(response)

@app.route("/web3/balance/<address_check>",methods=['GET'])
def get_balance(address_check):
    account_balance = web3.eth.getBalance(address_check)
    response = {
        'data':{
            'balance': float(web3.fromWei(account_balance,'ether')),
            'address':address_check
        },
        'message':'Berhasil ambil data address'
    }
    return jsonify(response)


@app.route("/web3/send/ether",methods=['POST'])
def send_ether():
    data = request.get_json()
    nonce = web3.eth.getTransactionCount(address)
    tx = {
        'nonce':nonce,
        'to':data['address_to'],
        'value':web3.toWei(data['amount'],'ether'),
        'gas':2000000,
        'gasPrice':web3.toWei('50','gwei')
    }
    signed_tx = web3.eth.account.sign_transaction(tx,priv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    response = {
        'data':{
            'address_to':data['address_to'],
            'amount':data['amount'],
            'tx_hash':web3.toHex(tx_hash)
        },
        'message':'Berhasil mengirim ether'
    }
    return jsonify(response)



if __name__ == "__main__":
    app.run(debug=True)
    