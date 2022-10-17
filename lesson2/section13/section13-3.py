# GET などが簡単に書ける
import requests


payload = {'key1': 'value1', 'key2': 'value2'}

# r = requests.get('http://httpbin.org/get', params=payload)
# r = requests.post('http://httpbin.org/post', data=payload)
# r = requests.put('http://httpbin.org/put', data=payload)
r = requests.delete('http://httpbin.org/delete', data=payload)

# タイムアウトさせて次に行きたい場合に timeout を使う
r = requests.get('http://httpbin.org/get', params=payload, timeout=1)

print(r.status_code)
print(r.text)
print(r.json())