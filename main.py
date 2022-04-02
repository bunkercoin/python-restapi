from flask import Flask
from flask_restful import Resource, Api, reqparse
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

app = Flask(__name__)
api = Api(app)

apiversion = "0.1"


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
                'blockcount': get
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
                'hashrate': str(get)
         }
         } # This will print the balance
    pass

api.add_resource(HelloWorld, '/online')  # '/online' should retuen {'api': 'online'} if the api is online. Yes this is a very useful comment :)
api.add_resource(bloc, '/blockcount')  # 
api.add_resource(apiinfo, '/apinfo')  # 
api.add_resource(hashrate, '/hashrate')  # 

if __name__ == '__main__':
    app.run()  # run our Flask app



































































































































































