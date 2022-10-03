# クラス
s = 'test test test'
# capitalizeメソッドは strクラスの中にあるメソッド
print(s.capitalize())

# クラスの作成
# クラス名のあとの () に object を入れる
# Python2 では (objet) が必要であったが Python3 では書く必要がなくなった
# Python2 の名残で (object) を記述することがある

# class Person:
# class Person():
class Person(object):
    # メソッドの記述
    # メソッドの第一引数には self を書く
    # self はオブジェクト自身を指している
    def say_something(self):
        print('hello')

# オブジェクトの作成
person = Person()
# 作成したオブジェクトから say_somethingメソッドの呼び出し
# personオブジェクトというものがありメソッド(動作)が紐づいている
# オブジェクト指向
person.say_something()

# クラスの初期化
class Person(object):
    # __init__ を定義して初期化する
    # オブジェクトが作成された時点で実行される
    def __init__(self):
        print('First')

person = Person()

# インスタンス変数
# __init__ のメソッドに引数を渡す
# 第一引数の self の後ろに第二引数を追記する
class Person(object):
    # デフォルト引数を指定することも可能
    def __init__(self, name='Default'):
        # オブジェクト自身の name に引数name を代入
        self.name = name
        # print(self.name)

    # クラスのメソッドには第一引数には必ず self を指定する
    # self を渡さなければオブジェクトに値を保持したり、自身の値やメソッドにアクセスしたりできない
    def say_something(self):
        # オブジェクト自身の名前(self.name) で呼び出すことができる
        print('I am {}. hello'.format(self.name))
        # self を使うことによってメソッドの中からメソッドを呼び出すこともできる
        # 呼び出しには self がいらず、次の対応する引数から渡していく
        self.run(10)

    def run(self, num):
        print('run' * num)

    # デストラクタ
    # 最初に実行される インストラクタ　⇔　最後に実行される　デストラクタ
    # 後に実行されるコードがなくオブジェクトが使われなくなったときに実行される
    def __del__(self):
        print('good bye')


# オブジェクトのインスタンス変数の引数として渡す
# 引数を渡さないとエラーになる
person = Person('Mike')
person2 = Person()

# 作成したオブジェクト自身の名前が呼び出し元に返される
person.say_something()

print('##########')
# デストラクタは呼び出したいタイミングで del を使いオブジェクトを消すことで呼び出すこともできる
del person
print('##########')