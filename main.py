################# Imports ####################
from waitress import serve
from flask import Flask, render_template,jsonify
from bitcoinrpc.authproxy import AuthServiceProxy
##############################################
#user and password for rpc server e.g bunkercoind
rpcuser = "" #user
rpcpass = "" #password

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles') #get the html files

apiversion=2.2 #api version

@app.route('/')
def index():
    return render_template('index.html') #index page
############# app routes ##################
@app.route("/apiinfo")
def apiinfo():
    return jsonify({
        "apiver": apiversion,
        "result": {
            "id": "bkc-rest-api",
            "version": apiversion,
            "description": "Bunkercoin REST API Alpha 2.1",
            "author": "The Bunkercoin Project"
        }
    })

@app.route("/blockcount")
def blockcount():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getblockcount()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "blockcount": result
        }
    })

@app.route("/blockbyheight/<int:height>")
def blockbyheight(height):
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
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
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getnetworkhashps()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "hashrate": result
        }
    })


@app.route("/diff")
def diff():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getdifficulty()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "difficulty": result
        }
    })

@app.route("/meminfo")
def meminfo():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getmempoolinfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "mempool": result
        }
    })

@app.route("/info")
def info():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getinfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })


@app.route("/blockchaininfo")
def blockchaininfo():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getblockchaininfo()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })
@app.route("/chaintips")
def chaintips():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getchaintips()
    return jsonify({
        "apiver": apiversion,
        "result": {
            "info": result
        }
    })
@app.route("/serverinfo")
def serverinfo():
    rpc_connection = AuthServiceProxy(f"http://{rpcuser}:{rpcpass}@127.0.0.1:22555")
    result = rpc_connection.getmemoryinfo()
    return jsonify({
        "Server memory info ": result
    })
################################
@app.errorhandler(404)#404 "page not found" error handler
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    serve(app, port=5001)#run our Flask app