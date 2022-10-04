# 多重継承
# 継承元が複数存在するクラス
class Person(object):
    def talk(self):
        print('talk')

    """
    多重クラスの場合、他の継承元のクラスに同じメソッド名のものがあると、
    継承先(今回の場合は PersonCarRobotクラス)の()の中に書いてある順番に
    継承される
    """
    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Car, Person):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()