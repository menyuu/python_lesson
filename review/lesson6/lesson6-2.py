# クラスの継承
# 既存のクラスの機能を引き継いで新たなクラスを作る
class Car(object):
    def __init__(self, model=None):
        self.model = model

    # 継承先で同じメソッドが使われる場合は継承元のクラスにメソッドを書く
    def run(self):
        print('run')

# クラスの継承をするには (object) 部分を親のクラス(今回だと (Car) にする)
# 継承したクラスは親のクラスの機能を引き継ぐ
class MyCar(Car):
    # オーバーライド
    # 継承元のメソッドを継承先のクラスで再定義することによって処理を上書きできる
    def run(self):
        print('fast')

class AdvancedCar(Car):
    # super によるオーバーライド
    # オーバーライドすると継承元の __init__ は実行されなくなる
    def __init__(self, model='SUV', enable_auto_run=False):
        # 継承元の__init__ が実行されないため継承元にもある self.model = model が必要になる
        # self.model = model
        # 同じ処理を避けるため super を使うことによって継承元のメソッドを呼び出すことができる
        # super は継承元のクラスを指しているのでドット(.)でつなぐことで継承元のクラスのメソッドを使うことができる
        super().__init__(model)
        self.enable_auto_run =enable_auto_run

    # オーバーライド
    def run(self):
        print('super fast')
    # 子クラスのメソッドは独自のメソッドとなり、他のクラスでは使えない
    def auto_run(self):
        print('auto run')

# car = Car()
# car.run()

my_car = MyCar('sedan')
my_car.run()
print(my_car.model)

advanced_car = AdvancedCar('SUV')
advanced_car.run()
advanced_car.auto_run()
print(advanced_car.model)
