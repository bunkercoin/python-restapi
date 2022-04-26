from flask import Flask, jsonify
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

##############################################
# Bunkercoin REST API
# Originally made by IdotMaster1
# Fully rewritten by BastelPichi.
# This code is distributed under GPL3 license.
# See LICENSE file for licensing.
#
# Todo: add exceptions when communication
# with bunkercoind
#
# Use a proper WSGI Server
# (e.g. Apache or NGINX) to deploy
##############################################

username = "rpcuser"
password = "rpcpassword"


apiversion = 2.0
app = Flask(__name__)

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
            "author": "BastelPichi"
        }
    })

@app.route("/blockcount")
def blockcount():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22225")
    result = rpc_connection.getblockcount()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "blockcount": result
        }
    })

@app.route("/hashrate")
def hashrate():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22225")
    result = rpc_connection.getnetworkhashps()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "hashrate": result
        }
    })


@app.route("/diff")
def diff():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22225")
    result = rpc_connection.getdifficulty()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "difficulty": result
        }
    })

@app.route("/meminfo")
def meminfo():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22225")
    result = rpc_connection.getmempoolinfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "mempool": result
        }
    })

@app.route("/info")
def info():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22225")
    result = rpc_connection.getinfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })


@app.route("/blockchaininfo")
def blockchaininfo():
    rpc_connection = AuthServiceProxy(f"http://{username}:{password}@127.0.0.1:22225")
    result = rpc_connection.getblockchaininfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
