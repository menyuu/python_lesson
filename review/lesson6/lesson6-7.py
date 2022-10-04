# クラス変数
class Person(object):
    # どのオブジェクトにも共通した変数の場合、クラス変数を使う
    # 定義するときは共通なのでオブジェクト自身を表す self はいらない
    kind = 'human'

    def __init__(self, name):
        # どのオブジェクトにも共通している
        # self.kind = 'human'
        self.name = name

    def who_are_you(self):
        # 呼び出すときはそのオブジェクト自身を呼び出すので self を使う
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
a.who_are_you()

# 共通したものなのでクラスから呼び出すこともできる
print(Person.kind)

# クラス変数の注意点
# クラス変数は同じ変数を参照しているためリストなどを扱う際は注意
class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')

"""
クラス変数は土のオブジェクトにも共通しているので、
クラス変数でリストを指定し、そのリストに追加すると
同じリストに追加されてしまうので注意
"""

print('c.words =', c.words)

# 異なるオブジェクトでリストが共有されるのを防ぐには __init__ で空のリストをいれる
class T(object):
    # クラス変数は複数のオブジェクトで共通して使うものにする
    # words = []

    # __init__ で初期化する場合、それをクラス変数にする必要はない
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

print('c.words =', c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')

print('d.words =', d.words)