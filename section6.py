# import文
# import sys
# print(sys.argv)

# フルパスもしくはモジュールから読み込むようようにする
# import lesson_package.utils
# 長いモジュール名なら短くする場合がある
from lesson_package.tools import utils as u

# from lesson_package.utils import say_twice

r = u.say_twice('hello')
print(r)

# 絶対パスと相対パス
# from lesson_package.talk import human
# print(human.sing())
# print(human.cry())

# アスタリスクのインポート
# from lesson_package.talk import animal
# アスタリスクでインポートすると何が入っているのかわからない場合があるので、推奨しない
from lesson_package.talk import *
print(animal.sing())
print(animal.cry())

# ImportError
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils
utils.say_twice('word')

# 組み込み関数
import builtins

builtins.print()

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking, key=ranking.get, reverse=True))

# 標準ライブラリ
s = "akgjraiogklgnfdklgjawf"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import  defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

print(d['f'])

# サードパーティのライブラリ
from termcolor import colored

print('test')
print(colored('test', 'red'))

# import時の記述の注意
# 1行ずつインポートする
# アルファベット順に記述する
# 1.標準ライブラリ, 2.サードパーティのライブラリ, 3.自分たちのパッケージ, 4.ローカルのファイル
import collections
import os
import sys

# サードパーティなどのライブラリをインポートする際は一行空ける
import termcolor

import lesson_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)

# __name__と__main__
import lesson_package.talk.animal

import config

print('lesson:', __name__)

"""
そのままの状態で lesson_package.talk.animal.sing()などを置いておくと万一別のファイルからインポートされた場合に
実行されてしまうので、例えmainのファイルであっても実行されないようにしておくために記述すると安全になる
実際のアプリケーションだとインポートもあり得るため、記述するようにする
"""
def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()


