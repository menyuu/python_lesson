from xmlrpc.server import SimpleXMLRPCServer


# こちらで処理を行う
# サーバー側で処理する
# REST より簡単に書けるが、現在は REST のほうが好まれている
with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    def add_num(x, y):
        return x + y

    server.register_function(add_num, 'add_num')
    server.serve_forever()