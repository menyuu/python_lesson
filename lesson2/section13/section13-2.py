"""
REST

HTTPメソッド クライアントが行いたい処理をサーバーに伝える

GET     データの参照
POST    データの新規登録
PUT     データの更新
DELETE  データの削除
"""

import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

# GET
# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# print(url)

# with urllib.request.urlopen(url) as f:
    # decode することで人の目できれいに見えるようにできる
    # Json形式で返ってくる
    # print(f.read().decode('utf-8'))
    # Python の辞書型で返す場合
    # 返ってきたものを Python で扱える
    # r = json.loads(f.read().decode('utf-8'))
    # print(type(r))

# POST
# Request のオブジェクトを渡す
payload = json.dumps(payload).encode('utf-8')
# req = urllib.request.Request(
#     'http://httpbin.org/post', data=payload, method='POST'
# )
# with urllib.request.urlopen(req) as f:
#     print(json.loads(f.read().decode('utf-8')))

# PUT
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT'
)
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE'
)
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

