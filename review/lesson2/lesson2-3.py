d = {'x': 10, 'y': 20}
print(d)

print(d['x'])

# 値の変更
d['x'] = 100
print(d)
d['x'] = 'xxxxx'
print(d)
# キーと値の追加
d['z'] = 200
d[1] = 10000
print(d)

# 別の辞書の作成方法
print(dict(a=10, b=20))
print(dict([('c', 30), ('d', 40)]))

# 辞書のメソッド
d = {'x': 10, 'y':20}
print(d)
# keysメソッドはキーのみを確認できる
print(d.keys())
# valuesメソッドは値のみを確認できる
print(d.values())
# updateメソッドは他の辞書型のデータを使って更新することができる
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)
# getメソッドはキーを指定して値を取得できる
print(d.get('x'))
# 存在キーを指定すると None 返る
print(d.get('z'))
print(type(d.get('z')))
# popメソッドは値を取り除くことができる
print(d.pop('x'))
print(d)
# delメソッドは削除することも可能
del d['y']
print(d)
# clearメソッドは空の辞書型のみが返る(del だと変数そのものが削除されてしまう)
d.clear()
print(d)
# in
d = {'a': 100, 'b': 200}
print('a' in d)
print('j' in d)

# 辞書のコピーの際の注意点
# 辞書は参照型なので参照元そのものの値も変更されてしまう
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)
# copyメソッドを使い回避する
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# キーと値で紐づけることができるのでオンラインストなので利用される？
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}

print(fruits['apple'])