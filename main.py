import json
from json import JSONEncoder
from waitress import serve
from flask import Flask
from flask_restful import Resource, Api, reqparse
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

app = Flask(__name__)
api = Api(app)

apiversion = "1.0"


class HelloWorld(Resource):
    print("Hello World")
    def get(self):
        return {'api': 'online'}
    pass

class apiinfo(Resource):
    print("Hello World")
    def get(self):
     return {
         'apiver': apiversion,
         'result': {
                'id': 'bkc-rest-api',
                'version': apiversion,
                'description': 'Bunkercoin REST API Alpha 0.1',
                'author': 'IdotMaster1'
         }
         } # This will print the balance
    pass

class bloc(Resource):
    print("Hello World")
    def get(self):
     rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225" % ('user', 'pass'))
     get = rpc_connection.getblockcount()
     return {
         'apiver': apiversion,
         'result': {
                {"blockcount": str(get)}
         }
         } # This will print the balance
    pass

class hashrate(Resource):
    print("Hello World")
    def get(self):
     rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225" % ('user', 'pass'))
     get = rpc_connection.getnetworkhashps()
     return {
         'apiver': apiversion,
         'result': {
                {"hashrate": str(get)}
         }
         } # This will print the balance
    pass

class diff(Resource):
    print("Hello World")
    def get(self):
     rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225" % ('user', 'pass'))
     get = rpc_connection.getdifficulty()
     return {
         'apiver': apiversion,
         'result': {
                 {"difficulty": str(get)}
         }
         } # This will print the balance
    pass

class mempoolinfo(Resource):
    print("Hello World")
    def get(self):
     rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225" % ('user', 'pass'))
     get = rpc_connection.getmempoolinfo()
     return {
         'apiver': apiversion,
         'result': 
         {
             {"mempool": str(get)}
         }
     }
          # This will print the balance
    pass

class chaininfo(Resource):
    print("Hello World")
    def get(self):
     rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225" % ('user', 'pass'))
     get = rpc_connection.getinfo()
     return {
         'apiver': apiversion,
         'result': {"info": str(get)}
     }
          # This will print the balance
    pass
class blockchaininfo(Resource):
    print("Hello World")
    def get(self):
     rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225" % ('user', 'pass'))
     get = rpc_connection.getblockchaininfo()
     return {
         'apiver': apiversion,
         'result': {"info": str(get)}
     }
          # This will print the balance
    pass

api.add_resource(bloc, '/blockcount')  # 
api.add_resource(apiinfo, '/apinfo')  # 
api.add_resource(hashrate, '/hashrate')  # 
api.add_resource(diff, '/diff')  # 
api.add_resource(mempoolinfo, '/meminfo')  # 
api.add_resource(chaininfo, '/info')  # 
api.add_resource(blockchaininfo, '/blockchaininfo')  #


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)  # run our Flask app
