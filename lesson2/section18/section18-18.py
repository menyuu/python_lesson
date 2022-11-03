# 対話型シェルでは通常の呼び出しで representation として表示される
# 上2つは人間が見やすい形になる
print('s')
print(str('s'))
# Pythonオブジェクトとして表示される
print(repr('s'))

import datetime
d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))

print('{} {!s} {!r}'.format('test', 'test1', 'test2'))

class Poin(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # print を使って表示するときにわかりやすくする
    # self の属性をすべて表示したい場合などにオーバーライドするときがある
    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point<object>'


p = Poin(10, 200)
# 何もなければ、そのまま __str__ が呼び出される
print('{0}'.format(p))
# s があれば s の部分で __str__ が呼び出される
print('{0!s}'.format(p))
print('{0!r}'.format(p))