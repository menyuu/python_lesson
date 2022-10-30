import csv
import collections


# p = (10, 20)
# print(p[0])
# # タプルなので書き換えられない
# # p[0] = 100
# class Point(object):
#     def __init__(self, x, y):
#         # オブジェクトの変数だと書き換えられてしまう
#         self.__x = x
#         self.y = y
# p = Point(10, 20)
# print(p.x)
# print(type(p))

# # namedtuple でクラスのように扱うことができる
# # 第一引数はタイプ名
# # Point  = collections.namedtuple('Point', ['x', 'y'])
# # 第二引数で渡しているものをリストにしなくても上記と同様にできる
# Point  = collections.namedtuple('Point', 'x, y')
# p = Point(10, y=20)
# print(p.x)
# # 書き換えることができない
# # p.x = 100

# # 通常 _make で呼び出すことがないので namedtuple で呼び出していることがわかる
# p1 = Point._make([100, 200])
# print(p1)
# print(p1._asdict())
#
# # _replace を使うことによって値をコピーし新しい値を入れたオブジェクトを作ることができる
# # そのまま実行しても変更されない
# p1._replace(x=500)
# print(p1)
# # 一部値を変更してコピー
# p2 = p1._replace(x=500)
# print(p2)
#
# # 値の合計なども簡単にできる
# class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
#     @property
#     def total(self):
#         return self.x + self.y
#
# p3 = SumPoint(2, 3)
# print(p3.x, p3.y, p3.total)

# namedtuple を使って csvファイルにアクセスする
with open('names.csv', 'w', newline='\n') as csvfile:
    filenames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=filenames)
    writer.writeheader()
    writer.writerow({'first': 'Mike', 'last': 'Jackson', 'address': 'A'})
    writer.writerow({'first': 'Taro', 'last': 'Tanaka', 'address': 'B'})
    writer.writerow({'first': 'Nancy', 'last': 'Mask', 'address': 'C'})

with open('names.csv', 'r') as f:
    csv_reader = csv.reader(f)
    print(csv_reader)
    print(next(csv_reader))
    # Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        print(row)
        # names = Names._make(row)
        # print(names.first, names.last, names.address)