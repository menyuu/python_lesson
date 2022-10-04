# メソッドの振る舞いを中心に記述していくオブジェクト指向のコードの書き方をダックタイピングと呼ぶ
class Car(object):
    def ride(self, person):
        person.drive()

class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

# エラーが起こる
# baby = Baby()
# car = Car()
# car.ride(baby)

adult = Adult()
car = Car()
car.ride(adult)