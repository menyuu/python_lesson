class Person(object):
    def talk(self):
        print('talk')

class Car(object):
    def run(self):
        print('run')

# 記述した順に呼び出す
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()