# クラスメソッド
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    # def what_is_your_kind(self):
    #     self はオブジェクト自身
    #     return self.kind

    # クラスメソッドにすることでオブジェクトとして生成される前でもメソッドにアクセスできるようにする
    # @classmethod を付けることによってクラスメソッドにできる
    @classmethod
    # 引数self が取り出せないので引数を cls に指定する
    def what_is_your_kind(cls):
        return cls.kind


# a はオブジェクトが格納されている
a = Person()
print(a)
# a にはオブジェクトを格納しているためインスタンス変数を呼び出すことができる
print(a.x)
# クラス変数の呼び出し
print(a.kind)
# a はオブジェクトなので呼び出すことができる
# クラスメソッドにすることでオブジェクト生成前から呼び出すことができる
print(a.what_is_your_kind())


# b はクラスそのものが入っている
b = Person
print(b)
# b にはオブジェクトを格納していないのでインスタンス変数を呼び出すことができずにエラーになる
# print(b.x)
# クラス変数の呼び出し
print(b.kind)
# b はオブジェクトではなくクラスを格納しているのでオブジェクト self の引数を指定することができない
# クラスメソッドにすることでオブジェクト生成前から呼び出すことができる
print(b.what_is_your_kind())

print('####################')
# クラス変数やクラスメソッドはクラス名から呼び出すことができる
print(Person.kind)
print(Person.what_is_your_kind())


# スタティックメソッド
# @staticmethod をつけ引数に self や cls をとらないメソッド
# クラスとの関連性が薄く、クラスの外で定義しても問題ないもの
# クラスとの関連があるような処理であることを示したい場合に使う
class Person(object):

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

Person.about(1999)

# 上記と変わらない
def about(year):
    print('about human {}'.format(year))

class Person(object):
    pass

about(1999)