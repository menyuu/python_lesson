import collections

# Python の古いバージョン完全に順番を保証されていない
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# od = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
# print(d)
# print(od)
# print(d == od)
# od2 = collections.OrderedDict({'pear': 1, 'orange': 2, 'banana': 3, 'apple': 4})
# print(d == od2)
# d に入っているものと od od2 に入っているものの中身が一緒なので True
# od と od2 に入っているものは中身は同じだが順番が違うため False
# print(od == od2)

# ソートする場合
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# キーの昇順
od = collections.OrderedDict(
    sorted(d.items(), key=lambda  t: t[0])
)
print(od)
# バリューの昇順
od = collections.OrderedDict(
    sorted(d.items(), key=lambda  t: t[1])
)
print(od)
# キーの文字数の昇順
od = collections.OrderedDict(
    sorted(d.items(), key=lambda  t: len(t[0]))
)
print(od)

# データを追加するときは最後に追加される
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
od = collections.OrderedDict(d)
print(od)
od = collections.OrderedDict(
    sorted(od.items(), key=lambda  t: t[0])
)
print(od)
od['cc'] = 100
print(od)
# データを追加してソートしたい場合は再度ソートする必要がある
od = collections.OrderedDict(
    sorted(od.items(), key=lambda  t: t[0])
)
print(od)
