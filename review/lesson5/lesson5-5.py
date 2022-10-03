# ライブラリをインストールするときの注意点
# 標準ライブラリをインポートするときはカンマ(,)で繋げて書くこともできる
# この書き方はあまり推奨されていないので一行ずつ書いていくのがよい
# import collections, sys, os

# インポートする順番
# アルファベット順
# 標準ライブラリから書く
import collections
import os
import sys

# 標準ライブラリから一行空けてサードパーティのライブラリを書く
# 標準ライブラリかサードパーティのライブラリかを見分けられる
import termcolor

# サードパーティのライブラリから一行空けて他のチームなどが作成したパッケージを書く
import lesson_package

# 他のパッケージから一行空けて自分自身で作成したライブラリを書く
import config

# ライブラリの場所を確認する場合
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)