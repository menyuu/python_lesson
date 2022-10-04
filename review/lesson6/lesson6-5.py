# 抽象クラス
# 継承されて使うことを前提としたクラス
# そのまま使うことができない
# 3.4で追加された新しい概念(着想元はJava)

import abc

class Car(object):
    def ride(self, person):
        person.drive()

# 抽象クラスは定義する際に、()の中に metaclass=abc.ABCMeta と書くことで抽象クラスと示せる
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # 継承元のメソッドに @abc.abstractmethod を付けることで継承先で必ず実装するように指定できる
    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    # driveメソッドが継承先のクラスにないとエラーになる
    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    # driveメソッドが継承先のクラスにないとエラーになる
    def drive(self):
        print('ok')

car = Car()

# baby = Baby()
# baby.drive()

adult = Adult()
adult.drive()