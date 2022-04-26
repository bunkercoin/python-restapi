from unittest import result
from waitress import serve
from flask import Flask, jsonify, render_template
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

app = Flask(__name__)

apiversion = 2.0

username = "rpcusername"
password = "rpcpassword"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apiinfo")
def apiinfo():
    return jsonify({
        "apiver": apiversion,
        "result": {
            "id": "bkc-rest-api",
            "version": apiversion,
            "description": "Bunkercoin REST API Alpha 2.0",
            "author": "The Bunkercoin Project"
        }
    })

@app.route("/blockcount")
def blockcount():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    result = rpc_connection.getblockcount()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "blockcount": result
        }
    })

@app.route("/blockbyheight/<int:height>")
def blockbyheight(height):
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    tx = rpc_connection.getblockhash(height)
    result = rpc_connection.getblock(tx)
    return jsonify({
        "apiver": apiversion,
        "result": {
            "block": result
        }
    })

@app.route("/hashrate")
def hashrate():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    result = rpc_connection.getnetworkhashps()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "hashrate": result
        }
    })


@app.route("/diff")
def diff():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    result = rpc_connection.getdifficulty()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "difficulty": result
        }
    })

@app.route("/meminfo")
def meminfo():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    result = rpc_connection.getmempoolinfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "mempool": result
        }
    })

@app.route("/info")
def info():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    result = rpc_connection.getinfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })


@app.route("/blockchaininfo")
def blockchaininfo():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22555")
    result = rpc_connection.getblockchaininfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })


if __name__ == "__main__":
        serve(app, port=5000)  # run our Flask app
