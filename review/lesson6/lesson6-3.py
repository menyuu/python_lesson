# プロパティ
# 特定の条件に合致した時だけ値を書き換え可能にしたい場合に使う
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(
            self, model='SUV',
            enable_auto_run=False,
            passwd='123'):
        super().__init__(model)
        # 変数の前にアンダースコア(_)を使う
        # self._enable_auto_run = enable_auto_run
        # アンダースコア(_)を2個使うことによって直接参照できないようにする
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    # ゲッター
    # クラスの変数を返すだけのメソッドを定義し、その上に @property というデコレーターを追加する
    # 読み込みのみの変更できないメソッドで、()なしで呼び出すことができる
    @property
    def enable_auto_run(self):
        # self._ をつける
        # return self._enable_auto_run
        # 直接参照できないように __ にする
        return self.__enable_auto_run

    # セッター
    # プロパティに値を設定できるようにする
    # @プロパティ名(enable_auto_run).setter でデコレーターを書くことでセッターを作成できる
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        # 特定の条件下の時にだけプロパティが変更できる
        if self.passwd == '456':
            # self._プロパティ名に引数を代入できるようにする
            # self._enable_auto_run = is_enable
            # 直接参照できないように __ にする
            self.__enable_auto_run = is_enable

    # アンダースコア(_)を2個(__)付けた状態でもクラス内からなら呼び出すことができる
    def run(self):
        print(self.__enable_auto_run)
        print('super fast')


advanced_car = AdvancedCar('SUV')
# クラスの外から変更でき書き換えられたくない場合はプロパティを使う
# アンダースコア(_)が1つのみだと、まだ変更できてしまう
# プロパティを作成したらエラーになるが、セッターがある状態だと変数が設定される
# セッターの条件によって書き換えをできないようにすると？
advanced_car.run()
advanced_car.enable_auto_run = True
print('advanced_car changed True')
# こちらからだと変更できるので定義するときに __ にする
# advanced_car._enable_auto_run = True
# __ にすることによって直接参照できないようにする
# advanced_car.__enable_auto_run = True
# print(advanced_car.model, ':', __advanced_car.enable_auto_run)
advanced_car.run()
print(advanced_car.model, ':', advanced_car.enable_auto_run)

print('####################')
advanced_car2 = AdvancedCar('4WD', passwd='456')
advanced_car2.run()
advanced_car2.enable_auto_run = True
print('advanced_car2 changed True')
advanced_car2.run()
print(advanced_car2.model, ':', advanced_car2.enable_auto_run)
