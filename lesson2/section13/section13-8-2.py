import xmlrpc.client

# XML の形での呼び出し
# 処理能力はあまりない
with xmlrpc.client.ServerProxy('http://127.0.0.1:8000/') as proxy:
    print(proxy.add_num(10, 20))