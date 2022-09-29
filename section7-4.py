class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    # def what_is_your_kind(self):
    #     return self.kind

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # クラス外にあるメソッドのように扱えるが関連性があるためクラス内に記述している
    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.kind)
print(a.x)
print(a.what_is_your_kind())

# b はオブジェクトを生成していないのでオブジェクトのメソッドを呼ぶことができない
# クラスメソッドは呼ぶことができる
b = Person
print(b.kind)
# print(b.x)
print(b.what_is_your_kind())

print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)