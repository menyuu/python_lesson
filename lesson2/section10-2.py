# パッケージの読み込み順
# アルファベット順
# 標準ライブラリ
# import os
# import sys

# サードパーティーのライブラリ
# import flask

# ローカルのライブラリ
# import するときはモジュールを読み込む(関数を読み込むとどこのパッケージかわからなくなる)
# from roboter.controller.conversation import talk_about_restaurant
# 上で読み込むのではなく、下のほうで読み込むようにする
# import roboter.controller.conversation

# 自分のライブラリ
# import setting


# 上から2行空ける
# Exception の継承
# class MainError(Exception):
#     pass

# def main():
    # roboter.controller.conversation.talk_about_restaurant()
    # 例外処理は Exception で指定しないようにする
    # except Exception as exc:
    #     print(exc)
    # raise MainError('error')

# リスト内包括は多くなる場合は使用しない
# 見にくくなる
# x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]
# x = [i for i in [1, 2, 3]]

# 無駄なメソッドを呼び出さないようにする
# d = {'key1': 'value1', 'key2': 'value2'}
# if 'key1' in d:
#     print('test')

# 上記と同じなので keys メソッドが無駄になる
# 速度にも影響する
# if 'key1' in d.keys():
#     print('test')

# 変数名はわかりやすくする
# 省略した変数はテストだけにする
# for name, count in ranking.items():
#     print(name, count)

# if __name__ == '__main__':
#     main()

# ジェネレーターが使えるときはジェネレーターを使用する
# def t():
#     num = []
#     for i in range(10):
#         num.append(i)
#     return num
#
# for i in t():
#     print(i)
# i = t()
# print(i)
#
# def t():
#     # num = []
#     for i in range(10):
#         yield i
#         # num.append(i)
#     # return num
#
# for i in t():
#     print(i)

# 簡単な関数はラムダを使う
# def other_func(f):
#     print(f(10))
#
# def test_func(x):
#     return x * 2
#
# def test_func2(x):
#     return x * 5
#
# other_func(test_func)
# other_func(test_func2)
#
# other_func(lambda x: x * 2)
# other_func(lambda x: x * 5)

# 1行で変数を宣言し、if文を続けらられる
# y = None
# x = 1 if y else 2
# print(x)

# クロージャー
# def base(x):
#     def plus(y):
#         return x + y
#     return plus
#
# plus = base(10)
# print(plus(10))
# x = 100
# print(plus(30))

# クロージャーにすることでグローバル変数の書き換えを防げる
# 以下はグローバル変数を使用した場合
# i = 0
# def add_num():
#     def plus(y):
#         return i + y
#     return plus
#
# i = 10
# plus = add_num()
# print(plus(10))
# i = 100
# plus = add_num()
# print(plus(30))