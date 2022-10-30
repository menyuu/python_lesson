import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# 0より大きい値を 'num' に入れたい場合
# collections.ChainMap を継承する
class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            # 何もなければ新しいキーと値を入れる
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key] = value

m = DeepChainMap(a, b, c)
m['new_num'] = 1
print(m['num'])
print(m['new_num'])
print(m.maps)



# update によって辞書型の中に入っている値が変更される
# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

# # コードを書いていてあとから a の値を元に戻したくなった場合
# m = collections.ChainMap(a, b, c)
# print(m)
# # 先ほど入れた順番でリスト型を返す
# print(m.maps)
# print(m['c'])
# # リストの順番を逆順させる
# m.maps.reverse()
# print(m['c'])
# # 値の追加
# m.maps.insert(0, {'c': 'ccccc'})
# print(m.maps)
# print(m['c'])
# # 値の削除
# del m.maps[0]
# print(m.maps)
# print(m['c'])
# # 値を更新する場合は一番最初に入れたものが書き換わる
# m['b'] = 'BBBBB'
# print(m.maps)
# print(m['b'])