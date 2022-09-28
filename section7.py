# クラス

# object部分は書かなくてもよいが Python2 の名残から書いている
# 継承時にベースクラスとして扱うことを明示できる
class Person(object):
    # コンストラクタ(クラスの初期化)
    # インスタンスの作成と同時に実行される
    def __init__(self, name='name'):
        self.name = name
        print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    #デストラクタ(オブジェクトが破壊されるときに実行される)
    def __del__(self):
        print('good bye')

# オブジェクト指向では「人間」が「話す」といったようなものを考えるほうが直感的にわかりやすい？
# 人間がわかりやすい
person = Person('Mike')
person.say_something()

# 明示的にデリートする
del person

print('######################')

# 継承
class Car(object):
    # 何もしない時は pass をする
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enabel_auto_run=False,
                 passwd='123'):
        # 親と同じ場合は super することで親クラスの __init__ を呼び出せる
        # self.model = model
        super().__init__(model)
        # プロパティを使う場合はアンダースコア(_)を1もしくは2個使う
        # 1個：アクセスしてほしくないことを明示的にし、プロパティの仕様を促す
        # 2個：クラス内からのみアクセスさせたい場合
        # クラス内からはアクセスできる
        self.__enable_auto_run = enabel_auto_run
        self.passwd = passwd

    # プロパティは条件を付与させ機能を制限したいときに使用する
    # ゲッター
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # セッター
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

# car = Car()
# car.run()
# print('#################')
# toyota_car = ToyotaCar('Lexus')
# クラス変数も呼び出し可能
# print(toyota_car.model)
# toyota_car.run()
# print('#################')
tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
# print(tesla_car.model)
# tesla_car.run()
# tesla_car.auto_run()