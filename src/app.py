from flask import Flask,jsonify, request
from web3 import Web3


app = Flask(__name__)
ganache_endpoint = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_endpoint))

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


if __name__ == "__main__":
    app.run(debug=True)
    